# app/schemas/insumos_medicamentos.py
from pydantic import BaseModel

# ---------- INSUMO ----------
class InsumoBase(BaseModel):
    nombre: str

class InsumoCreate(InsumoBase):
    pass

class InsumoResponse(InsumoBase):
    id_Insumo: int
    class Config:
        orm_mode = True


# ---------- MEDICAMENTO ----------
class MedicamentoBase(BaseModel):
    nombre: str

class MedicamentoCreate(MedicamentoBase):
    pass

class MedicamentoResponse(MedicamentoBase):
    id_Medicamento: int
    class Config:
        orm_mode = True