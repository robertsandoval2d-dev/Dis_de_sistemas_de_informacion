from Entidades.E_estudiante import Estudiante
from Entidades.E_profesor import Profesor
from Entidades.E_salon import Salon
from Database.Database import SessionLocal
from sqlalchemy.orm import selectinload

class AgregarEstudiante:
    def __init__(self):
        pass

    def buscarInfoProfesor(self, profesorID: int):
            # Crear sesión
            session = SessionLocal()
            try:
                # Consulta profesor y carga salones y estudiantes relacionados
                profesor = session.query(Profesor).options(
                    selectinload(Profesor.salones).selectinload(Salon.estudiantes)
                ).filter_by(teacherID=profesorID).first()

                if profesor:
                    # get_info() accede directamente a atributos de salones y estudiantes
                    return profesor.getInfoProfesor()
                else:
                    return None
            finally:
                # Cerrar sesión siempre
                session.close()

    def listarEstudiantes(self):
            session = SessionLocal()
            try:
                # Trae todos los estudiantes
                estudiantes = session.query(Estudiante).all()
                # Opcional: puedes devolver un listado de nombres o diccionarios
                return ["Conexión a base de datos exitosa",
                    {
                        "ID": e.estudianteID,
                        "Nombre": e.nombres,
                        "Apellido": e.apellidos,
                        "SalonID": e.salonID
                    } for e in estudiantes
                ]
            finally:
                session.close()
    
    def agregarEstudianteSalon(self, estudianteID: int, salonID: int, profesorID: int):
        session = SessionLocal()
        try:
            # 1️⃣ Traer el estudiante
            estudiante = session.query(Estudiante).filter_by(estudianteID=estudianteID).first()
            if not estudiante:
                return f"No se encontró estudiante con ID {estudianteID}"

            # 2️⃣ Traer el salón del profesor
            profesor = session.query(Profesor).options(
                selectinload(Profesor.salones)
            ).filter_by(teacherID=profesorID).first()
            
            if not profesor:
                return f"No se encontró profesor con ID {profesorID}"

            # Buscar el salón específico
            salon = next((s for s in profesor.salones if s.salonID == salonID), None)
            if not salon:
                return f"No se encontró salón con ID {salonID} para el profesor {profesorID}"

            # 3️⃣ Asignar estudiante al salón
            estudiante.salonID = salon.salonID
            session.commit()  # Guardar cambio en la BD

            return f"Estudiante {estudiante.nombres} asignado al salón {salon.nombreSalon}"
        
        finally:
            session.close()
            
    #para fines de prueba
    def crearEstudiante(self, nombres: str, apellidos: str, direccion: str, edad: int):
        session = SessionLocal()
        try:
            # Crear el estudiante
            nuevoEstudiante = Estudiante(
                nombres=nombres,
                apellidos=apellidos,
                direccion=direccion,
                edad=edad
            )

            # Agregar a la sesión y guardar en la BD
            session.add(nuevoEstudiante)
            session.commit()  # SQLAlchemy asigna automáticamente estudianteID
            session.refresh(nuevoEstudiante)  # Trae el ID generado por la BD

            return nuevoEstudiante
        
        finally:
            session.close()
    
    def crearSalon(self, nombreSalon: str, profesorID: int = None):
        """
        Crea un nuevo salón y opcionalmente lo asigna a un profesor.
        """
        session = SessionLocal()
        try:
            # Crear el objeto Salon
            nuevoSalon = Salon(
                nombreSalon=nombreSalon,
                profesorID=profesorID  # Puede ser None si aún no hay profesor asignado
            )

            # Agregar y guardar en la BD
            session.add(nuevoSalon)
            session.commit()
            session.refresh(nuevoSalon)  # Trae el ID generado por la BD

            return nuevoSalon

        finally:
            session.close()
    
    def crearProfesor(self, nombres: str, apellidos: str, direccion: str, edad: int, clave: str):
        session = SessionLocal()
        try:
            nuevoProfesor = Profesor(
                nombres=nombres,
                apellidos=apellidos,
                direccion=direccion,
                edad=edad,
                contra=clave
            )
            session.add(nuevoProfesor)
            session.commit()
            session.refresh(nuevoProfesor)  # Obtener ID generado por BD
            return nuevoProfesor
        finally:
            session.close()
    
    def listarProfesores(self):
        session = SessionLocal()
        try:
            profesores = session.query(Profesor).all()
            return [
                {
                    "ID": p.teacherID,
                    "Nombres": p.nombres,
                    "Apellidos": p.apellidos,
                    "Edad": p.edad,
                    "Direccion": p.direccion
                } for p in profesores
            ]
        finally:
            session.close()

    
    def listarSalones(self):
        session = SessionLocal()
        try:
            salones = session.query(Salon).all()
            return [
                {
                    "ID": s.salonID,
                    "Nombre": s.nombreSalon,
                    "ProfesorID": s.profesorID
                } for s in salones
            ]
        finally:
            session.close()
     

    def agregarProfesorSalon(self, profesorID: int, salonID: int):
            session = SessionLocal()
            try:
                # 1️⃣ Traer el profesor
                profesor = session.query(Profesor).options(
                    selectinload(Profesor.salones)
                ).filter_by(teacherID=profesorID).first()
                if not profesor:
                    return f"No se encontró profesor con ID {profesorID}"

                # 2️⃣ Traer el salón
                salon = session.query(Salon).filter_by(salonID=salonID).first()
                if not salon:
                    return f"No se encontró salón con ID {salonID}"

                # 3️⃣ Asignar el profesor al salón
                salon.profesorID = profesor.teacherID
                session.commit()  # Persistir en la BD

                return f"Salón {salon.nombreSalon} asignado al profesor {profesor.nombres} {profesor.apellidos}"

            finally:
                session.close()    