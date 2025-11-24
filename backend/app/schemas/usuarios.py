# app/schemas/usuarios.py
from pydantic import BaseModel

# ---------- ADMIN ----------
class AdminBase(BaseModel):
    nombre: str
    email: str

class AdminCreate(AdminBase):
    contrasena: str

class AdminResponse(AdminBase):
    id_Admin: int
    class Config:
        orm_mode = True


# ---------- PARAMÉDICO ----------
class ParamedicoBase(BaseModel):
    nombre: str
    email: str

class ParamedicoCreate(ParamedicoBase):
    contrasena: str

class ParamedicoResponse(ParamedicoBase):
    id_Paramedico: int
    class Config:
        orm_mode = True