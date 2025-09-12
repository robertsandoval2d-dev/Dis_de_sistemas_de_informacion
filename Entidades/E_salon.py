from Entidades.E_estudiante import Estudiante

class Salon:
    def __init__(self,salonID,nombreSalon):
        self._salonID = salonID
        self.nombreSalon = nombreSalon
        
        self.estudiantes = []

    @property
    def salonID(self):
        return self._salonID

    def agregarEstudiante(self,estudiante: Estudiante):
        self.estudiantes.append(estudiante)
        estudiante.salonID = self.salonID
        return estudiante

    def obtenerInfoSalon(self):
        return f"ID del salón: {self.salonID}, Nombre del salón: {self.nombreSalon}"
    
    