from sqlalchemy.orm import Session
from models.paciente import Paciente

# -----------------------------
# Helpers
# -----------------------------

def _get_or_none(db: Session, id_paciente: int):
    return db.query(Paciente).filter(Paciente.id_paciente == id_paciente).first()

# -----------------------------
# Services
# -----------------------------

def obtener_pacientes(db: Session):
    return db.query(Paciente).all()

def obtener_paciente_por_id(db: Session, id_paciente: int):
    return _get_or_none(db, id_paciente)

def buscar_paciente_por_nombre(db: Session, nombre: str):
    return db.query(Paciente).filter(
        Paciente.nombre.ilike(f"%{nombre}%")
    ).all()