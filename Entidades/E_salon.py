from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from Database.Database import Base

class Salon(Base):
    __tablename__ = "salon"

    salonID = Column("salonid",Integer, primary_key=True,index=True)
    # aquí especificamos que la columna en BD se llama "className"
    nombreSalon = Column("classname", String(50), nullable=False)
    profesorID = Column("teacherid",Integer,ForeignKey("teacher.teacherid"))

    estudiantes = relationship("Estudiante", back_populates="salon")
    profesor = relationship("Profesor",back_populates="salones")


    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.salonID = self.salonID
        return estudiante 

    def obtenerInfoSalon(self):
        return f"ID del salón: {self.salonID}, Nombre del salón: {self.nombreSalon}"

    '''def __init__(self,salonID,nombreSalon):
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
    
    '''