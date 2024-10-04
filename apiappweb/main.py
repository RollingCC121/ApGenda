from fastapi import FastAPI, Response
from fastapi import HTTPException
from modelo.usuarios_model import Usuarios
from modelo.materias_model import Materias
from modelo.semestres_model import Semestres
from servicio.validar_usuario import validar_usuario
from fastapi.middleware.cors import CORSMiddleware
from your_database import get_db, Usuario, Semestre, Materia  # Asegúrate de tener esto configurado



# Crear la aplicación FastAPI
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen. Puedes especificar solo el dominio de tu frontend.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Permite todos los headers
)


# Endpoint para el login
@app.post("/login")
def login(usuario: Usuarios):
    success, message = validar_usuario(usuario.correo, usuario.password)
    
    if not success:
        raise HTTPException(status_code=400, detail=message)
    
    return {"message": message}


@app.post("/semestres/")
def crear_semestre(semestre: Semestres, db: Session = Depends(get_db), usuario_id: int = Depends(get_current_user)):
    nuevo_semestre = Semestre(numero=semestre.numero, usuario_id=usuario_id)
    db.add(nuevo_semestre)
    db.commit()
    db.refresh(nuevo_semestre)
    return nuevo_semestre

# Agregar materias a un semestre
@app.post("/materias/")
def agregar_materia(materia: Materias, db: Session = Depends(get_db), usuario_id: int = Depends(get_current_user)):
    semestre = db.query(Semestre).filter(Semestre.id == materia.semestre_id, Semestre.usuario_id == usuario_id).first()
    if not semestre:
        raise HTTPException(status_code=404, detail="Semestre no encontrado o no pertenece al usuario.")
    
    nueva_materia = Materia(
        nombre=materia.nombre,
        codigo=materia.codigo,
        creditos=materia.creditos,
        semestre_id=materia.semestre_id
    )
    db.add(nueva_materia)
    db.commit()
    db.refresh(nueva_materia)
    return nueva_materia