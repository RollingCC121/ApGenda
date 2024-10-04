from pydantic import BaseModel


# Modelo de datos para el login
class Usuarios(BaseModel):
    correo: str
    password: str