from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.patente_schema import (
    PatenteCreate,
    PatenteResponse,
    PatenteUpdate,
)
from app.services import patente_service

router = APIRouter(prefix="/patentes", tags=["Patentes"])


@router.get("/", response_model=list[PatenteResponse])
def listar_patentes(db: Session = Depends(get_db)):
    return patente_service.get_patentes(db)


@router.get("/{patente_id}", response_model=PatenteResponse)
def buscar_patente_por_id(patente_id: int, db: Session = Depends(get_db)):
    db_patente = patente_service.get_patente_by_id(db, patente_id)
    if not db_patente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patente não encontrada.",
        )
    return db_patente


@router.post(
    "/",
    response_model=PatenteResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_patente(patente: PatenteCreate, db: Session = Depends(get_db)):
    return patente_service.create_patente(db, patente)


@router.put("/{patente_id}", response_model=PatenteResponse)
def atualizar_patente(
    patente_id: int,
    patente: PatenteUpdate,
    db: Session = Depends(get_db),
):
    db_patente = patente_service.update_patente(db, patente_id, patente)
    if not db_patente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patente não encontrada.",
        )
    return db_patente


@router.delete("/{patente_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_patente(patente_id: int, db: Session = Depends(get_db)):
    db_patente = patente_service.delete_patente(db, patente_id)
    if not db_patente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patente não encontrada.",
        )
    return None