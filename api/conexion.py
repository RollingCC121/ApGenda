import psycopg
from fastapi import FastAPI, HTTPException

# Clase de conexión (manteniendo tu implementación)
class Connection:
    def __init__(self):
        try:
            self.conn = psycopg.connect(
                "dbname=dbappweb user=postgres password=pollito host=3.228.108.255 port=5432"
            )
            self.cur = self.conn.cursor()
        except psycopg.OperationalError as err:
            print(err)
            if self.conn:
                self.conn.close()

    def __del__(self):
        if self.conn:
            self.conn.close()
'''
    # Método para ejecutar consultas SQL
    def execute_query(self, query, params=None):
        try:
            self.cur.execute(query, params)
            self.conn.commit()
        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")
            self.conn.rollback()

    # Método para ejecutar consultas SELECT
    def fetch_query(self, query, params=None):
        try:
            self.cur.execute(query, params)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print(f"Error obteniendo los datos: {e}")
            return None
            '''