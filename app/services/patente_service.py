from sqlalchemy.orm import Session
from app.models import Patente
from app.schemas.patente_schema import PatenteCreate, PatenteUpdate

def get_patentes(db: Session):
    """Lista todas as patentes."""
    return db.query(Patente).all()

def get_patente_by_id(db: Session, patente_id: int):
    """Busca uma patente pelo ID."""
    return db.query(Patente).filter(Patente.id == patente_id).first()

def create_patente(db: Session, patente: PatenteCreate):
    """Cria uma nova patente."""
    db_patente = Patente(
        nome=patente.nome,
        hierarquia_nivel=patente.hierarquia_nivel
    )
    db.add(db_patente)
    db.commit()
    db.refresh(db_patente)
    return db_patente

def update_patente(db: Session, patente_id: int, patente_data: PatenteUpdate):
    """Atualiza os dados de uma patente existente."""
    db_patente = get_patente_by_id(db, patente_id)
    if not db_patente:
        return None
    
    update_data = patente_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_patente, key, value)
        
    db.commit()
    db.refresh(db_patente)
    return db_patente

def delete_patente(db: Session, patente_id: int):
    """Remove uma patente pelo ID."""
    db_patente = get_patente_by_id(db, patente_id)
    if db_patente:
        db.delete(db_patente)
        db.commit()
    return db_patente