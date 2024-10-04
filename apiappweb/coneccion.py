import psycopg
from fastapi import FastAPI, HTTPException

# Clase de conexión (manteniendo tu implementación)
class Connection:
    def __init__(self):
        try:
            self.conn = psycopg.connect(
                "dbname=dbappweb user=postgres password=pollito host=localhost port=5432"
            )
            self.cur = self.conn.cursor()
        except psycopg.OperationalError as err:
            print(err)
            if self.conn:
                self.conn.close()

    def __del__(self):
        if self.conn:
            self.conn.close()