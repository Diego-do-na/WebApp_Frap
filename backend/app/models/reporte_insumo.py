from sqlalchemy import Column, Integer, String
from databases.connection import Base

class ReporteInsumo(Base):
    __tablename__ = "reporte_insumo"
    
    reporte_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    insumo_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)