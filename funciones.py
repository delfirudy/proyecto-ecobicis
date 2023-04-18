from clases import *

empresaa = empresa("Ecobicis")

def ingresousuario():
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contrasena: ")
    nombre = input("Ingrese nombre: ")
    dni = input("Ingrese dni: ")
    fecnac = input("Ingrese fecha de nacimiento: ")
    telefono = input("Ingrese telefono: ")
    mail = input("Ingrese mail: ")
    direccion = input("Ingrese direccion: ")
    tarjeta = input("Ingrese tarjeta: ")
    print("")
    usuarioo = cliente(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta)
    empresaa.clientes.append(usuarioo.listausuario)
    print("Ingreso de datos realizado")
    print("")


def ingresotrabajador():
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contrasena: ")
    nombre = input("Ingrese nombre: ")
    dni = input("Ingrese dni: ")
    fecnac = input("Ingrese fecha de nacimiento: ")
    telefono = input("Ingrese telefono: ")
    mail = input("Ingrese mail: ")
    direccion = input("Ingrese direccion: ")
    puesto = input("Ingrese puesto: ")
    cbu = input("Ingrese cbu: ")
    print("")
    trabajadorr = trabajador(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu)
    empresaa.trabajadores.append(trabajadorr.listatrabajador)
    print("Ingreso de datos realizado")
    print("")

x = 0
def validacionusuario(usuario,contrasena):
    global x
    for i in empresaa.clientes:
        if i[0] == usuario and i[1] == contrasena:
            x = 1
            print("Cliente validado")
            print("")
            

def alquilar():
    pass

# Anotacion: Cuando pasemos todo a diccionarios, dato va a ser usuario, contrasena, nombre etc
# Por ahora es el valor actual
def cambiousuario(dato,usuario):
    for i in empresaa.clientes:
        if i[0] == usuario:
            for n in range(9):
                if i[n] == dato:
                    cambio = input("Ingrese valor nuevo: ")
                    print("")
                    i[n] = cambio
                    print("Cambio realizado")
                    print("")


def mostrarinfo():
    print(empresaa.estaciones)
    print("")

y = 0
def validaciontrabajador(usuario,contrasena):
    global y
    for i in empresaa.trabajadores:
        if i[0] == usuario and i[1] == contrasena:
            y = 1
            print("Trabajador validado")
            print("")


def ingresoestacion():
    nombre = input("Ingrese nombre: ")
    direccion = input("Ingrese direccion: ")
    barrio = input("Ingrese barrio: ")
    cantbicitotal = input("Ingrese capacidad: ")
    print("")
    estacionn = estacion(nombre, direccion, barrio, cantbicitotal)
    empresaa.estaciones.append(estacionn.listaestacion)
    print("Ingreso de datos realizado")
    print("")


def ingresobicicleta():
    patente = input("Ingrese patente: ")
    modelo = input("Ingrese modelo: ")
    anno = input("Ingrese anno: ")
    print("")
    bicicletaa = bicicleta(patente, modelo, anno)
    empresaa.bicicletas.append(bicicletaa.listabicicleta)
    print("Ingreso de datos realizado")
    print("")

# Anotacion: Cuando pasemos todo a diccionarios, dato va a ser usuario, contrasena, nombre etc
# Por ahora es el valor actual
def cambiotrabajador(dato,usuario):
    for i in empresaa.trabajadores:
        if i[0] == usuario:
            for n in range(10):
                if i[n] == dato:
                    cambio = input("Ingrese valor nuevo: ")
                    print("")
                    i[n] = cambio
                    print("Cambio realizado")
                    print("")