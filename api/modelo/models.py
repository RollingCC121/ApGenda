from pydantic import BaseModel

class Materias(BaseModel):
    nombre: str
    codigo: str
    creditos: int
    semestre_id: int

# Modelo de datos para el login
class Usuarios(BaseModel):
    correo: str
    password: str

class Semestres(BaseModel):
    numero: int