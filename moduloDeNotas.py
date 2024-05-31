

#Importacion de librerias
import json
import os
from funcionesUniversales import jsonIsEmpty, verificarDuplicadosJson

#Identificacion rutas json
patchPruebas = os.path.join("archivosJsonProyecto", "pruebas.json")#ruta de json de pruebas 
patchCamper = os.path.join("archivosJsonProyecto", "campers.json")#ruta de camper (cambiar estado)

#carga archivos json - pruebas y campers
with open(patchPruebas, "r") as dataPruebas:
    dataBasePruebas = json.loads(dataPruebas.read())
with open(patchCamper, "r") as dataCampers:
    dataBaseCampers = json.loads(dataCampers.read())

def menuPrueba() -> int : #Posible función universal - creacion de menus
    while True:
        #os.system("clear")
        print(f"{'-'*36}\n Modulo de Pruebas\n{'-'*36}\n")
        print("1. Agregar nota a una NUEVA prueba\n2. Agregar nota a a una prueba EXISTENTE\n3. Retornar al menu principal")
        try:
            opc = int(input("\nIngrese una opcion\n>>> "))
                
        except ValueError:
            print("X   Error: Has ingresado una opción invalida")
            os.system("sleep 2")
        else:
            print(opc)
            if opc == 1: return 1
            elif opc ==2: return 2
            elif opc == 3: return 3
            else:
                print("X    Error: ingresa una opcion que esté en el menú")
                os.system("sleep 2")
             
def agregarPromedio(id:int) -> dict: #parametro, para cuando se vaya a ingrear cosas diferentes a filtros
    Promedio = {}
    valorNota = 1 #cuando se ingresen otros filtros
    while True:
        #os.system("clear")
        try:
            PromedioTeoria = int(input("Ingrese la nota que tuvo el estudiante en la prueba teorica\n>>> ").strip())
            PromedioPractica = int(input("Ingrese la nota de la prueba practica:\n>>> ").strip())
            if PromedioTeoria in range(101) and PromedioPractica in range(101):
                Promedio["Teoria"], Promedio["Practica"] =PromedioTeoria, PromedioPractica 
                Promedio["Nota"] = round(((Promedio["Teoria"])+(Promedio["Practica"]))/2,2)
                if Promedio['Nota']> 60:
                    dataBaseCampers[str(id)]['Estado'] = "Aprobado"
                else:
                    dataBaseCampers[str(id)]['Estado'] = "Reprobado"
                return Promedio
            else:
                print("❌    Error: Ingresa numeros entre 1 y 100.")

        except (ValueError, TypeError):
            print("X   Error: Has ingresado un valor invalido")
            os.system("sleep 2")


#Registrar pruebas - si el est no tiene ninguna nota ingresada, se añadira por defecto a examen inicial
def registroPruebas() -> str:
    while True:
        #os.system("clear")
        opc = menuPrueba()
        if opc == 3:
            return 0
        elif opc == 1:
            try:
                nombre = str(input("o   AVISO: El nombre de la prueba debe ser unico.\nIngrese el nombre de la prueba\n>>> "))
                while verificarDuplicadosJson(dataBasePruebas, nombre):
                    nombre = str(input(f"X  Error, ese nombre ya existe\nIngrese uno nuevo\n>>> ").strip())

                estudianteId = int(input("Ingrese el Id del estudiante que presentó la prueba\n>>> ").strip())
                #CONVERTIR A STR
                while  not(verificarDuplicadosJson(dataBaseCampers, estudianteId)):
                    estudianteId = int(input(f"X     Error: el estudiante con el Id no existe, intente de nuevo\n>>> ").strip())

                if (dataBaseCampers[str(estudianteId)]['Estado']) == "Inscrito":
                    nombre2 = nombre
                    res = str(input("o    AVISO: El estudiante está pre- inscrito, por lo que las notas que se van a registrar, se van a ver reflejadas en su Examen de ingreso\nDigite 'S' para proceder.\nDigite cualquier letra para ir de vuelta al menú del modulo de pruebas\n>>> ").strip())
                    if res.lower() == 's':
                        dataBasePruebas[nombre]= {
                            estudianteId: {
                            "Nombre estudiante": dataBaseCampers[str(estudianteId)]["Nombre"],
                            "Promedio": agregarPromedio(estudianteId)
                                }
                        }
                        with open(patchPruebas, "w+") as filePruebas:
                            filePruebas.write(json.dumps(dataBasePruebas, indent=4))
                        print(f"Se han registrado las notas del estduiante {dataBaseCampers[str(estudianteId)]['Nombre']} \n Su promedio fue de: {nuevo_registro[nombre][estudianteId]['Promedio']['Nota']}, por lo que su estado cambia a {dataBaseCampers[str(estudianteId)]['Estado']}")
        
            except ValueError:
                print("X    Error: Has ingresado un tipo de datos invalidos")
                os.system("sleep 2")
            #except KeyError:
                print("No encontrado")
            
                
    

