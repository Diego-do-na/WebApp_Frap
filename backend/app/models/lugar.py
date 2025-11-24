from sqlalchemy import Column, Integer, String
from databases.connection import Base

class Lugar(Base):
    __tablename__ = "lugar"
    
    id_Lugar = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    nombre = Column(String(50), unique = True, index = True, nullable=False)