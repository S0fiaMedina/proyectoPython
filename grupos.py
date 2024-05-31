#CAMBIOS
# Se agraga validacion de fechas, numeros bvalidos y que sea mayor a hoy
import json 
import os
import datetime
import json
from funcionesUniversales import(
    validacionInput as validar,
    getNextIdSecuencial as obtenerId,
    verificarDuplicadosJson as search,
    header as titulo,
    menus2Lv as listar,
    verificaInscrito as isIn,
    jsonIsEmpty as empty

    
)


pathGrupos = os.path.join("archivosJsonProyecto", "grupos.json")
pathRutas = os.path.join("archivosJsonProyecto", "rutas.json")
pathTraineer = os.path.join("archivosJsonProyecto","traineers.json")
pathStudent = os.path.join("archivosJsonProyecto","campers.json")

# Cargar de archivos json
with open(pathGrupos, "r") as dataGrupos:
    dataBaseGrupos = json.loads(dataGrupos.read())
with open(pathRutas, "r") as dataRutas:
    dataBaseRutas = json.loads(dataRutas.read())
with open(pathTraineer,'r') as dataTraineer:
    dataBaseTraineer = json.loads(dataTraineer.read())
with open(pathStudent, "r") as f:
    camper = json.loads(f.read())

def ingresarFecha(opcion:str) ->datetime.date:
    while True:
        try:
            dia = validar("Ingrese el dia de "+opcion+"\n>>> ")
            mes = validar("Ingrese el mes de "+opcion+"\n>>> ")
            anio = validar("Ingrese el anio de "+opcion+"\n>>> ")
            fecha = datetime.date(anio, mes, dia)
        except ValueError:
            print("X\tERROR: ¿Tal vez ingresaste un dia, mes o año de "+opcion+" fuera de los rangos?")
        else:
            return fecha
 
def seleccionarRuta() -> dict:
    while True:
        listar(dataBaseRutas, "RUTAS DISPONIBLES", "Nombre", "Nombre de la ruta")
        opc = validar("Introduzca un valor que corresponda a la ruta que desea asignar  al grupo\n >>> ")
        if opc in range(1, len(dataBaseRutas)+1):
            return dataBaseRutas[str(opc)]["Nombre"]

            
def ingresarEstudiante() -> dict:
    bandera = True
    while bandera:
        os.system("clear")
        camperId = validar("Ingrese la identificacion del estudiante para agregar al grupo \n>>> ")
        while not(search(camper, camperId)):
            camperId = validar("X\tERROR: identificacion inexistente.\nIngrese una nueva identificacion")
        if isIn(camper,camperId) == True:
            estudiantes = {
                camperId: camper[str(camperId)]['Nombre']
            }
            flag = input("digite 'x' para agregar otro TRAINEER.\nPara salir, ingrese cualquier otra letra.\n >>> ")
            if flag.lower() != 'x':
                bandera = False
            return estudiantes
        else: 
            print("!\tAVISO: El estudiante no fue aprobado. No se puede agregar al grupo")
            os.system("sleep 2")

def verificarTraineers():
    for id in dataBaseTraineer.keys():
        if dataBaseTraineer[str(id)]['Horario'] == True:
            traineerDisp=  {
        id:{"Nombre":dataBaseTraineer[str(id)]['Horario']}}
    return traineerDisp
    
            

def agregarTraineer() -> dict:
    traineers = { verificarTraineers()}
    listar(dataBaseTraineer, "TRAINEERS DISPONIBLES", "Nombre", "Nombre")

def crearGrupo():
    titulo("CREACION DE GRUPOS")
    while True:
        idGrupo = obtenerId(dataBaseGrupos)
        print("!\tAVISO: El nombre del grupo debe ser unico")
        nombre = input("Ingresa el nombre del grupo\n>>> ")
        while search(dataBaseGrupos, nombre):
            print("X\tERROR: Ya existe un grupo con ese nombre")
        Grupos = {
            "FechaInicio": ingresarFecha("inicio").strftime('%Y-%m-%d'),
            "FechaFin": ingresarFecha("Fin").strftime('%Y-%m-%d'),
            "Estudiantes":ingresarEstudiante(),
            "Traineer": "Agrega Traineer",
            "Horario": "importar de Traineer",
            "Ruta de entrenamiento": seleccionarRuta()
        }
        print(Grupos)
        return 0

opcionesGrupo={
    "1": {
        "Nombre":"Registrar Grupo",
        "Funcion": crearGrupo 
    },
    "2":{
         "Nombre": "Retornar al menu principal"

    }
}
#FUNCION PRINCIPAL
def menuGrupos():
    while True:
        listar(opcionesGrupo, "MODULO DE AREAS DE TRAINING(SALONES)", "Nombre", "Acciones")
        opc = validar("Introduzca un valor que corresponda a la opcion que desea realizar\n >>> ")
        if opc in range(1, len(opcionesGrupo)+1):
            if opc == len(opcionesGrupo):
                return 0
            else: opcionesGrupo[str(opc)]["Accion"]()


