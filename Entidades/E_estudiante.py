class Estudiante:
    def __init__(self,estudianteID,nombres,apellidos,direccion,edad):
        self._estudianteID = estudianteID
        self.salonID = 0
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.edad = edad

    @property
    def estudianteID(self):
        return self._estudianteID
    

    