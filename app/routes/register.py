from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from app.db import engine
from app.models import Usuario
from app.auth import hash_senha, criar_token  # Certifique-se de ter a função criar_token

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
def register(email: str = Form(...), senha: str = Form(...), response: Response):
    # Cria o usuário
    with Session(engine) as session:
        usuario = Usuario(email=email, senha=hash_senha(senha))
        session.add(usuario)
        session.commit()
    
    # Cria o token para o usuário
    token = criar_token(email)  # Gera o token (necessário criar a função criar_token)

    # Define o token no cookie para autenticação
    response.set_cookie(key="token", value=token, httponly=True, secure=True)  # Certifique-se de usar HTTPS em produção

    return RedirectResponse("/dashboard", status_code=302)
