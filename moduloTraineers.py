import os
import json
from funcionesUniversales import  (verificarDuplicadosJson as search
                                   , menus2Lv as listar
                                   , validacionInput as validar)

pathTraineer = os.path.join("archivosJsonProyecto","traineers.json")
pathRutas = os.path.join("archivosJsonProyecto", "rutas.json")


with open(pathTraineer,'r') as dataTraineer:
    baseDataTraineer = json.loads(dataTraineer.read())
with open(pathRutas, "r") as dataRutas:
    dataBaseRutas = json.loads(dataRutas.read())

def seleccionarHorario() -> dict:
    opcionesHorario = {
    '1': '6 AM a 9:30 AM',
    '2': '9:30 AM a 1:30 PM',
    '3': '2:00 PM a 5:30 PM',
    '4': '5:30 PM a 9:30 PM'
    }
    trainerHorario = {}
    while True:
        print("Opcion\tHorario")
        for opcion, horas in opcionesHorario.items():
            print(f"{opcion}\t{horas}")
        try:
            select = int(input("\nDigite una opcion de horario en donde el traineer este disponible:\n>>> ".strip()))
            if (0 <select<=(len(opcionesHorario))):
                trainerHorario.update({str(select): opcionesHorario[str(select)]})
            else:
                print("X    Error: Valor fuera de los rangos")
        except ValueError:
            print("X   Error: Has ingresado un valor invalido")
        else:
            flag = input("digite 'x' para agregar otro HORARIO.\nPara salir, ingrese cualquier otra letra o caracter.\n >>> ")
            if flag.lower() != 'x':
                return trainerHorario


            



def registroTraineer():
      bandera = True
      while bandera:
            os.system("clear")
            cc = int(input("Ingrese el numero de identificación del traineer:\n"))
            while search(baseDataTraineer, cc):
                print(f"X    Error:{baseDataTraineer[str(cc)]['Nombre']} ya tiene esa identificacion({cc})")
                cc = int(input(("Ingrese un nuevo numero: \n>>> ")))
            
            baseDataTraineer[cc] = {
                "Nombre" : str(input("Ingrese el nombre del traineer\n>>> ").strip()),
                "Horario": seleccionarHorario()
                
            }
            
            with open(pathTraineer,"w") as dataTraineer:
                dataTraineer.write(json.dumps(baseDataTraineer, indent = 4))

            print(f"El traineer:{baseDataTraineer[cc]['Nombre']} ha sido registrado exitosamente con el id: {cc}")
            flag = input("digite 'x' para agregar otro TRAINEER.\nPara salir, ingrese cualquier otra letra.\n >>> ")
            #break the loop
            if flag.lower() != 'x':
                bandera = False

def listarTraineers():
    listar(baseDataTraineer, "LISTA DE TRAINEERS", "Nombre", "Nombre") #listar traineers
menuTraineers= {
    "1":{
        "Nombre":"Registrar Traineer",
        "Accion": registroTraineer
    },
    "2":{
        "Nombre": "Listar Traineers",
        "Accion": listarTraineers
    },
    "3":{
        "Nombre": "Retornar al menu principal"
    }
}

def menuTraineer():
    while True:
        listar(menuTraineers, "MODULO DE TRAINEERS", "Nombre", "Acciones")
        opc = validar("Introduzca un valor que corresponda a la opcion que desea realizar\n >>> ")
        if opc in range(1, len(menuTraineers)+1):
            if opc == len(menuTraineers):
                return 0
            else: menuTraineers[str(opc)]["Accion"]()


