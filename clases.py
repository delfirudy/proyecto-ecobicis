class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = []
        self.clientes = []
        self.estaciones = []
        self.bicicletas = []
        self.alquileres = []
        self.usuarios = []
        self.nombresestaciones = []
        self.patentes = []
        self.cbus = []
        self.tarjetas = []
        self.dnis = []

class Usuario:
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion):
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.dni = dni
        self.fecnac = fecnac
        self.telefono = telefono
        self.mail = mail
        self.direccion = direccion

class Cliente(Usuario):
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta):
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        self.tarjeta = tarjeta
        self.listacliente = [usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta]

class Trabajador(Usuario):
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu):
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        self.puesto = puesto
        self.cbu = cbu
        self.listatrabajador = [usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu]

class Estacion:
    def __init__(self, nombre, direccion, barrio, cantbicitotal, cantbicidisponible=0):
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.cantbicitotal = cantbicitotal
        self.cantbicidisponible = cantbicidisponible
        self.listaestacion = [nombre, direccion, barrio, cantbicitotal, cantbicidisponible]

class Bicicleta:
    def __init__(self, patente, modelo, estacionactual, cantusos=0):
        self.patente = patente
        self.modelo = modelo
        self.estacionactual = estacionactual
        self.cantusos = cantusos
        self.listabicicleta = [patente, modelo, estacionactual, cantusos]

class Alquiler():
    def __init__(self, usuario, codigo, fecha, duracion, estacionsalida, estacionllegada):
        self.usuario = usuario
        self.codigo = codigo
        self.fecha = fecha
        self.duracion = duracion
        self.estacionsalida = estacionsalida
        self.estacionllegada = estacionllegada
        self.listaalquiler = [usuario, codigo, fecha, duracion, estacionsalida, estacionllegada]