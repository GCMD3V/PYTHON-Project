from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = "postgresql://fastapi:senha123@postgres:5432/meu_banco"
    SECRET_KEY: str = "segredo_super_secreto"
    ALGORITHM: str = "HS256"
    TOKEN_EXP_MINUTES: int = 30

settings = Settings()