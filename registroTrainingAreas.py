import os
import json
from funcionesUniversales import( getNextIdSecuencial as obtenerId,
                                 validacionInput as validar,
                                 menus2Lv as imprimirMenu)
pathTraining = os.path.join("archivosJsonProyecto","areasTraining.json")

with open(pathTraining,'r') as dataTraining:
    baseDataTraining = json.loads(dataTraining.read())


def registroSalon():
      bandera = True
      while bandera:
            os.system("clear")
            idArea = obtenerId(baseDataTraining)
            baseDataTraining[idArea] = {
                "Nombre" : str(input("Ingrese el nombre del salón\n>>> ").strip()),
                "Capacidad" : 33
                
            }
            
            with open(pathTraining,"w") as dataTraining:
                dataTraining.write(json.dumps(baseDataTraining, indent = 4))

            print(f"Salon:{baseDataTraining[idArea]['Nombre']} ha sido registrado exitosamente con el id: {idArea}")
            flag = input("digite 'x' para agregar otro salón.\nPara salir, ingrese cualquier otra letra.\n >>> ")
            idArea+=1
            #break the loop
            if flag.lower() != 'x':
                bandera = False

opcionesArea={
    "1": {
        "Nombre":"Registrar Salon",
        "Funcion": registroSalon 
    },
    "2":{
         "Nombre": "Retornar al menu principal"

    }
}
#FUNCION PRINCIPAL
def menuArea():
    while True:
        imprimirMenu(opcionesArea, "MODULO DE AREAS DE TRAINING(SALONES)", "Nombre", "Acciones")
        opc = validar("Introduzca un valor que corresponda a la opcion que desea realizar\n >>> ")
        if opc in range(1, len(opcionesArea)+1):
            if opc == len(opcionesArea):
                return 0
            else: opcionesArea[str(opc)]["Accion"]()

