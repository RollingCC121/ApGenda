from conexion import Connection
from fastapi import HTTPException

# Función para crear un nuevo usuario en la base de datos
def crear_usuario(correo: str, password: str):
    connection = Connection()
    cursor = connection.conn.cursor()
    
    try:
        # Verificar si el usuario ya está registrado
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        usuario_existente = cursor.fetchone()
        
        if usuario_existente:
            raise HTTPException(status_code=400, detail="El usuario ya está registrado")
        
        # Insertar el nuevo usuario
        cursor.execute("INSERT INTO usuarios (correo, password) VALUES (%s, %s)", (correo, password))
        connection.conn.commit()
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        connection.conn.rollback()
        raise Exception(f"Error al crear el usuario: {str(e)}")
    finally:
        cursor.close()
        del connection