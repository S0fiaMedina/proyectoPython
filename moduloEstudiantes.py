import os
from funcionesUniversales import verificarDuplicadosJson, menus2Lv, validacionInput, mostrarMenu
import json

patch = os.path.join("archivosJsonProyecto","campers.json")

camper = {}
with open(patch, "r") as f:
    camper = json.loads(f.read())

def agregarNumeros() -> dict:
    bandera2 = True
    colTel = {
        "Fijo" : [],
        "Celular": [],
        }
    while bandera2:
        os.system("clear")
        try:
            
            opc = int(input("Seleccione el numero de contacto del camper\n\t1. Fijo\n\t2. Celular\n"))
            if opc == 1:
                newTel =  int(input("Ingrese el numero de telefono Fijo:\n>>> "))
                colTel["Fijo"].append(newTel) #reducir repeticion
                opc = int(input("\nDigite '1' para introducir un nuevo numero de telefono\nDigite cualquier otro numero para salir.\n>>> "))
                if opc != 1:
                    bandera2 = False
                    return colTel
            elif opc == 2:
                newCel = int(input("Ingrese un numero de telefono celular:\n>>> "))
                colTel["Celular"].append(newCel)
                opc = int(input("\nDigite '1' para introducir un nuevo numero de telefono\nDigite cualquier otro numero para salir.\n>>> "))
                if opc != 1:
                    bandera2 = False
                    return colTel
            else:
                raise("Opcion invalida")
            
        except ValueError:
            print("X    Error: has ingresado un numero o una opcion invalida invalidos")
            os.system("sleep 2")
            
#FUNCION PRINCIPAL
def registrarCamper() -> str:
    bandera = True
    while bandera:
        try:  # input datos de estudiante
            os.system("clear")
            cc = int(input("Ingrese el numero de identificación del camper:\n"))
            #verficar si ya hay un estudiante con ese documento
            while verificarDuplicadosJson(camper,cc):
                print(f"X    Error:{camper[cc]['Nombre']} ya tiene esa identificacion({cc})")
                cc = int(input(("Ingrese un nuevo numero: \n>>> ")))
                
            camper[cc] = {
                "Nombre": str(input("Ingrese el nombre completo  del camper:\n")),
                "Direccion": str(input("Ingrese la direccion del camper:\n")),
                "Edad": int(input("Ingrese su la edad del camper\n>>> ")),
                "Telefonos": agregarNumeros(),  # lista - diccionario - litsa
                "Acudiente": {
                    "Nombre": str(input("Nombre del acudiente o contacto de emergencia:\n>>> ")),
                    "Numero de contacto": int(input("Digite un numero para contactarl@\n >>> "))
                },
                "Estado": "Inscrito"
            }

        except ValueError:
            print("Ingresa datos validos")
            os.system("sleep 2")
        else:
            #Carga los datos 
            with open(patch, "w+") as f:
                f.write(json.dumps(camper, indent=4))

            #prints finales
            print( f'El camper {cc} - {camper[cc]["Nombre"]} ha sido registrado.\n')
            flag = input("digite 'x' para agregar otro estudiante.\nPara salir, ingrese cualquier otra letra.\n >>> ")

            #break the loop
            if flag.lower() != 'x':
                bandera = False

def listarEstudiantes():
    menus2Lv(camper, "LISTA DE ESTUDIANTES", "Nombre", "Nombre") #listar campers

def listarAprobados():
    for id in camper.keys():
        if camper[str(id)]['Estado'] == 'Aprobado':
            traineerDisp=  {
        id:{"Nombre":camper[str(id)]['Nombre']}}
        menus2Lv(id,"CAMPERS APROBADOS","Nombre", "Nombres")
    if not id:
        print("No hay estudiantes que hayan aprobado")

subOpciones =  {
            "1": {
                "Nombre": "Registrar campers",
                "Accion": registrarCamper
            },
            "2": {
                "Nombre": "Ver campers inscritos",
                "Accion": listarEstudiantes
            },
            "3": {
                "Nombre": "Ver campers aprobados (estudiantes en el campus)",
                "Accion": listarAprobados
            },
            "4": {
                "Nombre": "Ver estudiantes con bajo rendimiento",
                "Accion": "No implementado :("
            },
            "5": {
                "Nombre": "Retornar al menú principal",
                "Accion": ""
            }
        }


#FUNCION PRINCIPAL
def menuEstudiantes():
    while True:
        menus2Lv(subOpciones, "MODULO DE ESTUDIANTES", "Nombre", "Acciones")
        opc = validacionInput("Introduzca un valor que corresponda a la opcion que desea realizar\n >>> ")
        if opc in range(1, len(subOpciones)+1):
            if opc == len(subOpciones):
                    return 0
            else: subOpciones[str(opc)]["Accion"]()

