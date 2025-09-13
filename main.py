from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from Control.G_agregarEstudiante import AgregarEstudiante

app = FastAPI() 
agregarEstudiante = AgregarEstudiante()


@app.get("/")
def root():
    return {"status": "ok", "message": "Servidor funcionando"}

@app.get("/agregar_estudiante/info_profesor/{profesorID}")
def buscar_Info_Profesor(profesorID: int):
    resultado = agregarEstudiante.buscarInfoProfesor(profesorID)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return resultado

@app.get("/agregar_estudiante/listar_estudiantes")
def listar_Estudiantes():
    try:
        return agregarEstudiante.listarEstudiantes()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error en DB: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

@app.post("/agregar_estudiante")
def agregar_Estudiante_Salon(estudianteID:int,salonID:int,profesorID:int):
    estudiante = agregarEstudiante.agregarEstudianteSalon(estudianteID,salonID,profesorID)
    return {"id": estudiante.estudianteID, "nombre": estudiante.nombres, "salonID": estudiante.salonID}

@app.post("/agregar_estudiante/agregar_salon_profesor")
def agregar_profesor_salon(profesorID:int,salonID:int):
    salon = agregarEstudiante.agregarProfesorSalon(profesorID,salonID)
    return {"id": salon.salonID,"nombre salon:":salon.nombreSalon}

@app.post("/agregar_estudiante/crear_estudiante_prueba")
def crear_Estudiante(nombres:str,apellidos:str,direccion:str,edad:int):
    estudiante = agregarEstudiante.crearEstudiante(nombres,apellidos,direccion,edad)
    return {"id": estudiante.estudianteID, "nombres": estudiante.nombres, "apellidos":estudiante.apellidos, "edad":estudiante.edad}

@app.post("/agregar_estudiante/crear_salon_prueba")
def crear_Salon(nombreSalon:str):
    salon = agregarEstudiante.crearSalon(nombreSalon)
    return {"id": salon.salonID, "nombre salon": salon.nombreSalon}

@app.post("/agregar_estudiante/crear_profesor_prueba")
def crear_Profesor(nombres:str,apellidos:str,direccion:str,edad:int,clave:int):
    profesor = agregarEstudiante.crearProfesor(nombres,apellidos,direccion,edad,clave)
    return {"id": profesor.profesorID, "nombres": profesor.nombres,"apellidos":profesor.apellidos,"direccion":profesor.direccion,"edad":profesor.edad,"clave":profesor.clave}

@app.get("/agregar_estudiante/listar_profesores")
def listar_Profesores():
    return [{"id": p.profesorID, "nombre": p.nombres, "apellidos": p.apellidos} for p in agregarEstudiante.listarProfesores()]

@app.get("/agregar_estudiante/listar_salones")
def listar_Salones():
    return [{"id": s.salonID, "nombre salon": s.nombreSalon} for s in agregarEstudiante.listarSalones()]


