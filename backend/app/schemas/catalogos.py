# app/schemas/catalogos.py
from pydantic import BaseModel

# ---------- ALERGIA ----------
class AlergiaBase(BaseModel):
    nombre: str

class AlergiaCreate(AlergiaBase):
    pass

class AlergiaResponse(AlergiaBase):
    id_Alergia: int
    class Config:
        orm_mode = True


# ---------- PATOLOGÍA ----------
class PatologiaBase(BaseModel):
    nombre: str

class PatologiaCreate(PatologiaBase):
    pass

class PatologiaResponse(PatologiaBase):
    id_Patologia: int
    class Config:
        orm_mode = True


# ---------- PUPILAS ----------
class PupilasBase(BaseModel):
    tipo: str

class PupilasCreate(PupilasBase):
    pass

class PupilasResponse(PupilasBase):
    id_Pupilas: int
    class Config:
        orm_mode = True


# ---------- NIVEL DE CONCIENCIA ----------
class NivelConcienciaBase(BaseModel):
    estado: str

class NivelConcienciaCreate(NivelConcienciaBase):
    pass

class NivelConcienciaResponse(NivelConcienciaBase):
    id_NivelConciencia: int
    class Config:
        orm_mode = True


# ---------- ANATÓMICA ----------
class AnatomicaBase(BaseModel):
    zona: str

class AnatomicaCreate(AnatomicaBase):
    pass

class AnatomicaResponse(AnatomicaBase):
    id_Anatomica: int
    class Config:
        orm_mode = True


# ---------- LUGAR ----------
class LugarBase(BaseModel):
    nombre: str

class LugarCreate(LugarBase):
    pass

class LugarResponse(LugarBase):
    id_Lugar: int
    class Config:
        orm_mode = True