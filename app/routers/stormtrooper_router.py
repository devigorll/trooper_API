from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.stormtrooper_schema import (
    StormtrooperCreate,
    StormtrooperResponse,
    StormtrooperUpdate,
)
from app.services import (
    esquadrao_service,
    patente_service,
    stormtrooper_service,
)

router = APIRouter(prefix="/stormtroopers", tags=["Stormtroopers"])


@router.get("/", response_model=list[StormtrooperResponse])
def listar_stormtroopers(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return stormtrooper_service.get_stormtroopers(
        db, skip=skip, limit=limit
    )


@router.get("/{trooper_id}", response_model=StormtrooperResponse)
def buscar_stormtrooper_por_id(trooper_id: int, db: Session = Depends(get_db)):
    db_trooper = stormtrooper_service.get_stormtrooper_by_id(db, trooper_id)
    if not db_trooper:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stormtrooper não encontrado.",
        )
    return db_trooper


@router.post(
    "/",
    response_model=StormtrooperResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_stormtrooper(
    trooper: StormtrooperCreate, db: Session = Depends(get_db)
):
    # Validar se a identificação (ex: TK-421) já existe
    db_trooper_existente = (
        stormtrooper_service.get_stormtrooper_by_identificacao(
            db, trooper.identificacao
        )
    )
    if db_trooper_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Identificação '{trooper.identificacao}' já cadastrada.",
        )

    # Validar se a patente_id existe
    if not patente_service.get_patente_by_id(db, trooper.patente_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patente informada não existe.",
        )

    # Validar se o esquadrao_id existe
    if not esquadrao_service.get_esquadrao_by_id(db, trooper.esquadrao_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esquadrão informado não existe.",
        )

    return stormtrooper_service.create_stormtrooper(db, trooper)


@router.put("/{trooper_id}", response_model=StormtrooperResponse)
def atualizar_stormtrooper(
    trooper_id: int,
    trooper: StormtrooperUpdate,
    db: Session = Depends(get_db),
):
    db_trooper = stormtrooper_service.update_stormtrooper(
        db, trooper_id, trooper
    )
    if not db_trooper:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stormtrooper não encontrado.",
        )
    return db_trooper


@router.delete("/{trooper_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_stormtrooper(trooper_id: int, db: Session = Depends(get_db)):
    db_trooper = stormtrooper_service.delete_stormtrooper(db, trooper_id)
    if not db_trooper:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stormtrooper não encontrado.",
        )
    return None