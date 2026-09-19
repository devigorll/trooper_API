from pydantic import BaseModel
from app.schemas.esquadrao_schema import EsquadraoResponse
from app.schemas.patente_schema import PatenteResponse


# Atributos base compartilhados
class StormtrooperBase(BaseModel):
    identificacao: str
    precisao_tiro_pct: float
    batimento_cardiaco_bpm: int
    status_servico: str = "Ativo"


# Schema para recepção de criação (POST)
class StormtrooperCreate(StormtrooperBase):
    patente_id: int
    esquadrao_id: int


# Schema para atualização parcial/total (PUT/PATCH)
class StormtrooperUpdate(BaseModel):
    identificacao: str | None = None
    patente_id: int | None = None
    esquadrao_id: int | None = None
    precisao_tiro_pct: float | None = None
    batimento_cardiaco_bpm: int | None = None
    status_servico: str | None = None


# Schema para resposta da API (GET)
class StormtrooperResponse(StormtrooperBase):
    id: int
    patente_id: int
    esquadrao_id: int

    # traz também os detalhes completos das tabelas relacionadas
    patente: PatenteResponse
    esquadrao: EsquadraoResponse

    class Config:
        from_attributes = True