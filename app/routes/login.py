from fastapi import APIRouter, Form, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from app.db import engine
from app.models import Usuario
from app.auth import verificar_senha, criar_token

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login(response: Response, email: str = Form(...), senha: str = Form(...)):
    # Verifica o usuário no banco de dados
    with Session(engine) as session:
        stmt = select(Usuario).where(Usuario.email == email)
        user = session.exec(stmt).first()
        
        if not user or not verificar_senha(senha, user.senha):
            # Retorna mensagem de erro amigável caso as credenciais sejam inválidas
            return templates.TemplateResponse("login.html", {"request": request, "error": "Credenciais inválidas"})
        
        # Cria o token JWT
        token = criar_token(email)  # Passa o email diretamente
        
        # Redireciona para o dashboard com o token como cookie
        res = RedirectResponse("/dashboard", status_code=302)
        res.set_cookie("token", token, httponly=True, secure=True)  # Certifique-se de usar HTTPS em produção
        return res
