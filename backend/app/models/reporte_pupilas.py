from sqlalchemy import Column, Integer, String
from databases.connection import Base

class ReportePupilas(Base):
    __tablename__ = "reporte_pupilas"
    
    paciente_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    pupilas_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)