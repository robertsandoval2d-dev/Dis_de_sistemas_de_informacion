from Entidades.E_estudiante import Estudiante
from Entidades.E_profesor import Profesor
from Entidades.E_salon import Salon

class AgregarEstudiante:
    def __init__(self):
        self.profesores = []
        self.estudiantes = []
        self.salones = []
        self.next_id_prof = 1
        self.next_id_alum = 1
        self.next_id_salon = 1

    def buscarInfoProfesor(self,profesorID):
        for profesor in self.profesores:
            if profesor.profesorID == profesorID:
                return profesor.getInfoProfesor()

    def listarEstudiantes(self):
        return self.estudiantes
    
    def agregarEstudianteSalon(self,estudianteID,salonID,profesorID):
        estudianteEncontrado = None

        for estudiante in self.estudiantes:
            if estudiante.estudianteID==estudianteID:
                estudianteEncontrado = estudiante
                break

        for profesor in self.profesores:
            if profesor.profesorID == profesorID:
                return profesor.obtenerSalonProfesor(salonID).agregarEstudiante(estudianteEncontrado)
            
    #para fines de prueba
    def crearEstudiante(self,nombres,apellidos,direccion,edad):
        nuevoEstudiante = Estudiante(self.next_id_alum,nombres,apellidos,direccion,edad)
        self.estudiantes.append(nuevoEstudiante)
        self.next_id_alum+=1
        return nuevoEstudiante
    
    def crearSalon(self,nombreSalon):
        nuevoSalon = Salon(self.next_id_salon,nombreSalon)
        self.salones.append(nuevoSalon)
        self.next_id_salon+=1
        return nuevoSalon
    
    def crearProfesor(self,nombres,apellidos,direccion,edad,clave):
        nuevoProfesor = Profesor(self.next_id_prof,nombres,apellidos,direccion,edad,clave)
        self.profesores.append(nuevoProfesor)
        self.next_id_prof+=1
        return nuevoProfesor
    
    def listarProfesores(self):
        return self.profesores
    
    def listarSalones(self):
        return self.salones
    
    def agregarProfesorSalon(self,profesorID,salonID):
        salonEncontrado = None

        for salon in self.salones:
            if salon.salonID == salonID:
                salonEncontrado=salon
                break

        for profesor in self.profesores:
            if profesor.profesorID == profesorID:
                return profesor.agregarSalon(salonEncontrado)    


    