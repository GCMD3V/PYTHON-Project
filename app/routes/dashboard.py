from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from jose import JWTError
from app.auth import decodificar_token

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    # Tenta pegar o token do cookie
    token = request.cookies.get("token")
    
    # Se não tiver token, redireciona para login
    if not token:
        return RedirectResponse("/login")
    
    try:
        # Tenta decodificar o token para pegar as informações do usuário
        dados = decodificar_token(token)
    except JWTError:
        # Se o token for inválido, redireciona para login
        return RedirectResponse("/login")
    
    # Se tudo estiver certo, retorna a página de dashboard com os dados do usuário
    return templates.TemplateResponse("dashboard.html", {"request": request, "email": dados["sub"]})
