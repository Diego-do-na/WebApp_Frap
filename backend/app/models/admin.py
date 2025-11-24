from sqlalchemy import Column, Integer, String
from databases.connection import Base

class Admin(Base):
    __tablename__ = "admin"
    
    id_admin = Column(Integer, primary_key=True, index=True, nullable=False)
    usuario = Column(String(50), unique=True, index=True, nullable=False)
    contraseña = Column(String(100), nullable=False)
    correo = Column(String(50), unique=True, index=True, nullable=False)