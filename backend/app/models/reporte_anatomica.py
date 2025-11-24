from sqlalchemy import Column, Integer, String
from databases.connection import Base

class ReporteAnatomica(Base):
    __tablename__ = "reporte_anatomica"
    
    reporte_id = Column(Integer, primary_key=True, index=True, nullable=False)
    anatomica_id = Column(Integer, primary_key=True, index=True, nullable=False)