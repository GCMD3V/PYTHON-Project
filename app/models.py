from sqlmodel import SQLModel, Field
from typing import Optional

class Usuario(SQLModel, table=True): # cada classe representa uma tabela no banco de dados
    # __tablename__ = "usuarios"  # Nome da tabela no banco de dados
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    senha: str
# para delimitar a quantidade de caracteres, use o Field com max_length
#     # Exemplo: senha: str = Field(max_length=100)
    # Outros campos podem ser adicionados conforme necessário
    #as outras formas de definir o nome da tabela são:
    # __tablename__ = "usuarios"  # Nome da tabela no banco de dados
    # __table_args__ = {"extend_existing": True}  # Permite sobrescrever a tabela existente, se necessário
    # __table_args__ = {"schema": "esquema"}  # Define o esquema do banco de dados
    # Field(default=None, primary_key=True)  # Define o campo como chave primária
    # Field(default=None, foreign_key="outra_tabela.id")  # Define uma chave estrangeira
    # Field(default=None, index=True)  # Define um index
    # Field(default=None, unique=True)  # Define um campo único
    # Field(default=None, nullable=False)  # Define um campo não nulo
    # Field(default=None, default_factory=uuid.uuid4)  # Define um campo com valor padrão gerado por uma função
    # Field(default=None, default="valor_padrao")  # Define um campo com valor padrão fixo
    # Field(default=None, sa_column_kwargs={"server_default": "valor_padrao"})  # Define um campo com valor padrão no banco de dados
#     # Outros campos podem ser adicionados conforme necessário

