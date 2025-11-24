from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, ForeignKey, Text, SmallInteger
from databases.connection import Base

class Reporte(Base):
    __tablename__ = "reporte"
    
    id_Reporte = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fecha_hora = Column(DateTime, nullable = False, index=True)
    observaciones = Column(Text, nullable = False, index = True)
    recomendaciones = Column(Text, nullable = False, index = True)
    translado_aceptado = Column(SmallInteger, nullable = False, index = True)
    numero_unidad = Column(String(50), nullable = False, index = True)
    nombre_operador = Column(String(50), nullable = True, index = True)
    firma_operador = Column(LargeBinary, nullable = True, index = True)
    firma_paciente = Column(LargeBinary, nullable = False, index = True)
    nombre_testigo = Column(String(50), nullable = True, index = True)
    firma_testigo = Column(LargeBinary, nullable = True, index = True)
    lugar_id = Column(Integer, ForeignKey("lugar.id_Lugar"), nullable = False, index = True)
    signos_id = Column(Integer, ForeignKey("signos_vitales.id_Signos"), nullable = False, index = True)
    nivel_conciencia_id = Column(Integer, ForeignKey("nivel_conciencia.id_Nivel_Conciencia"), nullable = False, index = True)