# Este arquivo define oos modeloos de tabelas que serão usados pelo SQLALchemy para interagir com oos bancoos de dados.


from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Importamos a Base que você configurou no database.py
from app.database import Base


# 1. MODELO DE PATENTES
class Patente(Base):
    __tablename__ = "patentes_tb"

    id = Column(Integer, primary_primary_key=True, primary_key=True, index=True)
    nome = Column(String(30), nullable=False, unique=True)
    hierarquia_nivel = Column(Integer, nullable=False)

    # Relacionamento de volta para os Stormtroopers
    stormtroopers = relationship("Stormtrooper", back_populates="patente")


# 2. MODELO DE ESQUADRÕES
class Esquadrao(Base):
    __tablename__ = "esquadroes_tb"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False, unique=True)
    especialidade = Column(String(50), nullable=False)

    # Relacionamento de volta para os Stormtroopers
    stormtroopers = relationship("Stormtrooper", back_populates="esquadrao")


# 3. MODELO PRINCIPAL DE STORMTROOPERS
class Stormtrooper(Base):
    __tablename__ = "stormtroopers_tb"

    id = Column(Integer, primary_key=True, index=True)
    identificacao = Column(String(20), nullable=False, unique=True)
    
    patente_id = Column(
        Integer, ForeignKey("patentes_tb.id"), nullable=False
    )

    esquadrao_id = Column(
        Integer, ForeignKey("esquadroes_tb.id"), nullable=False
    )

    precisao_tiro_pct = Column(Float, nullable=False)
    batimento_cardiaco_bpm = Column(Integer, nullable=False)
    status_servico = Column(String(20), default="Ativo")

    # Mapeamento dos relacionamentos com as tabelas pai
    patente = relationship("Patente", back_populates="stormtroopers")
    esquadrao = relationship("Esquadrao", back_populates="stormtroopers")