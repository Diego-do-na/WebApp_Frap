from fastapi import APIRouter
from app.services.catalogos_services import (
    obtener_alergias,
    obtener_patologias,
    obtener_pupilas,
    obtener_nivel_conciencia,
    obtener_anatomica,
    obtener_lugares,
    obtener_signos_vitales
)

router = APIRouter(prefix="/catalogos", tags=["Catálogos"])

@router.get("/alergias")
def get_alergias():
    return obtener_alergias()

@router.get("/patologias")
def get_patologias():
    return obtener_patologias()

@router.get("/pupilas")
def get_pupilas():
    return obtener_pupilas()

@router.get("/nivel_conciencia")
def get_nivel_conciencia():
    return obtener_nivel_conciencia()

@router.get("/anatomica")
def get_anatomica():
    return obtener_anatomica()

@router.get("/lugares")
def get_lugares():
    return obtener_lugares()

@router.get("/signos_vitales")
def get_signos_vitales():
    return obtener_signos_vitales()