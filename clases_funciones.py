from validaciones import *
import pickle

listausuarios = []
listadnis = []
listatarjetas =[]
listacbus = []
listanombres = []
listapatentes = []


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = {}
        self.clientes = {}
        self.estaciones = {}
        self.bicicletas = {}
        self.alquileres = {}

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
        self.id = usuario + contrasena
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
        # Agregado de cliente al diccionario de clientes
        empresa.clientes[self.id] = self
        print("")
        print("Cliente ingresado")
        print("")

    def cambio(self):
        pass

    def eliminar(self):
        empresa.clientes.pop(self.usuario + self.contrasena)
        listadnis.remove(self.dni)
        listatarjetas.remove(self.tarjeta)
        print("")
        print("Cliente eliminado")
        print("")
    
    def alquilar(self):
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
        while validarestacionsalida(estacionsalida, listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay bicicletas o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionsalida = input("Ingrese estacion de salida: ").strip()
        estacionllegada = input("Ingrese estacion de llegada: ").strip()
        while validarestacionactual(estacionllegada, listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionllegada = input("Ingrese estacion de llegada: ").strip()
        # Agregado de alquiler al diccionario de alquileres
        empresa.alquileres[(Alquiler.id)] = Alquiler(self.nombre, fecha, duracion, estacionsalida, estacionllegada)
        # Resta uno a cantbicidisponible de la estacion salida
        try:
            estacion = empresa.estaciones.get(estacionsalida)
            estacion.cantbicidisponible -= 1
        except KeyError:
            print("No se encontro la estacion")
        except:
            print("Error")
        # Suma uno a cantbicidisponible de la estacion llegada 
        try:
            estacion = empresa.estaciones.get(estacionllegada)
            estacion.cantbicidisponible += 1
        except KeyError:
            print("No se encontro la estacion")
        except:
            print("Error")
        # Mueve la bicicleta de una estacion a la otra
        # Suma uno a cantusos de la bicicleta
        for bicicleta in empresa.bicicletas.values():
            if bicicleta.estacionactual == estacionsalida:
                bicicleta.cantusos += 1
                bicicleta.estacionactual = estacionllegada
                break
        print("")
        print("Alquiler ingresado")
        print("")

    def mostrarinfo(self):
        for estacion in empresa.estaciones.values():
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
        # Agregado de trabajador al diccionario de trabajadores
        empresa.trabajadores[self.id] = self
        print("")
        print("Trabajador ingresado")
        print("")

    def cambio(self):
        pass

    def eliminar(self):
        empresa.trabajadores.pop(self.usuario + self.contrasena)
        listacbus.remove(self.cbu)
        listadnis.remove(self.dni)
        print("")
        print("Trabajador eliminado")
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
        # Agregado de estacion al diccionario de estaciones
        empresa.estaciones[nombre] = Estacion(nombre, direccion, barrio, cantbicitotal, cantbicidisponible)
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
        # Agregado de bicicleta al diccionario de bicicletas
        empresa.bicicletas[patente] = Bicicleta(patente, modelo, estacionactual, cantusos)
        # Suma uno a cantbicidiponible de la estacion actual
        try:
            estacion = empresa.estaciones.get(estacionactual)
            estacion.cantbicidisponible += 1
        except KeyError:
            print("No se encontro la estacion")
        except:
            print("Error")
        print("")
        print("Bicicleta ingresada")
        print("")

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nPuesto {} \nCbu: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.puesto, self.cbu)


class Estacion:
    def __init__(self, nombre, direccion, barrio, cantbicitotal, cantbicidisponible):
        self.id = nombre
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.cantbicitotal = cantbicitotal
        self.cantbicidisponible = cantbicidisponible

    def cambio(self):
        pass

    def eliminar(self):
        empresa.estaciones.pop(self.nombre)
        for bicicleta in empresa.bicicletas.values():
            if bicicleta.estacionactual == self.nombre:
                empresa.bicicletas.pop(bicicleta.patente)
        listanombres.pop(self.nombre)
        print("")
        print("Estacion eliminada, reingrese las bicicletas en otra estacion")
        print("")

    def __str__(self):
        return "Nombre: {} \nDireccion: {} \nBarrio: {} \nCantidad maxima de bicicletas: {} \nCantidad disponible de bicicletas: {}".format(self.nombre, self.direccion, self.barrio, self.cantbicitotal, self.cantbicidisponible)


class Bicicleta():
    def __init__(self, patente, modelo, estacionactual, cantusos):
        self.id = patente
        self.patente = patente
        self.modelo = modelo
        self.estacionactual = estacionactual
        self.cantusos = cantusos

    def cambio(self):
        pass

    def eliminar(self):
        empresa.bicicletas.pop(self.patente)
        estacion = empresa.estaciones.get(self.estacionactual)
        estacion.cantbicidisponible -= 1
        listapatentes.pop(self.patente)
        print("")
        print("Bicicleta eliminada")
        print("")
    
    def __str__(self):
        return "Patente: {} \nModelo: {} \nEstacion actual: {} \nCantidad de usos: {}".format(self.patente, self.modelo, self.estacionactual, self.cantusos)


class Alquiler():
    id = 0

    def __init__(self, usuario, fecha, duracion, estacionsalida, estacionllegada):
        self.id = Alquiler.sumarid()
        self.usuario = usuario
        self.fecha = fecha
        self.duracion = duracion
        self.estacionsalida = estacionsalida
        self.estacionllegada = estacionllegada

    def sumarid():
        Alquiler.id += 1
        return Alquiler.id

    def __str__(self):
        return "Usuario: {} \nCodigo: {} \nFecha: {} \nDuracion: {} \nEstacion salida: {} \nEstacion llegada: {}".format(self.usuario, self.id, self.fecha, self.duracion, self.estacionsalida, self.estacionllegada)


def recorrerpickle():
    nombrespickle = ["datosclientes.pickle", "datostrabajadores.pickle", "datosestaciones.pickle", "datosbicicletas.pickle", "datosalquileres.pickle"]
    diccionarios = [empresa.clientes, empresa.trabajadores, empresa.estaciones, empresa.bicicletas, empresa.alquileres]
    for nombrepickle, diccionario in zip(nombrespickle, diccionarios): 
        with open(nombrepickle, "rb") as archivopickle:
            try:
                while True:
                    objeto = pickle.load(archivopickle)
                    diccionario[(objeto.id)] = objeto
            except EOFError:
                pass
    for cliente in empresa.clientes.values():
        listausuarios.append(cliente.nombre)
        listatarjetas.append(cliente.tarjeta)
        listadnis.append(cliente.dni)
    for trabajador in empresa.trabajadores.values():
        listausuarios.append(trabajador.nombre)
        listacbus.append(trabajador.cbu)
        listadnis.append(trabajador.dni)
    for estacion in empresa.estaciones.values():
        listanombres.append(estacion.nombre)
    for bicicleta in empresa.bicicletas.values():
        listapatentes.append(bicicleta.patente)


def actualizarpickle():
    nombrespickle = ["datosclientes.pickle", "datostrabajadores.pickle", "datosestaciones.pickle", "datosbicicletas.pickle", "datosalquileres.pickle"]
    diccionarios = [empresa.clientes, empresa.trabajadores, empresa.estaciones, empresa.bicicletas, empresa.alquileres]
    for nombrepickle, diccionario in zip(nombrespickle, diccionarios):
        with open(nombrepickle, "wb") as archivopickle:
            for objeto in diccionario.values():
                pickle.dump(objeto, archivopickle)
