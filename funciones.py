from clases import *
from datetime import datetime
from datetime import date

empresaa = Empresa("Ecobicis")

# DESCRIPCION
# Ingreso todos los datos del cliente
# Se validan los datos
# Se genera la listacliente, con todos los datos sobre el cliente
# Se agrega a clientes la listacliente
def ingresocliente():
    usuario = input("Ingrese usuario: ")
    while usuario.isalpha() == False or usuario in empresaa.usuarios:
        print("El usuario ya existe o ingresó caracteres numericos, el usuario debe contener solo letras")
        print("")
        usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contrasena: ")
    while contrasena.isalpha() == False or contrasena[0].isupper() == False:
        print("La contrasena debe contener solo letras y la primera debe ser mayuscula")
        print("")
        contrasena = input("Ingrese contrasena: ")
    nombre = input("Ingrese nombre: ")
    while nombre.isalpha() == False or nombre[0].isupper() == False:
        print("El nombre debe contener solo letras y la primera debe ser mayuscula")
        print("")
        nombre = input("Ingrese nombre: ")
    dni = input("Ingrese dni: ")
    while dni.isdigit() == False or len(dni) != 8:
        print("El dni debe ser un numero de ocho caracteres")
        print("")
        dni = input("Ingrese dni: ")
    while True:
        fecha = input("Ingrese una fecha en formato YYYY/MM/DD: ")
        try:
            fecha_valida = datetime.strptime(fecha, "%Y/%m/%d").date()
            fecha_actual = date.today()
            if fecha_valida < fecha_actual:
                fecnac = fecha_valida
                break
            else:
                print("La fecha es válida pero no es anterior a la fecha actual")
                print("")
                continue
        except ValueError:
            print("La fecha no tiene el formato esperado")
            print("")
            continue
    telefono = input("Ingrese telefono: ")
    while telefono.isdigit() == False or len(telefono) != 10:
        print("El telefono debe ser un numero de diez caracteres")
        print("")
        telefono = input("Ingrese telefono: ")
    mail = input("Ingrese mail: ")
    while "@" not in mail:
        print("El mail debe contener un @")
        print("")
        mail = input("Ingrese mail: ")
    direccion = input("Ingrese direccion: ")
    while direccion.isdigit() == True or direccion.isalpha() == True:
        print("La direccion debe tener letras y numeros")
        print("")
        direccion = input("Ingrese direccion: ")
    tarjeta = input("Ingrese tarjeta: ")
    while tarjeta.isdigit() == False or len(tarjeta) != 16:
        print("La tarjeta debe ser un numero de 16 digitos")
        print("")
        tarjeta = input("Ingrese tarjeta: ")
    print("")
    clientee = Cliente(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta)
    empresaa.clientes.append(clientee.listacliente)
    empresaa.usuarios.append(usuario)
    empresaa.tarjetas.append(tarjeta)
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
# Se validan los datos
# Se genera la listatrabajador, con todos los datos sobre el trabajador
# Se agrega a trabajadores la listatrabajador
def ingresotrabajador():
    usuario = input("Ingrese usuario: ")
    while usuario.isalpha() == False or usuario in empresaa.usuarios:
        print("El usuario ya existe o ingresó caracteres numericos, el usuario debe contener solo letras")
        print("")
        usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contrasena: ")
    while contrasena.isalpha() == False or contrasena[0].isupper() == False:
        print("La contrasena debe contener solo letras y la primera debe ser mayuscula")
        print("")
        contrasena = input("Ingrese contrasena: ")
    nombre = input("Ingrese nombre: ")
    while nombre.isalpha() == False or nombre[0].isupper() == False:
        print("El nombre debe contener solo letras y la primera debe ser mayuscula")
        print("")
        nombre = input("Ingrese nombre: ")
    dni = input("Ingrese dni: ")
    while dni.isdigit() == False or len(dni) != 8:
        print("El dni debe ser un numero de ocho caracteres")
        print("")
        dni = input("Ingrese dni: ")
    while True:
        fecha = input("Ingrese una fecha en formato YYYY/MM/DD: ")
        try:
            fecha_valida = datetime.strptime(fecha, "%Y/%m/%d").date()
            fecha_actual = date.today()
            if fecha_valida < fecha_actual:
                fecnac = fecha_valida
                break
            else:
                print("La fecha es válida pero no es anterior a la fecha actual")
                print("")
                continue
        except ValueError:
            print("La fecha no tiene el formato esperado")
            print("")
            continue
    telefono = input("Ingrese telefono: ")
    while telefono.isdigit() == False or len(telefono) != 10:
        print("El telefono debe ser un numero de diez caracteres")
        print("")
        telefono = input("Ingrese telefono: ")
    mail = input("Ingrese mail: ")
    while "@" not in mail:
        print("El mail debe contener un @")
        print("")
        mail = input("Ingrese mail: ")
    direccion = input("Ingrese direccion: ")
    while direccion.isdigit() == True or direccion.isalpha() == True:
        print("La direccion debe tener letras y numeros")
        print("")
        direccion = input("Ingrese direccion: ")
    puesto = input("Ingrese puesto: ")
    while puesto.isalpha() == False:
        print("El puesto debe contener solo letras")
        print("")
        puesto = input("Ingrese puesto: ")
    cbu = input("Ingrese cbu: ")
    while cbu.isdigit() == False or len(cbu) != 22:
        print("El cb debe ser un numero de 22 digitos")
        print("")
        cbu = input("Ingrese el cbu: ")
    print("")
    trabajadorr = Trabajador(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu)
    empresaa.trabajadores.append(trabajadorr.listatrabajador)
    empresaa.usuarios.append(usuario)
    empresaa.cbus.append(cbu)
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
# Se validan los datos
# Se genera la listaestacion, con todos los datos sobre la estacion
# Se agrega a estaciones la listaestacion
def ingresoestacion():
    nombre = input("Ingrese nombre: ")
    while nombre.isalpha() == False or nombre in empresaa.nombresestaciones:
        print("La estacion ya existe o ingresó caracteres numericos, el nombre debe contener solo letras")
        print("")
        nombre = input("Ingrse nombre: ")
    direccion = input("Ingrese direccion: ")
    while direccion.isdigit() == True or direccion.isalpha() == True:
        print("La direccion debe tener letras y numeros")
        print("")
        direccion = input("Ingrese direccion: ")
    barrio = input("Ingrese barrio: ")
    while barrio.isalpha() == False:
        print("El barrio debe contener solo letras")
        print("")
        barrio = input("Ingrese barrio: ")
    cantbicitotal = input("Ingrese capacidad: ")
    while cantbicitotal.isdigit() == False:
        print("La capacidad debe ser un numero")
        print("")
        cantbicitotal = input("Ingrese capacidad: ")
    print("")
    estacionn = Estacion(nombre, direccion, barrio, cantbicitotal)
    empresaa.estaciones.append(estacionn.listaestacion)
    empresaa.nombresestaciones.append(nombre)
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
# Se validan los datos
# Si no hay lugar en la estacionactual para guardar la bicicleta se cancela el ingreso y le pide al trabajador que ingrese la bicicleta en otra estacion antes de volver a cargar el ingreso
# Si hay lugar en la estacionactual hace lo siguiente
# Se genera la listabicicleta, con todos los datos sobre la bicicleta
# Se agrega a bicicletas la listabicicleta
# Se suma 1 a la cantidad disponible de bicicletas en la estacionactual
def ingresobicicleta():
    patente = input("Ingrese patente: ")
    while patente.isdigit() == False or patente in empresaa.patentes:
        print("La patente ya existe o ingresó una letra, la patente debe ser un numero")
        print("")
        patente = input("Ingrese patente: ")
    modelo = input("Ingrese modelo: ")
    estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ")
    while estacionactual not in empresaa.nombresestaciones:
        print("No se encontro la estacion")
        print("")
        estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ")
    print("")
    for i in empresaa.estaciones:
        if i[0] == estacionactual:
            if i[3] == i[4]:
                print("No hay lugar en la estacion, ingrese la bicicleta en otra estacion")
                print("")
            else:
                bicicletaa = Bicicleta(patente, modelo, estacionactual)
                empresaa.bicicletas.append(bicicletaa.listabicicleta)
                empresaa.patentes.append(patente)
                i[4] = str(int(i[4]) + 1)
                print("Ingreso de datos realizado")
                print("")
                texto = ""
                for i in bicicletaa.listabicicleta:
                    texto += str(i) + "\t" 
                f = open("datosbicicletas.txt","a")
                f.write("\n" + texto)
                f.close()
        break

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
    while True:
        fechaa = input("Ingrese fecha del alquiler en formato YYYY/MM/DD: ")
        try:
            fecha_valida = datetime.strptime(fechaa, "%Y/%m/%d").date()
            fecha_actual = date.today()
            if fecha_valida < fecha_actual:
                fecha = fecha_valida
                break
            else:
                print("La fecha es válida pero no es anterior a la fecha actual")
                print("")
                continue
        except ValueError:
            print("La fecha no tiene el formato esperado")
            print("")
            continue
    duracion = input("Ingrese duracion del alquiler en minutos: ")
    while duracion.isdigit() == False:
        print("La duracion debe ser un numero")
        print("")
        duracion = input("Ingrese duracion: ")
    estacionsalida = input("Ingrese estacion de salida: ")
    while estacionsalida not in empresaa.nombresestaciones:
        print("No se encontro la estacion")
        print("")
        estacionsalida = input("Ingrese estacion de salida: ")
    estacionllegada = input("Ingrese estacion de llegada: ")
    while estacionllegada not in empresaa.nombresestaciones:
        print("No se encontro la estacion")
        print("")
        estacionllegada = input("Ingrese estacion de llegada: ")
    print("")
    for m in empresaa.estaciones:
        if m[0] == estacionllegada:
            if m[3] == m[4]:
                print("No hay lugar para dejar la bicicleta, dejarla en otra estacion")
                print("")
            else:
                codigo += 1
                alquilerr = Alquiler(usuario, codigo, fecha, duracion, estacionsalida, estacionllegada)
                empresaa.alquileres.append(alquilerr.listaalquiler)
                m[4] = str(int(m[4]) + 1)
                for p in empresaa.estaciones:
                    if p[0] == estacionsalida:
                        p[4] = str(int(p[4]) - 1)
                for q in empresaa.bicicletas:
                    if q[2] == estacionsalida: 
                        q[3] = str(int(q[3]) + 1)
                        q[2] = estacionllegada
                        break
                print("Ingreso de alquiler realizado")
                print("")
                texto = ""
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
    r = 0
    for i in empresaa.clientes:
        if i[0] == usuario:
            for n in range(1,9):
                if i[n] == dato:
                    cambio = input("Ingrese valor nuevo: ")
                    print("")
                    i[n] = cambio
                    print("Cambio realizado")
                    print("")
                    r = 1
    if r == 0:
        print("No se encontro el dato que desea cambiar")
        print("")


# DESCRIPCION
# Pide valor actual que se desea cambiar (dato)
# Pide valor nuevo (cambio)
# Realiza el cambio de dato y altera todas las listas que lo tienen.
# Anotacion: Cuando pasemos todo a diccionarios, dato va a ser contrasena, nombre etc. Por ahora es el valor actual
# No se puede cambiar el usuario
def cambiotrabajador(usuario):
    dato = input("Ingrese que dato quiere cambiar: ")
    t = 0
    for i in empresaa.trabajadores:
        if i[0] == usuario:
            for n in range(1,10):
                if i[n] == dato:
                    cambio = input("Ingrese valor nuevo: ")
                    print("")
                    i[n] = cambio
                    print("Cambio realizado")
                    print("")
                    t = 1
    if t == 0:
        print("No se encontro el dato que desea cambiar")
        print("") 

def recorrertxt():
    with open("datosclientes.txt") as datosclientes:
        for i, line in enumerate(datosclientes):
            if i == 0:
                continue
            else:
                empresaa.clientes.append(line.strip().split("\t"))
    for i in empresaa.clientes:
        empresaa.usuarios.append(i[0])
        empresaa.tarjetas.append(i[8])
    with open("datostrabajadores.txt") as datostrabajadores:
        for i, line in enumerate(datostrabajadores):
            if i == 0:
                continue
            else:
                empresaa.trabajadores.append(line.strip().split("\t"))
    for i in empresaa.trabajadores:
        empresaa.usuarios.append(i[0])
        empresaa.cbus.append(i[9])
    with open("datosestaciones.txt") as datosestaciones:
        for i, line in enumerate(datosestaciones):
            if i == 0:
                continue
            else:
                empresaa.estaciones.append(line.strip().split("\t"))
    for i in empresaa.estaciones:
        empresaa.nombresestaciones.append(i[0])
    with open("datosbicicletas.txt") as datosbicicletas:
        for i, line in enumerate(datosbicicletas):
            if i == 0:
                continue
            else:
                empresaa.bicicletas.append(line.strip().split("\t"))
    for i in empresaa.bicicletas:
        empresaa.patentes.append(i[0])
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
