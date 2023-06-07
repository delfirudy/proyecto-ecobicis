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
