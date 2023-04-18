class empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = []
        self.clientes = []
        self.estaciones = []
        self.bicicletas = []
        self.alquileres = []


class persona:
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion):
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.dni = dni
        self.fecnac = fecnac
        self.telefono = telefono
        self.mail = mail
        self.direccion = direccion


class cliente(persona):
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta):
        persona.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        self.tarjeta = tarjeta
        self.listacliente = [usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, tarjeta]


class trabajador(persona):
    def __init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu):
        persona.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        self.puesto = puesto
        self.cbu = cbu
        self.listatrabajador = [usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu]


class estacion:
    def __init__(self, nombre, direccion, barrio, cantbicitotal, cantbicidisponible=0):
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.cantbicitotal = cantbicitotal
        self.cantbicidisponible = cantbicidisponible
        self.listaestacion = [nombre, direccion, barrio, cantbicitotal, cantbicidisponible]


class bicicleta:
    def __init__(self, patente, modelo, anno, estacionactual, cantusos=0):
        self.patente = patente
        self.modelo = modelo
        self.anno = anno
        self.estacionactual = estacionactual
        self.cantusos = cantusos
        self.listabicicleta = [patente, modelo, anno, estacionactual, cantusos]


class alquiler():
    def __init__(self, usuario, patente, codigo, fecyhora, duracion, estacionsalida, estacionllegada):
        self.usuario = usuario
        self.patente = patente
        self.codigo = codigo
        self.fecyhora = fecyhora
        self.duracion = duracion
        self.estacionsalida = estacionsalida
        self.estacionllegada = estacionllegada
        self.listaalquiler = [usuario, patente, codigo, fecyhora, duracion, estacionsalida, estacionllegada]
