# Esre arquivo é responsável por iniciar o FastAPI e juntar todas as rotas, além de criar as tabelas no banco de dados caso ainda não existam.


from fastapi import FastAPI
from app.database import Base, engine
from app.routers import esquadrao_router, patente_router, stormtrooper_router

# Cria as tabelas no banco de dados caso ainda não existam
Base.metadata.create_all(bind=engine)

# Instância da aplicação FastAPI com título e descrição para a documentação Swagger
app = FastAPI(
    title="Trooper API",
    description="API para gerenciamento de Stormtroopers do Império Galáctico",
    version="1.0.0",
)

# Registro das rotas (routers)
app.include_router(patente_router.router)
app.include_router(esquadrao_router.router)
app.include_router(stormtrooper_router.router)


# Rota raiz opcional para testar se a API está online
@app.get("/", tags=["Root"])
def root():
    return {
        "mensagem": "Serviço operacional! Que a Força esteja com você.",
        "docs": "/docs",
    }

# uvicorn app.main:app --reload