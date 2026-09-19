from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.esquadrao_schema import (
    EsquadraoCreate,
    EsquadraoResponse,
    EsquadraoUpdate,
)
from app.services import esquadrao_service

router = APIRouter(prefix="/esquadroes", tags=["Esquadrões"])


@router.get("/", response_model=list[EsquadraoResponse])
def listar_esquadroes(db: Session = Depends(get_db)):
    return esquadrao_service.get_esquadroes(db)


@router.get("/{esquadrao_id}", response_model=EsquadraoResponse)
def buscar_esquadrao_por_id(esquadrao_id: int, db: Session = Depends(get_db)):
    db_esquadrao = esquadrao_service.get_esquadrao_by_id(db, esquadrao_id)
    if not db_esquadrao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esquadrão não encontrado.",
        )
    return db_esquadrao


@router.post(
    "/",
    response_model=EsquadraoResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_esquadrao(
    esquadrao: EsquadraoCreate, db: Session = Depends(get_db)
):
    return esquadrao_service.create_esquadrao(db, esquadrao)


@router.put("/{esquadrao_id}", response_model=EsquadraoResponse)
def atualizar_esquadrao(
    esquadrao_id: int,
    esquadrao: EsquadraoUpdate,
    db: Session = Depends(get_db),
):
    db_esquadrao = esquadrao_service.update_esquadrao(
        db, esquadrao_id, esquadrao
    )
    if not db_esquadrao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esquadrão não encontrado.",
        )
    return db_esquadrao


@router.delete("/{esquadrao_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_esquadrao(esquadrao_id: int, db: Session = Depends(get_db)):
    db_esquadrao = esquadrao_service.delete_esquadrao(db, esquadrao_id)
    if not db_esquadrao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esquadrão não encontrado.",
        )
    return None