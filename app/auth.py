from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)

def criar_token(data: dict):
    expira = datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXP_MINUTES)
    data.update({"exp": expira})
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decodificar_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
