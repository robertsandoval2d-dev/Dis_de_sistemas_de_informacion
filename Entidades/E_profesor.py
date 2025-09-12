#from Database import DatabaseConexion
from Entidades.E_salon import Salon


class Profesor:

    def __init__(self,profesorID,nombres,apellidos,direccion,edad,clave):
        self._profesorID = profesorID
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.edad = edad
        self.clave = clave
        
        self.salones = []

    @property
    def profesorID(self):
        return self._profesorID

    def agregarSalon(self,salon: Salon):
        self.salones.append(salon)
        return salon

    def obtenerSalonProfesor(self,salonID):
        for salon in self.salones:
            if salon.salonID == salonID:
                return salon

    def getInfoProfesor(self):
        info = f"Nombres del profesor: {self.nombres}\nApellidos del profesor: {self.apellidos}\n"
        
        if self.salones:
            info += "Salones del profesor:\n"
            for salon in self.salones:
                info += f" - {salon.getInfoSalon()}\n"
        else:
            info += "No tiene salones asignados.\n"
        
        return info
    


'''class ProfesorDataBase:

    def __init__(self,conexion: DatabaseConexion):
        self.conexion = conexion.get_connection()
        self.cursor = self.conexion.cursor(dictionary=True)

    def getDatosProfesor(self, teacher_id):
        query = """
        SELECT firstNames AS Nombres, lastNames AS Apellidos
        FROM teacher
        WHERE teacherID = %s
        """
        self.cursor.execute(query, (teacher_id,))
        return self.cursor.fetchone()  # devuelve solo una fila
    
    def getSalonesProfesor(self, teacher_id):
        query = """
        SELECT s.salonID, s.className, t.firstNames
        FROM salon s
        JOIN teacher t ON s.teacherID = t.teacherID
        WHERE s.teacherID = %s
        """
        self.cursor.execute(query,(teacher_id,))
        return self.cursor.fetchall()

db = DatabaseConexion()
prueba = ProfesorDataBase(db)
print(prueba.getDatosProfesor(1000))
print(prueba.getSalonesProfesor(1000))
    '''