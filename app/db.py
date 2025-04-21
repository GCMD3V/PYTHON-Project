from sqlmodel import SQLModel, create_engine # É UMA ORM (ORM = Object Relational Mapping) que permite trabalhar com bancos de dados relacionais
from app.config import settings

engine = create_engine(settings.DB_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine) # Cria todas as tabelas no banco de dados com base nos modelos definidos
    # SQLModel.metadata.drop_all(engine) # Descomente esta linha para apagar todas as tabelas do banco de dados, conforme o arquivo models.py