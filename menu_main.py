from actualizacion_pickle import *
from menu_submenu import *

class Menu:
    """Manejo de opciones del menu principal.
    Returns:
        None
    """
    recorrerPickle()
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
            subMenuCliente()
        elif eleccion == "4":
            subMenuTrabajador()
        elif eleccion == "5":
            actualizarPickle()
            exit()
        else:
            print("Ingreso incorrecto de opcion")
            print("")

trabajofinal = Menu()
