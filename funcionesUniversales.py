from os import system


def verificarDuplicadosJson(data: dict,clave) -> bool:
    return str(clave) in data #retorna True si esta


def jsonIsEmpty(diccionario : dict ) -> bool: #hacer que devuelva el contenido
    if not(diccionario): # { } -> false
        return True # True = el diccionario es vacio

def getNextIdSecuencial(diccionario: dict) -> int:
    return len(diccionario)+1

def mostrarMenu(opciones:dict,columna1:str, columna2:str): #recorrer dicconario con un solo nivel
    print(f"{columna1}\t\t{columna2}\n")
    for nOpcion,contenido in opciones.items():
        print(f"{nOpcion}\t\t{contenido}")

def header(title:str):
    ancho = len(title)*3
    numCaracter = "°"*ancho
    print(numCaracter+ "\n"+title.center(ancho)+"\n"+ numCaracter )

def menus2Lv(diccionario:dict,title:str,campoOpc:str,columna2:str) -> int:
    header(title)
    print(f"N° opcion\t{columna2}\n{'-'*36}")
    for key in diccionario.keys():
         print(f'{key}\t{diccionario[key][campoOpc]}')

def validacionInput(mensaje:str)-> int: #Todos los que usen este menu deben tener while y un typeError
    while True:
        try:
            dato = int(input(mensaje).strip())
        except Exception as error:
            if error == ValueError or TypeError or KeyError:
                print("X\tERROR: Has ingresado un tipo de dato invalido")
                system("sleep 2")    
            if error == ZeroDivisionError:
                print("X\tERROR: No se puede dividir entre 0")
                system("sleep 2")    
        else:
            return dato
        
def verificaInscrito(DBCampers:dict, id:int)-> bool:
        if DBCampers[str(id)]['Estado'] == 'Aprobado':
            return True
        else: return False
#agregar  eleccion  
def funcion():
    print("wdhhdwqdwed")

