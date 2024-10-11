from fastapi import FastAPI, Response
from fastapi import HTTPException
from modelo.models import Usuarios, Semestres, Materias
from servicio.validar_usuario import validar_usuario
from servicio.crear_usuario import crear_usuario
from fastapi.middleware.cors import CORSMiddleware

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
@app.post("/api/login")
def login(usuario: Usuarios):
    success, message = validar_usuario(usuario.correo, usuario.password)
    
    if not success:
        raise HTTPException(status_code=400, detail=message)
    
    return {"message": message}


# Endpoint para registrar un nuevo usuario
@app.post("/api/register")
def registrar_usuario(usuario_data: Usuarios):
    correo = usuario_data.correo
    password = usuario_data.password

    try:
        crear_usuario(correo, password)
        return {"message": "Usuario registrado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

''' 
#ruta para las crud de autobus
@app.post("/api")
def insert (User_data:Usuarios):
    data = User_data
    print(data)
    create(data)

# Crear un nuevo semestre
@app.post("/semestres/")
def crear_semestre(data: Semestres, usuario_id: int):
    query = "INSERT INTO semestres (numero, usuario_id) VALUES (%s, %s)"
    db.execute_query(query, (data.numero, usuario_id))
    return {"message": "Semestre creado correctamente"}

@app.post("/materias/")
def agregar_materia(data: Materias, usuario_id: int):
    # Verificar que el semestre pertenece al usuario
    query_semestre = "SELECT id FROM semestres WHERE id = %s AND usuario_id = %s"
    result = db.fetch_query(query_semestre, (data.semestre_id, usuario_id))

    if not result:
        raise HTTPException(status_code=404, detail="Semestre no encontrado o no pertenece al usuario.")

    # Insertar materia
    query_materia = """
        INSERT INTO materias (nombre, codigo, creditos, semestre_id) 
        VALUES (%s, %s, %s, %s)
    """
    db.execute_query(query_materia, (data.nombre, data.codigo, data.creditos, data.semestre_id))
    
    return {"message": "Materia agregada correctamente"}
    '''