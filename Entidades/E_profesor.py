from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from Database.Database import Base


class Profesor(Base):
    __tablename__ = "teacher"

    profesorID = Column("teacherid",Integer, primary_key=True,index=True)
    nombres = Column("firstnames",String(50),nullable=False)
    apellidos = Column("lastnames",String(50),nullable=False)
    direccion =  Column("address",String(50),nullable=False)
    edad = Column("age",Integer,nullable=False)
    contra = Column("pwd",String(50))

    salones = relationship("Salon", back_populates="profesor")

    def agregarSalon(self,salon):
        self.salones.append(salon)
        return salon
    
    def obtenerSalonProfesor(self,salonID):
        for salon in self.salones:
            if salon.salonID == salonID:
                return salon
            
def getInfoProfesor(self):
    # Información básica del profesor
    info = {
        "teacherID": self.teacherID,
        "nombres": self.nombres,
        "apellidos": self.apellidos,
        "salones": []
    }

    # Salones asignados y sus estudiantes
    for salon in self.salones:
        info["salones"].append({
            "salonID": salon.salonID,
            "nombreSalon": salon.nombreSalon,
        })

    return info
    

    '''def __init__(self,profesorID,nombres,apellidos,direccion,edad,clave):
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
        
        return info'''
    

