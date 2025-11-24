# app/schemas/paciente.py
from pydantic import BaseModel
from typing import Optional

# ---------- PACIENTE ----------
class PacienteBase(BaseModel):
    nombre: str
    edad: int
    genero: str

class PacienteCreate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id_Paciente: int

    class Config:
        orm_mode = True


# ---------- PACIENTE - ALERGIA ----------
class PacienteAlergiaBase(BaseModel):
    id_Paciente: int
    id_Alergia: int

class PacienteAlergiaCreate(PacienteAlergiaBase):
    pass

class PacienteAlergiaResponse(PacienteAlergiaBase):
    id: int
    class Config:
        orm_mode = True


# ---------- PACIENTE - MEDICAMENTO ----------
class PacienteMedicamentoBase(BaseModel):
    id_Paciente: int
    id_Medicamento: int

class PacienteMedicamentoCreate(PacienteMedicamentoBase):
    pass

class PacienteMedicamentoResponse(PacienteMedicamentoBase):
    id: int
    class Config:
        orm_mode = True


# ---------- PACIENTE - PATOLOGÍA ----------
class PacientePatologiaBase(BaseModel):
    id_Paciente: int
    id_Patologia: int

class PacientePatologiaCreate(PacientePatologiaBase):
    pass

class PacientePatologiaResponse(PacientePatologiaBase):
    id: int
    class Config:
        orm_mode = True