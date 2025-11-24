from sqlalchemy import Column, Integer, String, LargeBinary
from databases.connection import Base

class Paramedico(Base):
    __tablename__ = "paramedico"
    
    id_paramedico = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    nombre = Column(String(50),index = True, nullable=False)
    correoInst = Column(String(50), unique = True, nullable = False, index = True)
    correoEsc = Column(String(50), nullable = False, index = True)   
    usuario = Column(String(50), unique = True, nullable = False, index = True)
    contraseña = Column(String(100), nullable = False, index = True)
    firma_paramedico = Column(LargeBinary, nullable=False, index=True)