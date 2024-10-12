from conexion import Connection


# Función para validar el login
def validar_usuario(correo: str, password: str):
    conn = Connection()  # Instanciar la clase de conexión
    try:
        # Ejecutar consulta para verificar si el usuario existe y si la contraseña es correcta
        conn.cur.execute(
            "SELECT password FROM usuarios WHERE correo = %s", (correo,)
        )
        result = conn.cur.fetchone()
        
        if result is None:
            return False, "Correo no encontrado"
        
        stored_password = result[0]
        
        if stored_password != password:
            return False, "Contraseña incorrecta"
        
        return True, "Login exitoso"
    
    except Exception as e:
        print(f"Error al consultar la base de datos: {e}")
        return False, "Error del servidor"
    
    finally:
        del conn  # Cerrar la conexión cuando termine la operación
