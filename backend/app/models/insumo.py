from sqlalchemy import Column, Integer, String
from databases.connection import Base

class Insumo(Base):
    __tablename__ = "insumo"
    
    id_Insumo = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre = Column(String(50), index = True, nullable=False)
    cantidad = Column(Integer, nullable=False)