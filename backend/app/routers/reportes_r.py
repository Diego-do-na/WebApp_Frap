from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases.connection import get_db

from models.reporte import Reporte
from models.reporte_anatomica import ReporteAnatomica
from models.reporte_insumo import ReporteInsumo
from models.reporte_lesion import ReporteLesion
from models.reporte_pupilas import ReportePupilas

router = APIRouter(prefix="/reportes", tags=["Reportes"])

# ---------------------------
#   CRUD REPORTES
# ---------------------------
@router.get("/")
def obtener_reportes(db: Session = Depends(get_db)):
    return db.query(Reporte).all()

@router.get("/{id_reporte}")
def obtener_reporte(id_reporte: int, db: Session = Depends(get_db)):
    r = db.query(Reporte).filter(Reporte.id_reporte == id_reporte).first()
    if not r:
        raise HTTPException(404, "Reporte no encontrado")
    return r

@router.post("/")
def crear_reporte(data: dict, db: Session = Depends(get_db)):
    r = Reporte(**data)
    db.add(r)
    db.commit()
    db.refresh(r)
    return r

@router.put("/{id_reporte}")
def actualizar_reporte(id_reporte: int, data: dict, db: Session = Depends(get_db)):
    r = db.query(Reporte).filter(Reporte.id_reporte == id_reporte).first()
    if not r:
        raise HTTPException(404, "Reporte no encontrado")

    for k, v in data.items():
        setattr(r, k, v)

    db.commit()
    db.refresh(r)
    return r

@router.delete("/{id_reporte}")
def eliminar_reporte(id_reporte: int, db: Session = Depends(get_db)):
    r = db.query(Reporte).filter(Reporte.id_reporte == id_reporte).first()
    if not r:
        raise HTTPException(404, "Reporte no encontrado")

    db.delete(r)
    db.commit()
    return {"mensaje": "Reporte eliminado"}

# ---------------------------
#   ANATÓMICA
# ---------------------------
@router.get("/{id_reporte}/anatomica")
def obtener_anatomica(id_reporte: int, db: Session = Depends(get_db)):
    return db.query(ReporteAnatomica).filter(
        ReporteAnatomica.id_reporte == id_reporte
    ).all()

@router.post("/{id_reporte}/anatomica")
def agregar_anatomica(id_reporte: int, data: dict, db: Session = Depends(get_db)):
    data["id_reporte"] = id_reporte
    a = ReporteAnatomica(**data)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a

# ---------------------------
#   INSUMOS
# ---------------------------
@router.get("/{id_reporte}/insumos")
def obtener_insumos(id_reporte: int, db: Session = Depends(get_db)):
    return db.query(ReporteInsumo).filter(
        ReporteInsumo.id_reporte == id_reporte
    ).all()

@router.post("/{id_reporte}/insumos")
def agregar_insumo(id_reporte: int, data: dict, db: Session = Depends(get_db)):
    data["id_reporte"] = id_reporte
    ins = ReporteInsumo(**data)
    db.add(ins)
    db.commit()
    db.refresh(ins)
    return ins

# ---------------------------
#   LESIONES
# ---------------------------
@router.get("/{id_reporte}/lesiones")
def obtener_lesiones(id_reporte: int, db: Session = Depends(get_db)):
    return db.query(ReporteLesion).filter(
        ReporteLesion.id_reporte == id_reporte
    ).all()

@router.post("/{id_reporte}/lesiones")
def agregar_lesion(id_reporte: int, data: dict, db: Session = Depends(get_db)):
    data["id_reporte"] = id_reporte
    l = ReporteLesion(**data)
    db.add(l)
    db.commit()
    db.refresh(l)
    return l

# ---------------------------
#   PUPILAS
# ---------------------------
@router.get("/{id_reporte}/pupilas")
def obtener_pupilas(id_reporte: int, db: Session = Depends(get_db)):
    return db.query(ReportePupilas).filter(
        ReportePupilas.id_reporte == id_reporte
    ).all()

@router.post("/{id_reporte}/pupilas")
def agregar_pupilas(id_reporte: int, data: dict, db: Session = Depends(get_db)):
    data["id_reporte"] = id_reporte
    p = ReportePupilas(**data)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p