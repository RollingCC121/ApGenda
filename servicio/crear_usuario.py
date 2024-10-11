from conexion import Connection
from fastapi import HTTPException

# Función para crear un nuevo usuario en la base de datos
def crear_usuario(correo: str, password: str):
    connection = Connection()
    cursor = connection.conn.cursor()
    
    try:
        cursor.execute("INSERT INTO usuarios (correo, password) VALUES (%s, %s)", (correo, password))
        connection.conn.commit()
    except Exception as e:
        connection.conn.rollback()
        raise Exception(f"Error al crear el usuario: {str(e)}")
    finally:
        cursor.close()
        del connection