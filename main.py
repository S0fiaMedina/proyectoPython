from os import system
from grupos import menuGrupos
from moduloDeNotas import registroPruebas
from moduloEstudiantes import menuEstudiantes
from moduloRutas import menuRutas
from moduloTraineers import menuTraineer
from registroTrainingAreas import menuArea
from funcionesUniversales import (
    menus2Lv as imprimirMenu,
    validacionInput as validar,
)

menuPrincipal = {
    "1": {
        "Nombre": "ESTUDIANTES",
        "Funcion": menuEstudiantes
    },
    "2": {
        "Nombre": "TRAINERS",
        "Funcion": menuTraineer
        },
    "3": {
        "Nombre":"NOTAS",
        "Funcion": registroPruebas
        },
    "4":{
        "Nombre": "SALONES",
        "Funcion": menuArea
        },

    "5": {
        "Nombre":"RUTAS",
        "Funcion": menuRutas
        },

    "6": {
        "Nombre":"SALIR"
        }
}
def main():
    while True:
        #system("clear")
        try:
            imprimirMenu(menuPrincipal, "CAMPUSLAND","Nombre","Modulo")
            opc = validar("Ingrese el numero del modulo al que desea entrar\n >>>")
            if opc == len(menuPrincipal):
                    return 0
        except KeyError:
            print("X    ERROR: Has ingresado un tipo invalido de datos")
        else:
             menuPrincipal[str(opc)]['Funcion']()
          


          
main()

