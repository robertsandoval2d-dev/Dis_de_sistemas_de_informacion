from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from Database.Database import Base

class Estudiante(Base):
    __tablename__ = "student"

    estudianteID = Column("studentid",Integer, primary_key=True,index = True)
    salonID = Column("salonid",Integer,ForeignKey("salon.salonid")) 
    nombres = Column("firstnames",String(50),nullable=False)
    apellidos = Column("lastnames",String(50),nullable=False)
    direccion = Column("address",String(50))
    edad = Column("age",SmallInteger)

    salon = relationship("Salon",back_populates="estudiantes")


    '''def __init__(self,estudianteID,nombres,apellidos,direccion,edad):
        self._estudianteID = estudianteID
        self.salonID = 0
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.edad = edad

    @property
    def estudianteID(self):
        return self._estudianteID
    '''

    