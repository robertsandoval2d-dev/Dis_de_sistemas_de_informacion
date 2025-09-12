import mysql.connector

class DatabaseConexion():
    def __init__(self):
        return mysql.connector.connect(
        host="localhost",      # o la IP/servidor
        user="root",           # tu usuario
        password="root",       # tu contraseña
        database="VIRTUAL_ASSESSMENT"  # tu base de datos
        )
    
