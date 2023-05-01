from clases import *
from validaciones import *

empresaa = Empresa("Ecobicis")

# DESCRIPCION
# Ingreso todos los datos del cliente
# Se validan los datos
# Se genera la listacliente, con todos los datos sobre el cliente
# Se agrega a clientes la listacliente
def ingresocliente():
    usuario = input("Ingrese usuario: ").strip()
    while validarusuario(usuario,empresaa.usuarios) == False:
        print("El usuario ya existe o el formato es incorrecto, el usuario debe contener solo letras")
        print("")
        usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    while validarcontrasena(contrasena) == False:
        print("El formato es incorrecto, la contrasena debe contener solo letras y la primera debe ser mayuscula")
        print("")
        contrasena = input("Ingrese contrasena: ").strip()
    nombre = input("Ingrese nombre: ").strip()
    while validarnombre(nombre) == False:
        print("El formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
        print("")
        nombre = input("Ingrese nombre: ").strip()
    dni = input("Ingrese dni: ").strip()
    while validardni(dni, empresaa.dnis) == False:
        print("El dni ya existe o el formato es incorrecto, debe ser un numero de ocho caracteres")
        print("")
        dni = input("Ingrese dni: ").strip()
    fecnac = input("Ingrese fecha de nacimiento: ").strip() 
    while validarfecha(fecnac) == False:
        fecnac = input("Ingrese fecha de nacimiento: ").strip() 
    telefono = input("Ingrese telefono: ").strip()
    while validartelefono(telefono) == False:
        print("El formato es incorrecto, el telefono debe ser un numero de diez caracteres")
        print("")
        telefono = input("Ingrese telefono: ").strip()
    mail = input("Ingrese mail: ").strip()
    while validarmail(mail) == False:
        print("El formato es incorrecto, el mail debe contener un @")
        print("")
        mail = input("Ingrese mail: ").strip()
    direccion = input("Ingrese direccion: ").strip()
    while validardireccion(direccion) == False:
        print("El formato es incorrecto, la direccion debe tener letras y numeros")
        print("")
        direccion = input("Ingrese direccion: ").strip()
    tarjeta = input("Ingrese tarjeta: ").strip()
    while validartarjeta(tarjeta, empresaa.tarjetas) == False:
        print("El formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
        print("")
        tarjeta = input("Ingrese tarjeta: ").strip()
    print("")
    clientee = Cliente(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta)
    empresaa.clientes.append(clientee.listacliente)
    empresaa.usuarios.append(usuario)
    empresaa.tarjetas.append(tarjeta)
    empresaa.dnis.append(dni)
    print("Ingreso de datos realizado")
    print("")

# DESCRIPCION
# Ingreso todos los datos del trabajador
# Se validan los datos
# Se genera la listatrabajador, con todos los datos sobre el trabajador
# Se agrega a trabajadores la listatrabajador
def ingresotrabajador():
    usuario = input("Ingrese usuario: ").strip()
    while validarusuario(usuario,empresaa.usuarios) == False:
        print("El usuario ya existe o el formato es incorrecto, el usuario debe contener solo letras")
        print("")
        usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    while validarcontrasena(contrasena) == False:
        print("El formato es incorrecto, la contrasena debe contener solo letras y la primera debe ser mayuscula")
        print("")
        contrasena = input("Ingrese contrasena: ").strip()
    nombre = input("Ingrese nombre: ").strip()
    while validarnombre(nombre) == False:
        print("El formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
        print("")
        nombre = input("Ingrese nombre: ").strip()
    dni = input("Ingrese dni: ").strip()
    while validardni(dni, empresaa.dnis) == False:
        print("El dni ya existe o el formato es incorrecto, debe ser un numero de ocho caracteres")
        print("")
        dni = input("Ingrese dni: ").strip()
    fecnac = input("Ingrese fecha de nacimiento: ").strip() 
    while validarfecha(fecnac) == False:
        fecnac = input("Ingrese fecha de nacimiento: ").strip() 
    telefono = input("Ingrese telefono: ").strip()
    while validartelefono(telefono) == False:
        print("El formato es incorrecto, el telefono debe ser un numero de diez caracteres")
        print("")
        telefono = input("Ingrese telefono: ").strip()
    mail = input("Ingrese mail: ").strip()
    while validarmail(mail) == False:
        print("El formato es incorrecto, el mail debe contener un @")
        print("")
        mail = input("Ingrese mail: ").strip()
    direccion = input("Ingrese direccion: ").strip()
    while validardireccion(direccion) == False:
        print("El formato es incorrecto, la direccion debe tener letras y numeros")
        print("")
        direccion = input("Ingrese direccion: ").strip()
    puesto = input("Ingrese puesto: ").strip()
    while validarpuesto(puesto) == False:
        print("El formato es incorrecto, el puesto debe contener solo letras")
        print("")
        puesto = input("Ingrese puesto: ").strip()
    cbu = input("Ingrese cbu: ").strip()
    while validarcbu(cbu,empresaa.cbus) == False:
        print("El formato es incorrecto, el cbu debe ser un numero de 22 digitos")
        print("")
        cbu = input("Ingrese el cbu: ").strip()
    print("")
    trabajadorr = Trabajador(usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu)
    empresaa.trabajadores.append(trabajadorr.listatrabajador)
    empresaa.usuarios.append(usuario)
    empresaa.cbus.append(cbu)
    empresaa.dnis.append(dni)
    print("Ingreso de datos realizado")
    print("")

# DESCRIPCION
# Ingreso todos los datos de la estacion
# Se validan los datos
# Se genera la listaestacion, con todos los datos sobre la estacion
# Se agrega a estaciones la listaestacion
def ingresoestacion():
    nombre = input("Ingrese nombre: ").strip()
    while validarestacion(nombre, empresaa.nombresestaciones) == False:
        print("La estacion ya existe o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
        print("")
        nombre = input("Ingrse nombre: ").strip()
    direccion = input("Ingrese direccion: ").strip()
    while validardireccion(direccion) == False:
        print("El formato es incorrecto, la direccion debe tener letras y numeros")
        print("")
        direccion = input("Ingrese direccion: ").strip()
    barrio = input("Ingrese barrio: ").strip()
    while validarnombre(barrio) == False:
        print("El formato es incorrecto, el barrio debe contener solo letras y la primera debe ser mayuscula")
        print("")
        barrio = input("Ingrese barrio: ").strip()
    cantbicitotal = input("Ingrese capacidad: ").strip()
    while validarnumero(cantbicitotal) == False:
        print("El formato es incorrecto, la capacidad debe ser un numero")
        print("")
        cantbicitotal = input("Ingrese capacidad: ").strip()
    print("")
    estacionn = Estacion(nombre, direccion, barrio, cantbicitotal)
    empresaa.estaciones.append(estacionn.listaestacion)
    empresaa.nombresestaciones.append(nombre)
    print("Ingreso de datos realizado")
    print("")

# DESCRIPCION
# Ingreso todos los datos de la bicicleta
# Se validan los datos
# Si no hay lugar en la estacionactual para guardar la bicicleta se cancela el ingreso y le pide al trabajador que ingrese la bicicleta en otra estacion antes de volver a cargar el ingreso
# Si hay lugar en la estacionactual hace lo siguiente
# Se genera la listabicicleta, con todos los datos sobre la bicicleta
# Se agrega a bicicletas la listabicicleta
# Se suma 1 a la cantidad disponible de bicicletas en la estacionactual
def ingresobicicleta():
    patente = input("Ingrese patente: ").strip()
    while validarpatente(patente, empresaa.patentes) == False:
        print("La patente ya existe o el formato es incorrecto, la patente debe ser un numero")
        print("")
        patente = input("Ingrese patente: ").strip()
    modelo = input("Ingrese modelo: ").strip()
    estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
    while validarestacionactual(estacionactual, empresaa.nombresestaciones, empresaa.estaciones) == False:
        print("No se encontro la estacion o no hay lugar para dejar la bicicleta")
        print("")
        estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
    print("")
    bicicletaa = Bicicleta(patente, modelo, estacionactual)
    empresaa.bicicletas.append(bicicletaa.listabicicleta)
    empresaa.patentes.append(patente)
    print("Ingreso de datos realizado")
    print("")
    for i in empresaa.estaciones:
        if i[0] == estacionactual:
            i[4] = str(int(i[4]) + 1)

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
    fecha = input("Ingrese fecha del alquiler: ").strip()
    while validarfecha(fecha) == False:
        fecha = input("Ingrese fecha del alquiler: ").strip() 
    duracion = input("Ingrese duracion del alquiler en minutos: ").strip()
    while validarnumero(duracion) == False:
        print("El formato es incorrecto, la duracion debe ser un numero")
        print("")
        duracion = input("Ingrese duracion: ").strip()
    estacionsalida = input("Ingrese estacion de salida: ").strip()
    while validarestacion(estacionsalida, empresaa.nombresestaciones) == False:
        print("No se encontro la estacion")
        print("")
        estacionsalida = input("Ingrese estacion de salida: ").strip()
    estacionllegada = input("Ingrese estacion de llegada: ").strip()
    while validarestacion(estacionllegada, empresaa.nombresestaciones) == False:
        print("No se encontro la estacion")
        print("")
        estacionllegada = input("Ingrese estacion de llegada: ").strip()
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

# DESCRIPCION
# Muestra la informacion de las estaciones, con sus bicicletas
def mostrarinfo():
    print(empresaa.estaciones)
    print("")

# DESCRIPCION
# Recorre el txt al inicio de la ejecución para pasar los datos a las listas
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
        empresaa.dnis.append(i[3])
    with open("datostrabajadores.txt") as datostrabajadores:
        for i, line in enumerate(datostrabajadores):
            if i == 0:
                continue
            else:
                empresaa.trabajadores.append(line.strip().split("\t"))
    for i in empresaa.trabajadores:
        empresaa.usuarios.append(i[0])
        empresaa.cbus.append(i[9])
        empresaa.dnis.append(i[3])
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

# DESCRIPCION
# Actualiza el txt al cerrar el código
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
