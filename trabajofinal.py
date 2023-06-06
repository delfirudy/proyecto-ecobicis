from clases_funciones import *
from submenus import *

class Menu:
    recorrerpickle()
    seguir = True
    while seguir == True:
        print("1. Ingreso de datos cliente")
        print("2. Ingreso de datos trabajador")
        print("3. Opciones cliente")
        print("4. Opciones trabajador")
        print("5. Salir")
        print("")
        eleccion = input("Ingrese opcion: ").strip()
        print("")
        if eleccion == "1":
            Cliente()
        elif eleccion == "2":
            Trabajador()
        elif eleccion == "3":
            submenucliente()
        elif eleccion == "4":
            submenutrabajador()
        elif eleccion == "5":
            actualizarpickle()
            exit()
        else:
            print("Ingreso incorrecto de opcion")
            print("")

trabajofinal = Menu()
