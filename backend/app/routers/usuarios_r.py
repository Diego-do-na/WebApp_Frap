from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases.connection import get_db

from models.admin import Admin
from models.paramedico import Paramedico

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# ---------------------------
#           ADMINS
# ---------------------------
@router.get("/admins")
def obtener_admins(db: Session = Depends(get_db)):
    return db.query(Admin).all()

@router.get("/admins/{id_admin}")
def obtener_admin(id_admin: int, db: Session = Depends(get_db)):
    adm = db.query(Admin).filter(Admin.id_admin == id_admin).first()
    if not adm:
        raise HTTPException(404, "Admin no encontrado")
    return adm

@router.post("/admins")
def crear_admin(data: dict, db: Session = Depends(get_db)):
    adm = Admin(**data)
    db.add(adm)
    db.commit()
    db.refresh(adm)
    return adm

@router.put("/admins/{id_admin}")
def actualizar_admin(id_admin: int, data: dict, db: Session = Depends(get_db)):
    adm = db.query(Admin).filter(Admin.id_admin == id_admin).first()
    if not adm:
        raise HTTPException(404, "Admin no encontrado")

    for k, v in data.items():
        setattr(adm, k, v)

    db.commit()
    db.refresh(adm)
    return adm

@router.delete("/admins/{id_admin}")
def eliminar_admin(id_admin: int, db: Session = Depends(get_db)):
    adm = db.query(Admin).filter(Admin.id_admin == id_admin).first()
    if not adm:
        raise HTTPException(404, "Admin no encontrado")

    db.delete(adm)
    db.commit()
    return {"mensaje": "Admin eliminado"}

# ---------------------------
#        PARAMÉDICOS
# ---------------------------
@router.get("/paramedicos")
def obtener_paramedicos(db: Session = Depends(get_db)):
    return db.query(Paramedico).all()

@router.get("/paramedicos/{id_paramedico}")
def obtener_paramedico(id_paramedico: int, db: Session = Depends(get_db)):
    p = db.query(Paramedico).filter(Paramedico.id_paramedico == id_paramedico).first()
    if not p:
        raise HTTPException(404, "Paramédico no encontrado")
    return p

@router.post("/paramedicos")
def crear_paramedico(data: dict, db: Session = Depends(get_db)):
    p = Paramedico(**data)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

@router.put("/paramedicos/{id_paramedico}")
def actualizar_paramedico(id_paramedico: int, data: dict, db: Session = Depends(get_db)):
    p = db.query(Paramedico).filter(Paramedico.id_paramedico == id_paramedico).first()
    if not p:
        raise HTTPException(404, "Paramédico no encontrado")

    for k, v in data.items():
        setattr(p, k, v)

    db.commit()
    db.refresh(p)
    return p

@router.delete("/paramedicos/{id_paramedico}")
def eliminar_paramedico(id_paramedico: int, db: Session = Depends(get_db)):
    p = db.query(Paramedico).filter(Paramedico.id_paramedico == id_paramedico).first()
    if not p:
        raise HTTPException(404, "Paramédico no encontrado")

    db.delete(p)
    db.commit()
    return {"mensaje": "Paramédico eliminado"}