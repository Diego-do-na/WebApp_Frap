from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases.connection import get_db

from models.insumo import Insumo
from models.medicamento import Medicamento

router = APIRouter(prefix="/insumos-medicamentos", tags=["Insumos y Medicamentos"])

# =====================================================
#                    INSUMOS
# =====================================================

@router.get("/insumos")
def obtener_insumos(db: Session = Depends(get_db)):
    return db.query(Insumo).all()

@router.get("/insumos/{id_insumo}")
def obtener_insumo(id_insumo: int, db: Session = Depends(get_db)):
    ins = db.query(Insumo).filter(Insumo.id_insumo == id_insumo).first()
    if not ins:
        raise HTTPException(404, "Insumo no encontrado")
    return ins

@router.post("/insumos")
def crear_insumo(data: dict, db: Session = Depends(get_db)):
    ins = Insumo(**data)
    db.add(ins)
    db.commit()
    db.refresh(ins)
    return ins

@router.put("/insumos/{id_insumo}")
def actualizar_insumo(id_insumo: int, data: dict, db: Session = Depends(get_db)):
    ins = db.query(Insumo).filter(Insumo.id_insumo == id_insumo).first()
    if not ins:
        raise HTTPException(404, "Insumo no encontrado")

    for k, v in data.items():
        setattr(ins, k, v)

    db.commit()
    db.refresh(ins)
    return ins

@router.delete("/insumos/{id_insumo}")
def eliminar_insumo(id_insumo: int, db: Session = Depends(get_db)):
    ins = db.query(Insumo).filter(Insumo.id_insumo == id_insumo).first()
    if not ins:
        raise HTTPException(404, "Insumo no encontrado")

    db.delete(ins)
    db.commit()
    return {"mensaje": "Insumo eliminado"}

# =====================================================
#                    MEDICAMENTOS
# =====================================================

@router.get("/medicamentos")
def obtener_medicamentos(db: Session = Depends(get_db)):
    return db.query(Medicamento).all()

@router.get("/medicamentos/{id_medicamento}")
def obtener_medicamento(id_medicamento: int, db: Session = Depends(get_db)):
    med = db.query(Medicamento).filter(Medicamento.id_medicamento == id_medicamento).first()
    if not med:
        raise HTTPException(404, "Medicamento no encontrado")
    return med

@router.post("/medicamentos")
def crear_medicamento(data: dict, db: Session = Depends(get_db)):
    med = Medicamento(**data)
    db.add(med)
    db.commit()
    db.refresh(med)
    return med

@router.put("/medicamentos/{id_medicamento}")
def actualizar_medicamento(id_medicamento: int, data: dict, db: Session = Depends(get_db)):
    med = db.query(Medicamento).filter(Medicamento.id_medicamento == id_medicamento).first()
    if not med:
        raise HTTPException(404, "Medicamento no encontrado")

    for k, v in data.items():
        setattr(med, k, v)

    db.commit()
    db.refresh(med)
    return med

@router.delete("/medicamentos/{id_medicamento}")
def eliminar_medicamento(id_medicamento: int, db: Session = Depends(get_db)):
    med = db.query(Medicamento).filter(Medicamento.id_medicamento == id_medicamento).first()
    if not med:
        raise HTTPException(404, "Medicamento no encontrado")

    db.delete(med)
    db.commit()
    return {"mensaje": "Medicamento eliminado"}