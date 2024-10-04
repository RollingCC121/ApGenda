from pydantic import BaseModel

class Materias(BaseModel):
    nombre: str
    codigo: str
    creditos: int
    semestre_id: int
