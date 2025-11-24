from sqlalchemy.orm import Session
from app.models.reporte import Reporte
from app.models.paciente import Paciente
from sqlalchemy import func

def total_reportes(db: Session):
    return db.query(func.count(Reporte.id_Reporte)).scalar()

def reportes_por_genero(db: Session):
    return db.query(
        Paciente.genero,
        func.count(Reporte.id_Reporte)
    ).join(Reporte, Reporte.id_Paciente == Paciente.id_Paciente
    ).group_by(Paciente.genero).all()

def edades_promedio(db: Session):
    return db.query(
        func.avg(Paciente.edad)
    ).scalar()