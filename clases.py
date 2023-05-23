from validaciones import *

listausuarios = []
listadnis = []
listatarjetas = []
listacbus = []
listaestaciones = []
listapatentes = []

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
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion):
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
        listausuarios.append(usuario)
        listadnis.append(dni)
    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion)

class Cliente(Usuario):
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta):
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        tarjeta = input("Ingrese tarjeta: ").strip()
        while validartarjeta(tarjeta, listatarjetas) == False:
            print("La tarjeta ya existe o el formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
            print("")
            tarjeta = input("Ingrese tarjeta: ").strip()
        self.tarjeta = tarjeta
        listatarjetas.append(tarjeta)
    def agregar(self):
        empresa.clientes.append(self)
    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nTarjeta: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.tarjeta)

class Trabajador(Usuario):
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu):
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
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
        listacbus.append(cbu)
    def agregar(self):
        empresa.trabajadores.append(self)
    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nPuesto {} \nCbu: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.puesto, self.cbu)

# DEBERIA SER UN METODO DE TRABAJADOR
class Estacion:
    def __init__(self, nombre, direccion, barrio, cantbicitotal, cantbicidisponible=0):
        nombre = input("Ingrese nombre: ").strip()
        while validarestacion(nombre, listaestaciones) == False:
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
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.cantbicitotal = cantbicitotal
        self.cantbicidisponible = cantbicidisponible
        listaestaciones.append(nombre)
    def agregar(self):
        empresa.estaciones.append(self)
    def __str__(self):
        return "Nombre: {} \nDireccion: {} \nBarrio: {} \nCantidad maxima de bicicletas: {} \nCantidad disponible de bicicletas: {}".format(self.nombre, self.direccion, self.barrio, self.cantbicitotal, self.cantbicidisponible)

# DEBERIA SER UN METODO DE TRABAJADOR
class Bicicleta():
    def __init__(self, patente, modelo, estacionactual, cantusos=0):
        patente = input("Ingrese patente: ").strip()
        while validarpatente(patente, listapatentes) == False:
            print("La patente ya existe o el formato es incorrecto, la patente debe ser un numero")
            print("")
            patente = input("Ingrese patente: ").strip()
        modelo = input("Ingrese modelo: ").strip()
        estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
        while validarestacionactual(estacionactual, listaestaciones, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
        self.patente = patente
        self.modelo = modelo
        self.estacionactual = estacionactual
        self.cantusos = cantusos
        # SUMAR UNO A CANTBICIDISPONIBLE
    def agregar(self):
        empresa.bicicletas.append(self)
    def __str__(self):
        return "Patente: {} \nModelo: {} \nEstacion actual: {} \nCantidad de usos: {}".format(self.patente, self.modelo, self.estacionactual, self.cantusos)

# DEBERIA SER UN METODO DE CLIENTE, NO UNA CLASE
class Alquiler():
    def __init__(self, usuario, codigo, fecha, duracion, estacionsalida, estacionllegada):
        fecha = input("Ingrese fecha del alquiler: ").strip()
        while validarfecha(fecha) == False:
            fecha = input("Ingrese fecha del alquiler: ").strip() 
        duracion = input("Ingrese duracion del alquiler en minutos: ").strip()
        while validarnumero(duracion) == False:
            print("El formato es incorrecto, la duracion debe ser un numero")
            print("")
            duracion = input("Ingrese duracion: ").strip()
        estacionsalida = input("Ingrese estacion de salida: ").strip()
        while validarestacionsalida(estacionsalida, listaestaciones) == False:
            print("No se encontro la estacion o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionsalida = input("Ingrese estacion de salida: ").strip()
        estacionllegada = input("Ingrese estacion de llegada: ").strip()
        while validarestacionactual(estacionllegada, listaestaciones, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionllegada = input("Ingrese estacion de llegada: ").strip()
        self.usuario = usuario
        self.codigo = codigo
        self.fecha = fecha
        self.duracion = duracion
        self.estacionsalida = estacionsalida
        self.estacionllegada = estacionllegada
        # SUMAR UNO A CANTIDAD DE USOS
        # SUMAR UNO A ESTACION LLEGADA
        # SUMAR UNO A ESTACION SALIDA
    def agregar(self):
        empresa.alquileres.append(self)
    def __str__(self):
        return "Usuario: {} \nCodigo: {} \nFecha: {} \nDuracion: {} \nEstacion salida: {} \nEstacion llegada: {}".format(self.usuario, self.codigo, self.fecha, self.duracion, self.estacionsalida, self.estacionllegada)
    