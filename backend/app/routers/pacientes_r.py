from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.databases.connection import get_db
from app.schemas.pacientes import PacienteResponse
from app.services.pacientes_services import (
    obtener_pacientes,
    obtener_paciente_por_id,
    buscar_paciente_por_nombre
)

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

@router.get("/", response_model=list[PacienteResponse])
def listar_pacientes(db: Session = Depends(get_db)):
    return obtener_pacientes(db)

@router.get("/{id_paciente}", response_model=PacienteResponse)
def obtener_paciente(id_paciente: int, db: Session = Depends(get_db)):
    paciente = obtener_paciente_por_id(db, id_paciente)
    if not paciente:
        raise HTTPException(404, "Paciente no encontrado")
    return paciente

@router.get("/buscar/nombre", response_model=list[PacienteResponse])
def buscar_paciente(nombre: str, db: Session = Depends(get_db)):
    resultados = buscar_paciente_por_nombre(db, nombre)
    if not resultados:
        raise HTTPException(404, "No se encontraron pacientes")
    return resultados