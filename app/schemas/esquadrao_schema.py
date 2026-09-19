from pydantic import BaseModel


class EsquadraoBase(BaseModel):
    nome: str
    especialidade: str


class EsquadraoCreate(EsquadraoBase):
    pass                                    # o argumentoo pass serve para indicar que a classe não tem atributos adicionais além dos herdados de EsquadraoBase


class EsquadraoUpdate(EsquadraoBase):
    nome: str | None = None                 # "| None" indica que o atributo é opcional, ou seja, pode ser fornecido ou não na atualização
    especialidade: str | None = None


class EsquadraoResponse(EsquadraoBase):
    id: int

    class Config:
        from_attributes = True             # Permite que o Pydantic crie instâncias de EsquadraoResponse a partir de objetos ORM 
                                           # (como os modelos SQLAlchemy), mapeando automaticamente os atributos do modelo para os campos do schema