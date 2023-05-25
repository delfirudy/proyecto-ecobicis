from validaciones import *
import pickle

listausuarios = []
listadnis = []
listatarjetas = []
listacbus = []
listanombres = []
listapatentes = []
codigoalquiler = 0


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = []
        self.clientes = []
        self.estaciones = []
        self.bicicletas = []
        self.alquileres = []

empresa = Empresa("Ecobicis")


class Usuario:
    def __init__(self, usuario=0, contrasena=0, nombre=0, dni=0, fecnac=0, telefono=0, mail=0, direccion=0):
        # Ingreso de datos del usuario
        usuario = input("Ingrese usuario: ").strip()
        while validarusuario(usuario, listausuarios) == False:
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
        while validardni(dni, listadnis) == False:
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
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.dni = dni
        self.fecnac = fecnac
        self.telefono = telefono
        self.mail = mail
        self.direccion = direccion
        # Agregado de usuario a la lista de usuarios
        listausuarios.append(usuario)
        # Agregado de dni a la lista de dnis
        listadnis.append(dni)

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion)


class Cliente(Usuario):
    def __init__(self, usuario=0, contrasena=0, nombre=0, dni=0, fecnac=0, telefono=0, mail=0, direccion=0, tarjeta=0):
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        # Ingreso de datos del cliente
        tarjeta = input("Ingrese tarjeta: ").strip()
        while validartarjeta(tarjeta, listatarjetas) == False:
            print("La tarjeta ya existe o el formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
            print("")
            tarjeta = input("Ingrese tarjeta: ").strip()
        self.tarjeta = tarjeta
        # Agregado de tarjeta a la lista de tarjetas
        listatarjetas.append(tarjeta)
        # Agregado de cliente a la lista de clientes
        empresa.clientes.append(self)
        print("")
        print("Cliente ingresado")
        print("")
    
    def alquilar(self):
        global codigoalquiler
        codigoalquiler += codigoalquiler
        # Ingreso de datos del alquiler
        fecha = input("Ingrese fecha del alquiler: ").strip()
        while validarfecha(fecha) == False:
            fecha = input("Ingrese fecha del alquiler: ").strip() 
        duracion = input("Ingrese duracion del alquiler en minutos: ").strip()
        while validarnumero(duracion) == False:
            print("El formato es incorrecto, la duracion debe ser un numero")
            print("")
            duracion = input("Ingrese duracion: ").strip()
        estacionsalida = input("Ingrese estacion de salida: ").strip()
        while validarestacionsalida(estacionsalida, listanombres) == False:
            print("No se encontro la estacion o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionsalida = input("Ingrese estacion de salida: ").strip()
        estacionllegada = input("Ingrese estacion de llegada: ").strip()
        while validarestacionactual(estacionllegada, listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionllegada = input("Ingrese estacion de llegada: ").strip()
        # Agregado de alquiler a la lista de alquileres
        empresa.alquileres.append(Alquiler(self.nombre, codigoalquiler, fecha, duracion, estacionsalida, estacionllegada))
        # Mueve la bicicleta de una estacion a la otra
        # Suma uno a cantusos de la bicicleta
        # Suma uno a cantbicidisponible de la estacion llegada
        # Resta uno a cantbicidisponible de la estacion salida
        for estacion in empresa.estaciones:
            if estacion.nombre == estacionsalida:
                estacion.cantbicidisponible -= 1
            if estacion.nombre == estacionllegada:
                estacion.cantbicidisponible += 1
        for bicicleta in empresa.bicicletas:
            if bicicleta.estacionactual == estacionsalida:
                bicicleta.cantusos += 1
                bicicleta.estacionactual = estacionllegada
                break
        print("")
        print("Alquiler ingresado")
        print("")

    def mostrarinfo(self):
        for estacion in empresa.estaciones:
            print(str(estacion.nombre) + " " + str(estacion.direccion) + " " + str(estacion.barrio) + " " + str(estacion.cantbicitotal) + " " + str(estacion.cantbicidisponible))
            print("")

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nTarjeta: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.tarjeta)


class Trabajador(Usuario):
    def __init__(self, usuario=0, contrasena=0, nombre=0, dni=0, fecnac=0, telefono=0, mail=0, direccion=0, puesto=0, cbu=0):
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        # Ingreso de datos del trabajador
        puesto = input("Ingrese puesto: ").strip()
        while validarpuesto(puesto) == False:
            print("El formato es incorrecto, el puesto debe contener solo letras")
            print("")
            puesto = input("Ingrese puesto: ").strip()
        cbu = input("Ingrese cbu: ").strip()
        while validarcbu(cbu, listacbus) == False:
            print("El cbu ya existe o el formato es incorrecto, el cbu debe ser un numero de 22 digitos")
            print("")
            cbu = input("Ingrese el cbu: ").strip()
        self.puesto = puesto
        self.cbu = cbu
        # Agregado del cbu a la lista de cbus
        listacbus.append(cbu)
        # Agregado de trabajador a la lista de trabajadores
        empresa.trabajadores.append(self)
        print("")
        print("Trabajador ingresado")
        print("")

    def agregarestacion(self):
        # Ingreso de datos de la estacion
        nombre = input("Ingrese nombre: ").strip()
        while validarestacion(nombre, listanombres) == False:
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
        cantbicidisponible = 0
        # Agregado de nombre a la lista de nombres
        listanombres.append(nombre)
        # Agregado de estacion a la lista de estaciones
        empresa.estaciones.append(Estacion(nombre, direccion, barrio, cantbicitotal, cantbicidisponible))
        print("")
        print("Estacion ingresada")
        print("")

    def agregarbicicleta(self):
        # Ingreso de datos de la bicicleta
        patente = input("Ingrese patente: ").strip()
        while validarpatente(patente, listapatentes) == False:
            print("La patente ya existe o el formato es incorrecto, la patente debe ser un numero")
            print("")
            patente = input("Ingrese patente: ").strip()
        modelo = input("Ingrese modelo: ").strip()
        estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
        while validarestacionactual(estacionactual, listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
        cantusos = 0
        # Agregado de patente a la lista de patentes
        listapatentes.append(patente)
        # Agregado de bicicleta a la lista de bicicletas
        empresa.bicicletas.append(Bicicleta(patente, modelo, estacionactual, cantusos))
        # Suma uno a cantbicidiponible de la estacion actual
        for estacion in empresa.estaciones:
            if estacion.nombre == estacionactual:
                estacion.cantbicidisponible += 1
        print("")
        print("Bicicleta ingresada")
        print("")

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nPuesto {} \nCbu: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.puesto, self.cbu)


class Estacion:
    def __init__(self, nombre, direccion, barrio, cantbicitotal, cantbicidisponible):
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.cantbicitotal = cantbicitotal
        self.cantbicidisponible = cantbicidisponible

    def __str__(self):
        return "Nombre: {} \nDireccion: {} \nBarrio: {} \nCantidad maxima de bicicletas: {} \nCantidad disponible de bicicletas: {}".format(self.nombre, self.direccion, self.barrio, self.cantbicitotal, self.cantbicidisponible)


class Bicicleta():
    def __init__(self, patente, modelo, estacionactual, cantusos):
        self.patente = patente
        self.modelo = modelo
        self.estacionactual = estacionactual
        self.cantusos = cantusos
    
    def __str__(self):
        return "Patente: {} \nModelo: {} \nEstacion actual: {} \nCantidad de usos: {}".format(self.patente, self.modelo, self.estacionactual, self.cantusos)


class Alquiler():
    def __init__(self, usuario, codigo, fecha, duracion, estacionsalida, estacionllegada):
        self.usuario = usuario
        self.codigo = codigo
        self.fecha = fecha
        self.duracion = duracion
        self.estacionsalida = estacionsalida
        self.estacionllegada = estacionllegada

    def __str__(self):
        return "Usuario: {} \nCodigo: {} \nFecha: {} \nDuracion: {} \nEstacion salida: {} \nEstacion llegada: {}".format(self.usuario, self.codigo, self.fecha, self.duracion, self.estacionsalida, self.estacionllegada)


def recorrertxt():
    nombrespickle = ["datosclientes.pickle", "datostrabajadores.pickle", "datosestaciones.pickle", "datosbicicletas.pickle", "datosalquileres.pickle"]
    listas = [empresa.clientes, empresa.trabajadores, empresa.estaciones, empresa.bicicletas, empresa.alquileres]
    for nombrepickle, lista in zip(nombrespickle, listas): 
        with open(nombrepickle, "rb") as archivopickle:
            try:
                while True:
                    lista.append(pickle.load(archivopickle))
            except EOFError:
                pass
    for cliente in empresa.clientes:
        listausuarios.append(cliente.nombre)
        listatarjetas.append(cliente.tarjeta)
        listadnis.append(cliente.dni)
    for trabajador in empresa.trabajadores:
        listausuarios.append(trabajador.nombre)
        listacbus.append(trabajador.cbu)
        listadnis.append(trabajador.dni)
    for estacion in empresa.estaciones:
        listanombres.append(estacion.nombre)
    for bicicleta in empresa.bicicletas:
        listapatentes.append(bicicleta.patente)


def actualizartxt():
    nombrespickle = ["datosclientes.pickle", "datostrabajadores.pickle", "datosestaciones.pickle", "datosbicicletas.pickle", "datosalquileres.pickle"]
    listas = [empresa.clientes, empresa.trabajadores, empresa.estaciones, empresa.bicicletas, empresa.alquileres]
    for nombrepickle, lista in zip(nombrespickle, listas):
        with open(nombrepickle, "wb") as archivopickle:
            for objeto in lista:
                pickle.dump(objeto, archivopickle)

