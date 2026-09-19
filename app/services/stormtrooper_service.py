from sqlalchemy.orm import Session
from app.models import Stormtrooper
from app.schemas.stormtrooper_schema import StormtrooperCreate, StormtrooperUpdate

def get_stormtroopers(db: Session, skip: int = 0, limit: int = 100):
    """Lista os stormtroopers com paginação simples."""
    return db.query(Stormtrooper).offset(skip).limit(limit).all()

def get_stormtrooper_by_id(db: Session, trooper_id: int):
    """Busca um stormtrooper pelo ID."""
    return db.query(Stormtrooper).filter(Stormtrooper.id == trooper_id).first()

def get_stormtrooper_by_identificacao(db: Session, identificacao: str):
    """Busca um stormtrooper pela identificação (Ex: 'TK-421')."""
    return db.query(Stormtrooper).filter(Stormtrooper.identificacao == identificacao).first()

def create_stormtrooper(db: Session, trooper: StormtrooperCreate):
    """Cria um novo stormtrooper."""
    db_trooper = Stormtrooper(
        identificacao=trooper.identificacao,
        patente_id=trooper.patente_id,
        esquadrao_id=trooper.esquadrao_id,
        precisao_tiro_pct=trooper.precisao_tiro_pct,
        batimento_cardiaco_bpm=trooper.batimento_cardiaco_bpm,
        status_servico=trooper.status_servico
    )
    db.add(db_trooper)
    db.commit()
    db.refresh(db_trooper)
    return db_trooper

def update_stormtrooper(db: Session, trooper_id: int, trooper_data: StormtrooperUpdate):
    """Atualiza dados de um stormtrooper."""
    db_trooper = get_stormtrooper_by_id(db, trooper_id)
    if not db_trooper:
        return None
    
    update_data = trooper_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_trooper, key, value)
        
    db.commit()
    db.refresh(db_trooper)
    return db_trooper

def delete_stormtrooper(db: Session, trooper_id: int):
    """Remove um stormtrooper pelo ID."""
    db_trooper = get_stormtrooper_by_id(db, trooper_id)
    if db_trooper:
        db.delete(db_trooper)
        db.commit()
    return db_trooper