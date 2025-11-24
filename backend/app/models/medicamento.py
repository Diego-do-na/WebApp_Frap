from sqlalchemy import Column, Integer, String
from databases.connection import Base

class Medicamento(Base):
    __tablename__ = "medicamento"
    
    id_Medicamento = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    nombre = Column(String(100), unique = True, index = True, nullable=False)