from clases import *
from datetime import datetime, date

empresaa = Empresa("Ecobicis")


# DESCRIPCION
# Ingreso todos los datos del cliente
# Se genera la listacliente, con todos los datos sobre el cliente
# Se agrega a clientes la listacliente
def ingresocliente():

# ######################################## HAY QUE VER SI ESTO FUNCIONA 
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    for cliente in empresaa.clientes:
        if nombre_usuario == cliente[0]:
            nombre_usuario = input("Este nombre de usuario ya existe. Por favor, ingrese otro nombre de usuario: ")
    usuario = nombre_usuario 
    print("El nombre de usuario", nombre_usuario, "ha sido registrado exitosamente")


    
    contrasenaa = input("Ingrese contrasena con caracteres especiales, alfabeticos y digitos con la primera letra mayuscula: ")
    if contrasenaa.isalpha() and contrasenaa.isdigit() and contrasenaa.isspace() and contrasenaa[0].isupper():
         contrasena= contrasenaa
    else: 
        contrasenaa = input("Ingrese contrasena correcta : ")

    nombre = input("Ingrese nombre: ")
  
    dni1 = input("ingrese dni:")
    while len(dni1)!=8 or not dni1.isdigit():
        dni1=input("Ingrese dni nuevamente") 
    dni = dni1
    
    #fecnac
    while True:
        fecha = input("Ingrese una fecha en formato YYYY/MM/DD: ")

        try:
            fecha_valida = datetime.strptime(fecha, "%Y/%m/%d").date()
            fecha_actual = date.today()
            if fecha_valida < fecha_actual:
                print("La fecha ingresada es:", fecha_valida)
                fecnac = fecha_valida
                break
            else:
                print("La fecha es válida pero no es anterior a la fecha actual.")
                continue
        except ValueError:
            print("La fecha no tiene el formato esperado. Ingrese la fecha nuevamente.")
            continue

    #Telefono
    tel = input("Ingrese numero de telefono: ")
    while len(tel) != 8 or not tel.isdigit():
        tel = input("Ingrese nuevamente el telefono (debe tener 8 dígitos): ")
        telefono = tel

    #Mail
    maill = input("Ingrese correo electronico:")
    while "@" not in maill: 
        maill = input("Ingrese nuevamente el correo electronico (debe contener @)")
        mail = maill

    #Tarjeta
    tarjeta1 = input("Ingrese numero de tarjeta:")
    while len(tarjeta1.replace(" ", "")) != 16 or not tarjeta1.isdigit():
        tarjeta1 = input("Ingrese nuevamente:")
        tarjeta = tarjeta1

    direccion = input("Ingrese direccion: ")
    print("")
    clientee = Cliente(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta)
    empresaa.clientes.append(clientee.listacliente)
    print("Ingreso de datos realizado")
    print("")
    texto = ""
    for i in clientee.listacliente:
        texto += " " + str(i)
    with open("./datosclientes.txt", "a", encoding= "utf-8") as f:
        f.write("\n" + texto)


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
        texto += " " + str(i)
    with open("./datostrabajadores.txt", "a", encoding= "utf-8") as f:
        f.write("\n" + texto)


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
        texto += " " + str(i)
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
                i[4] += 1
                print("Ingreso de datos realizado")
                print("")
    if x == 0:
        print("No se encontro la estacion")
        print("")
    texto = ""
    for i in bicicletaa.listabicicleta:
        texto += " " + str(i)
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
    x = 0
    for i in empresaa.estaciones:
        if i[0] == estacionllegada:
            x = 1
    for n in empresaa.estaciones:
        if n[0] == estacionsalida:
            x = 2
    for k in empresaa.bicicletas:
        if k[0] == patente:
            x = 3
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
                    m[4] += 1
                    for p in empresaa.estaciones:
                        if p[0] == estacionsalida:
                            p[4] -= 1
                    print("Ingreso de alquiler realizado")
                    print("")
    else:
        print("No se encontro patente, estacion de salida o estacion de llegada")
        print("")
    texto = ""
    for i in alquilerr.listaalquiler:
        texto += " " + str(i)
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