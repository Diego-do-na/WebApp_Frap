from sqlalchemy import Column, Integer, String
from databases.connection import Base

class ReporteLesion(Base):
    __tablename__ = "reporte_lesion"
    
    reporte_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    lesion_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)