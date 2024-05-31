#import lib
import os
import json
from funcionesUniversales import (verificarDuplicadosJson as buscar, 
                                  getNextIdSecuencial as getId,
                                  menus2Lv as listar,
                                  validacionInput as validar )

#crear rutas para acceder a los json
pathSubRutas = os.path.join("archivosJsonProyecto","subRutas.json")
pathRutas = os.path.join("archivosJsonProyecto", "rutas.json")
pathTraineer = os.path.join("archivosJsonProyecto","traineers.json")
pathStudent = os.path.join("archivosJsonProyecto","campers.json")

# Cargar de archivos json
with open(pathSubRutas, "r") as dataSubRutas:
    dataBaseSubRutas = json.loads(dataSubRutas.read())
with open(pathRutas, "r") as dataRutas:
    dataBaseRutas = json.loads(dataRutas.read())


rutaOpciones = {
    "1":"Ruta NodeJS",
    "2":"Ruta Java",
    "3": "Ruta Netcore"
}
def menu() -> int:
    while True:
        os.system("clear")
        print("AVISO:   Las rutas transversales (Rutas que ven todos las rutas de entrenamiento) ya estan definidas, las cuales son:\n- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)\n- Programación Web (HTML, CSS y Bootstrap)\n\n")
        print("Seleccione una ruta para construir: ")
        for i in range (1, len(rutaOpciones)+1):
            print(f"{i}\t{rutaOpciones[str(i)]}")

        opc = int(input("\n>>> ").strip())
        if 0<opc <= len(rutaOpciones):
            return opc

def Tema(diccionario: dict, i: int,add:int)-> int:
        if add == 1:
            opEvaluada = "SGDB principal"
        elif add == 2: 
            opEvaluada = "SGDB alternativo"
        else: opEvaluada = diccionario[str(i)]['Nombre']
        print(f"Digite un numero correspondiente a un tema de {opEvaluada}")
        print("*"*36)
         
        for elemento in range(len(diccionario[str(i)]['Temas'])):
                print(f"{elemento+1}\t{diccionario[str(i)]['Temas'][elemento]}") #itera sobre lista
        try:
            while True:
                temaSelect = int(input("\n>>> "))
                while temaSelect not in range(1, len(diccionario[str(i)]['Temas'])+1):
                    print("X    Error: Ingresaste una opcion incorrecta.")
                    int(input("Ingresa una nueva opcion\n>>> "))
                return diccionario[str(i)]['Temas'][temaSelect-1]
        except ValueError:
            print("X    Error: Ingresaste un tipo de dato incorrecto")


def agregarDato(rutaTraining:int) -> dict :
    print("*"*36+"\n"+rutaOpciones[str(rutaTraining)]+"\n"+"*"*36)
    modOp = {
            "1":{
                'Nombre':"Programación formal",
                'Temas': ['Java', 'JavaScript', 'C#']
            },
            "2":{
                'Nombre':"Bases de datos",
                'Temas': ['Mysql', 'MongoDb', 'Postgresql']
            },
            "3":{
                'Nombre':"Backend",
                'Temas': ['NetCore', 'Spring Boot', 'NodeJS', 'Express']

            }
        }
    rutaAvanzada = {
            "1":{
                'Nombre':"Programación formal",
                'Temas': Tema(modOp,1,0)
            },
            "2":{
                'Nombre':"Bases de datos",
                'Temas':{
                    "SGBD_Principal": Tema(modOp,2,1),
                    "SGBD_Alternativa":Tema(modOp,2,2)
                }
                
            },
            "3":{
                'Nombre':"Backend",
                'Temas': Tema(modOp, 3,0)
            }
        }
    return rutaAvanzada

def ingresoDatosRutas():
    rutaSelec = menu() #Ruta seleccionada para armar
    while True:
        idRuta = getId(dataBaseRutas)
        dataBaseRutas[idRuta] = {
                "Nombre": rutaOpciones[str(rutaSelec)],
                "Transversales":{
                "01": {
                    "Nombre": "Fundamentos de programacion",
                    "temas":{
                        "Tema1": "Algoritmia",
                        "Tema 2":"Pseint",
                        "Tema 3":"Python"
                    }
                },
                "02": {
                    "Nombre": "Programacion web",
                    "temas":{
                        "Tema1": "HTML",
                        "Tema 2":"CSS",
                        "Tema 3":"JavaScript"
                    }
            },
            "Avanzadas":agregarDato(rutaSelec)}}
        
        
        with open(pathRutas, "w") as dataRutas:
            dataRutas.write(json.dumps(dataBaseRutas, indent = 4))
        print("Ruta ingresada exitosamente")
        return 0 

opcionesRutas={
"1":{
    "Nombre": "Construir ruta",
    "Funcion": ingresoDatosRutas
    },
"2":{
     "Nombre": "Retornar al menu principal"
}
}
#FUNCION PRINCIPAL
def menuRutas():
    while True:
        listar(opcionesRutas, "MODULO DE RUTAS", "Nombre", "Acciones")
        opc = validar("Introduzca un valor que corresponda a la opcion que desea realizar\n >>> ")
        if opc in range(1, len(opcionesRutas)+1):
            if opc == len(opcionesRutas):
                    return 0
            else: opcionesRutas[str(opc)]["Funcion"]()

