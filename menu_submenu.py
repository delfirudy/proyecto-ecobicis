from clase_usuario import *
from clase_alquiler import *
from clase_estacion import *
from clase_bicicleta import *

def submenucambio(trabajador):
    seguir3 = True
    while seguir3 == True:
        print("1. Cambiar datos trabajador")
        print("2. Cambiar datos bicicleta")
        print("3. Cambiar datos estacion")
        print("4. Volver a opciones trabajador")
        print("")
        eleccioncambio = input("Ingrese opcion: ")
        print("")
        if eleccioncambio == "1":
            trabajador.cambio()
        elif eleccioncambio == "2":
            patente = input("Ingrese la patente de la bicicleta a modificar: ")
            while validarPatente(patente, listapatentes) == True:
                print("Patente no encontrada")
                print("")
                patente = input("Ingrese bicicleta a modificar: ")
            bicicleta = empresa.bicicletas.get(patente)
            bicicleta.cambio()
        elif eleccioncambio == "3":
            nombre = input("Ingrese el nombre de la estacion a modificar: ")
            while validarEstacion(nombre, listanombres) == True:
                print("Estacion no encontrada")
                print("")
                nombre = input("Ingrese el nombre de la estacion a modificar: ")
            estacion = empresa.estaciones.get(nombre)
            estacion.cambio()
        elif eleccioncambio == "4":
            seguir3 = False
        else:
            print("Ingreso incorrecto de opcion")
            print("")


def submenueliminar(trabajador):
    seguir4 = True
    while seguir4 == True:
        print("1. Eliminar trabajador")
        print("2. Eliminar bicicleta")
        print("3. Eliminar estacion")
        print("4. Volver a opciones trabajador")
        print("")
        eleccioneliminar = input("Ingrese opcion: ")
        print("")
        if eleccioneliminar == "1":
            trabajador.eliminar()
            seguir4 = False
        elif eleccioneliminar == "2":
            patente = input("Ingrese la patente de la bicicleta a eliminar: ")
            while validarPatente(patente, listapatentes) == True:
                print("Patente no encontrada")
                print("")
                patente = input("Ingrese bicicleta a eliminar: ")
            bicicleta = empresa.bicicletas.get(patente)
            bicicleta.eliminar()
        elif eleccioneliminar == "3":
            nombre = input("Ingrese el nombre de la estacion a eliminar: ")
            while validarEstacion(nombre, listanombres) == True:
                print("Estacion no encontrada")
                print("")
                nombre = input("Ingrese el nombre de la estacion a eliminar: ")
            estacion = empresa.estaciones.get(nombre)
            estacion.eliminar()
        elif eleccioneliminar == "4":
            seguir4 = False
        else:
            print("Ingreso incorrecto de opcion")
            print("")

def submenutrabajador():
    usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    while validarPersona(usuario, contrasena, empresa.trabajadores) == False:
        print("Trabajador no encontrado")
        print("")
        usuario = input("Ingrese usuario: ").strip()
        contrasena = input("Ingrese contrasena: ").strip()
    trabajador = empresa.trabajadores.get(usuario + contrasena)
    print("")
    print("Trabajador validado")
    print("")
    seguir1 = True
    while seguir1 == True:
        print("1. Ingresar estacion")
        print("2. Ingresar bicicleta")
        print("3. Cambiar datos")
        print("4. Dar de baja")
        print("5. Volver al menu principal")
        print("")
        elecciontrabajador = input("Ingrese opcion: ").strip()
        print("")
        if elecciontrabajador == "1":
            trabajador.agregarestacion()
        elif elecciontrabajador == "2":
            trabajador.agregarbicicleta()
        elif elecciontrabajador == "3":
            submenucambio(trabajador)
        elif elecciontrabajador == "4":
            submenueliminar(trabajador)
        elif elecciontrabajador == "5":
            seguir1 = False
        else:
            print("Ingreso incorrecto de opcion")
            print("")

def subMenuCliente():
    usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    while validarPersona(usuario, contrasena, empresa.clientes) == False:
        print("Cliente no encontrado")
        print("")
        usuario = input("Ingrese usuario: ").strip()
        contrasena = input("Ingrese contrasena: ").strip()
    cliente = empresa.clientes.get(usuario + contrasena)
    print("")
    print("Cliente validado")
    print("")
    seguir2 = True
    while seguir2 == True:
        print("1. Alquilar")
        print("2. Información sobre estaciones")
        print("3. Cambiar datos")
        print("4. Dar de baja")
        print("5. Volver al menu principal")
        print("")
        eleccionusuario = input("Ingrese opcion: ").strip()
        print("")
        if eleccionusuario == "1":
            cliente.alquilar()
        elif eleccionusuario == "2":
            cliente.mostrarinfo()
        elif eleccionusuario == "3":
            cliente.cambio()
        elif eleccionusuario == "4":
            cliente.eliminar()
            seguir2 = False
        elif eleccionusuario == "5":
            seguir2 = False
        else:
            print("Ingreso incorrecto de opcion")
            print("")

