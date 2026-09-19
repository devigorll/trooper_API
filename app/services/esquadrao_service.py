from sqlalchemy.orm import Session
from app.models import Esquadrao
from app.schemas.esquadrao_schema import EsquadraoCreate, EsquadraoUpdate

def get_esquadroes(db: Session):
    """Lista todos os esquadrões."""
    return db.query(Esquadrao).all()

def get_esquadrao_by_id(db: Session, esquadrao_id: int):
    """Busca um esquadrão pelo ID."""
    return db.query(Esquadrao).filter(Esquadrao.id == esquadrao_id).first()

def create_esquadrao(db: Session, esquadrao: EsquadraoCreate):
    """Cria um novo esquadrão."""
    db_esquadrao = Esquadrao(
        nome=esquadrao.nome,
        especialidade=esquadrao.especialidade
    )
    db.add(db_esquadrao)
    db.commit()
    db.refresh(db_esquadrao)
    return db_esquadrao

def update_esquadrao(db: Session, esquadrao_id: int, esquadrao_data: EsquadraoUpdate):
    """Atualiza dados de um esquadrão existente."""
    db_esquadrao = get_esquadrao_by_id(db, esquadrao_id)
    if not db_esquadrao:
        return None
    
    update_data = esquadrao_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_esquadrao, key, value)
        
    db.commit()
    db.refresh(db_esquadrao)
    return db_esquadrao

def delete_esquadrao(db: Session, esquadrao_id: int):
    """Remove um esquadrão pelo ID."""
    db_esquadrao = get_esquadrao_by_id(db, esquadrao_id)
    if db_esquadrao:
        db.delete(db_esquadrao)
        db.commit()
    return db_esquadrao