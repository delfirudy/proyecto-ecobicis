from clases import *

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
        print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
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
# FALTAAAAA

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
    while validarestacionsalida(estacionsalida, empresaa.nombresestaciones) == False:
        print("No se encontro la estacion o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
        print("")
        estacionsalida = input("Ingrese estacion de salida: ").strip()
    estacionllegada = input("Ingrese estacion de llegada: ").strip()
    while validarestacionactual(estacionllegada, empresaa.nombresestaciones, empresaa.estaciones) == False:
        print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
        print("")
        estacionllegada = input("Ingrese estacion de llegada: ").strip()
    print("")
    codigo += 1
    alquilerr = Alquiler(usuario, codigo, fecha, duracion, estacionsalida, estacionllegada)
    empresaa.alquileres.append(alquilerr.listaalquiler)
    print("Ingreso de alquiler realizado")
    print("")
    for p in empresaa.estaciones:
        if p[0] == estacionsalida:
            p[4] = str(int(p[4]) - 1)
        if p[0] == estacionllegada:
            p[4] = str(int(p[4]) + 1)
    for q in empresaa.bicicletas:
        if q[2] == estacionsalida: 
            q[3] = str(int(q[3]) + 1)
            q[2] = estacionllegada
            break
# CODIGO

# DESCRIPCION
# Muestra la informacion de las estaciones, con sus bicicletas
def mostrarinfo():
    print(empresaa.estaciones)
    print("")

def recorrertxt():
    nombrestxt = ["datosclientes.txt", "datostrabajadores.txt", "datosestaciones.txt", "datosbicicletas.txt", "datosalquileres.txt"]
    listas = [empresaa.clientes, empresaa.trabajadores, empresaa.estaciones, empresaa.bicicletas, empresaa.alquileres]
    for n, p in zip(nombrestxt, listas): 
        with open(n) as nombrepy:
            for i, line in enumerate(nombrepy):
                if i == 0:
                    continue
                else:
                    p.append(line.strip().split("\t"))
    for i in empresaa.clientes:
        empresaa.usuarios.append(i[0])
        empresaa.tarjetas.append(i[8])
        empresaa.dnis.append(i[3])
    for i in empresaa.trabajadores:
        empresaa.usuarios.append(i[0])
        empresaa.cbus.append(i[9])
        empresaa.dnis.append(i[3])
    for i in empresaa.estaciones:
        empresaa.nombresestaciones.append(i[0])
    for i in empresaa.bicicletas:
        empresaa.patentes.append(i[0])

def actualizartxt():
    nombrestxt = ["datosclientes.txt", "datostrabajadores.txt", "datosestaciones.txt", "datosbicicletas.txt", "datosalquileres.txt"]
    listas = [empresaa.clientes, empresaa.trabajadores, empresaa.estaciones, empresaa.bicicletas, empresaa.alquileres]
    for t, p in zip(nombrestxt, listas): 
        for i in range(len(p)):
            if i == 0:
                texto = ""
                for n in p[i]:
                    texto += str(n) + "\t"
                f = open(t,"w")
                f.write("\n" + texto)
                f.close()
            else:
                texto = ""
                for n in p[i]:
                    texto += str(n) + "\t" 
                f = open(t,"a")
                f.write("\n" + texto)
                f.close()
