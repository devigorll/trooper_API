from pydantic import BaseModel


# Base comum para compartilhamento de atributos
class PatenteBase(BaseModel):
    nome: str
    hierarquia_nivel: int


# Utilizado para criar uma nova Patente (recebido via POST)
class PatenteCreate(PatenteBase):
    pass


# Utilizado para atualizar uma Patente (recebido via PUT)
class PatenteUpdate(PatenteBase):
    nome: str | None = None
    hierarquia_nivel: int | None = None


# Utilizado como resposta da API (Response)
class PatenteResponse(PatenteBase):
    id: int

    class Config:
        from_attributes = (
            True  # Permite conversão automática de objetos SQLAlchemy
        )