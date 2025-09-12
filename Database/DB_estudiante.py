from Database import DatabaseConexion

class EstudianteDB:
    def __init__(self,conexion: DatabaseConexion):
        self.conexion = conexion.get_connection()

    def agregarEstudiante(self, nombres, apellidos, edad):
        sql = "INSERT INTO student (firstNames, lastNames, age) VALUES (%s, %s, %s)"

        conn = self.conexion.get_connection()   # obtener una nueva conexión del pool
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(sql, (nombres, apellidos, edad))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()



    