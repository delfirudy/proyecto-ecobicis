from clases_funciones import *

class Submenutrabajador:
    usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    while validarpersona(usuario, contrasena, empresa.trabajadores) == False:
        print("Trabajador no encontrado")
        print("")
        usuario = input("Ingrese usuario: ").strip()
        contrasena = input("Ingrese contrasena: ").strip()
    trabajador = empresa.trabajadores.get(usuario + contrasena)
    print("Trabajador validado")
    print("")
    seguir1 = True
    while seguir1 == True:
        print("1. Ingresar estacion")
        print("2. Ingresar bicicleta")
        print("3. Volver al menu principal")
        print("")
        elecciontrabajador = input("Ingrese opcion: ").strip()
        print("")
        if elecciontrabajador == "1":
            trabajador.agregarestacion()
        elif elecciontrabajador == "2":
            trabajador.agregarbicicleta()
        elif elecciontrabajador == "3":
            seguir1 = False
        else:
            print("Ingreso incorrecto de opcion")
            print("")

class Submenucliente:
    usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    while validarpersona(usuario, contrasena, empresa.clientes) == False:
        print("Cliente no encontrado")
        print("")
        usuario = input("Ingrese usuario: ").strip()
        contrasena = input("Ingrese contrasena: ").strip()
    cliente = empresa.clientes.get(usuario + contrasena)
    print("Cliente validado")
    print("")
    seguir2 = True
    while seguir2 == True:
        print("1. Alquilar")
        print("2. Información sobre estaciones")
        print("3. Volver al menu principal")
        print("")
        eleccionusuario = input("Ingrese opcion: ").strip()
        print("")
        if eleccionusuario == "1":
            cliente.alquilar()
        elif eleccionusuario == "2":
            cliente.mostrarinfo()
        elif eleccionusuario == "3":
            seguir2 = False
        else:
            print("Ingreso incorrecto de opcion")
            print("")

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
            Submenucliente()
        elif eleccion == "4":
            Submenutrabajador()
        elif eleccion == "5":
            actualizarpickle()
            exit()
        else:
            print("Ingreso incorrecto de opcion")
            print("")

trabajofinal = Menu()
