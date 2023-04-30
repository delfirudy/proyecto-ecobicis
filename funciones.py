from clases import *

empresaa = Empresa("Ecobicis")


# DESCRIPCION
# Ingreso todos los datos del cliente
# Se genera la listacliente, con todos los datos sobre el cliente
# Se agrega a clientes la listacliente
def ingresocliente():
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
    clientee = Cliente(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta)
    empresaa.clientes.append(clientee.listacliente)
    print("Ingreso de datos realizado")
    print("")
    texto = ""
    for i in clientee.listacliente:
        texto += str(i) + "\t" 
    f = open("datosclientes.txt","a")
    f.write("\n" + texto)
    f.close()


# DESCRIPCION
# Ingreso todos los datos del trabajador
# Se genera la listatrabajador, con todos los datos sobre el trabajador
# Se agrega a trabajadores la listatrabajador
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
    trabajadorr = Trabajador(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu)
    empresaa.trabajadores.append(trabajadorr.listatrabajador)
    print("Ingreso de datos realizado")
    print("")
    texto = ""
    for i in trabajadorr.listatrabajador:
        texto += str(i) + "\t" 
    f = open("datostrabajadores.txt","a")
    f.write("\n" + texto)
    f.close()


# DESCRIPCION
# Ingreso todos los datos de la estacion
# Se genera la listaestacion, con todos los datos sobre la estacion
# Se agrega a estaciones la listaestacion
def ingresoestacion():
    nombre = input("Ingrese nombre: ")
    direccion = input("Ingrese direccion: ")
    barrio = input("Ingrese barrio: ")
    cantbicitotal = int(input("Ingrese capacidad: "))
    print("")
    estacionn = Estacion(nombre, direccion, barrio, cantbicitotal)
    empresaa.estaciones.append(estacionn.listaestacion)
    print("Ingreso de datos realizado")
    print("")
    texto = ""
    for i in estacionn.listaestacion:
        texto += str(i) + "\t" 
    f = open("datosestaciones.txt","a")
    f.write("\n" + texto)
    f.close()


# DESCRIPCION
# Ingreso todos los datos de la bicicleta
# Si no hay lugar en la estacionactual para guardar la bicicleta se cancela el ingreso y le pide al trabajador que ingrese la bicicleta en otra estacion antes de volver a cargar el ingreso
# Si hay lugar en la estacionactual hace lo siguiente
# Se genera la listabicicleta, con todos los datos sobre la bicicleta
# Se agrega a bicicletas la listabicicleta
# Se suma 1 a la cantidad disponible de bicicletas en la estacionactual
def ingresobicicleta():
    patente = input("Ingrese patente: ")
    modelo = input("Ingrese modelo: ")
    anno = input("Ingrese anno: ")
    estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ")
    print("")
    t = 0
    x = 0
    for i in empresaa.estaciones:
        if i[0] == estacionactual:
            x = 1
            if i[3] == i[4]:
                print("No hay lugar en la estacion, ingrese la bicicleta en otra estacion")
                print("")
            else:
                bicicletaa = Bicicleta(patente, modelo, anno, estacionactual)
                empresaa.bicicletas.append(bicicletaa.listabicicleta)
                i[4] = str(int(i[4]) + 1)
                t = 1
                print("Ingreso de datos realizado")
                print("")
    if x == 0:
        print("No se encontro la estacion")
        print("")
    texto = ""
    if t == 1:
        for i in bicicletaa.listabicicleta:
            texto += str(i) + "\t" 
        f = open("datosbicicletas.txt","a")
        f.write("\n" + texto)
        f.close()


# DESCRIPCION
# Ingreso de los datos necesarios para el alquiler
# Genera codigo del alquiler automaticamente
# Chequea que existan la patente, estacion de llegada y estacion de salida en las listas
# Si no hay lugar en la estacion llegada cancela el alquiler y le pide al cliente que deje la bicicleta en otra estacion antes de volver a cargar el alquiler
# Si hay lugar en la estacion llegada para guardar la bicicleta hace lo siguiente
# Suma 1 a la cantidad de usos de la bicicleta
# Resta 1 a la cantidad disponible de bicicletas en la estacion de salida y suma 1 a la cantidad de bicicletas disponible de la estacion llegada
codigo = 0
def alquilar(usuario):
    global codigo
    patente = input("Ingrese patente de la bicicleta: ")
    fecyhora = input("Ingrese fecha y hora del alquiler: ")
    duracion = input("Ingrese duracion del alquiler: ")
    estacionsalida = input("Ingrese estacion de salida: ")
    estacionllegada = input("Ingrese estacion de llegada: ")
    print("")
    w = 0
    x = 0
    for i in empresaa.estaciones:
        if i[0] == estacionllegada:
            x += 1
    for n in empresaa.estaciones:
        if n[0] == estacionsalida:
            x += 1
    for k in empresaa.bicicletas:
        if k[0] == patente:
            x += 1
    if x == 3:
        for m in empresaa.estaciones:
            if m[0] == estacionllegada:
                if m[3] == m[4]:
                    print("No hay lugar para dejar la bicicleta, dejarla en otra estacion")
                    print("")
                else:
                    codigo += 1
                    alquilerr = Alquiler(usuario,patente,codigo,fecyhora,duracion,estacionsalida,estacionllegada)
                    empresaa.alquileres.append(alquilerr.listaalquiler)
                    m[4] = str(int(m[4]) + 1)
                    for p in empresaa.estaciones:
                        if p[0] == estacionsalida:
                            p[4] = str(int(p[4]) - 1)
                    for q in empresaa.bicicletas:
                        if q[0] == patente:
                            q[4] = str(int(q[4]) + 1)
                            q[3] = estacionllegada
                    w = 1
                    print("Ingreso de alquiler realizado")
                    print("")
    else:
        print("No se encontro patente, estacion de salida o estacion de llegada")
        print("")
    texto = ""
    if w == 1:
        for i in alquilerr.listaalquiler:
            texto += str(i) + "\t" 
        f = open("datosalquileres.txt","a")
        f.write("\n" + texto)
        f.close()


# DESCRIPCION
# Muestra la informacion de las estaciones, con sus bicicletas
def mostrarinfo():
    print(empresaa.estaciones)
    print("")


# DESCRIPCION
# Pide valor actual que se desea cambiar (dato)
# Pide valor nuevo (cambio)
# Realiza el cambio de dato y altera todas las listas que lo tienen.
# Anotacion: Cuando pasemos todo a diccionarios, dato va a ser contrasena, nombre etc. Por ahora es el valor actual
# No se puede cambiar el usuario
def cambiocliente(usuario):
    dato = input("Ingrese dato que desea cambiar: ")
    for i in empresaa.clientes:
        if i[0] == usuario:
            for n in range(1,9):
                if i[n] == dato:
                    cambio = input("Ingrese valor nuevo: ")
                    print("")
                    i[n] = cambio
                    print("Cambio realizado")
                    print("")


# DESCRIPCION
# Pide valor actual que se desea cambiar (dato)
# Pide valor nuevo (cambio)
# Realiza el cambio de dato y altera todas las listas que lo tienen.
# Anotacion: Cuando pasemos todo a diccionarios, dato va a ser contrasena, nombre etc. Por ahora es el valor actual
# No se puede cambiar el usuario
def cambiotrabajador(usuario):
    dato = input("Ingrese que dato quiere cambiar: ")
    for i in empresaa.trabajadores:
        if i[0] == usuario:
            for n in range(1,10):
                if i[n] == dato:
                    cambio = input("Ingrese valor nuevo: ")
                    print("")
                    i[n] = cambio
                    print("Cambio realizado")
                    print("")

def recorrertxt():
    with open("datosclientes.txt") as datosclientes:
        for i, line in enumerate(datosclientes):
            if i == 0:
                continue
            else:
                empresaa.clientes.append(line.strip().split("\t"))
    with open("datostrabajadores.txt") as datostrabajadores:
        for i, line in enumerate(datostrabajadores):
            if i == 0:
                continue
            else:
                empresaa.trabajadores.append(line.strip().split("\t"))
    with open("datosestaciones.txt") as datosestaciones:
        for i, line in enumerate(datosestaciones):
            if i == 0:
                continue
            else:
                empresaa.estaciones.append(line.strip().split("\t"))
    with open("datosbicicletas.txt") as datosbicicletas:
        for i, line in enumerate(datosbicicletas):
            if i == 0:
                continue
            else:
                empresaa.bicicletas.append(line.strip().split("\t"))
    with open("datosalquileres.txt") as datosalquileres:
        for i, line in enumerate(datosalquileres):
            if i == 0:
                continue
            else:
                empresaa.alquileres.append(line.strip().split("\t"))

def actualizartxt():
    for i in range(len(empresaa.clientes)):
        if i == 0:
            texto = ""
            for n in empresaa.clientes[i]:
                texto += str(n) + "\t" 
            f = open("datosclientes.txt","w")
            f.write("\n" + texto)
            f.close()
        else:
            texto = ""
            for n in empresaa.clientes[i]:
                texto += str(n) + "\t" 
            f = open("datosclientes.txt","a")
            f.write("\n" + texto)
            f.close()
    for i in range(len(empresaa.trabajadores)):
        if i ==0:
            texto = ""
            for n in empresaa.trabajadores[i]:
                texto += str(n) + "\t" 
            f = open("datostrabajadores.txt","w")
            f.write("\n" + texto)
            f.close()
        else:
            texto = ""
            for n in empresaa.trabajadores[i]:
                texto += str(n) + "\t" 
            f = open("datostrabajadores.txt","a")
            f.write("\n" + texto)
            f.close()       
    for i in range(len(empresaa.estaciones)):
        if i ==0:
            texto = ""
            for n in empresaa.estaciones[i]:
                texto += str(n) + "\t" 
            f = open("datosestaciones.txt","w")
            f.write("\n" + texto)
            f.close()
        else:
            texto = ""
            for n in empresaa.estaciones[i]:
                texto += str(n) + "\t" 
            f = open("datosestaciones.txt","a")
            f.write("\n" + texto)
            f.close()
    for i in range(len(empresaa.bicicletas)):
        if i ==0: 
            texto = ""
            for n in empresaa.bicicletas[i]:
                texto += str(n) + "\t" 
            f = open("datosbicicletas.txt","w")
            f.write("\n" + texto)
            f.close()
        else:
            texto = ""
            for n in empresaa.bicicletas[i]:
                texto += str(n) + "\t" 
            f = open("datosbicicletas.txt","a")
            f.write("\n" + texto)
            f.close()
    for i in range(len(empresaa.alquileres)):
        if i ==0:
            texto = ""
            for n in empresaa.alquileres[i]:
                texto += str(n) + "\t" 
            f = open("datosalquileres.txt","w")
            f.write("\n" + texto)
            f.close()
        else:
            texto = ""
            for n in empresaa.alquileres[i]:
                texto += str(n) + "\t" 
            f = open("datosalquileres.txt","a")
            f.write("\n" + texto)
            f.close()
