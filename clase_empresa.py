class Empresa:

    def __init__(self, nombre): 
        self.nombre = nombre
        self.trabajadores = {}
        self.clientes = {}
        self.estaciones = {}
        self.bicicletas = {}
        self.alquileres = {}

        self.listausuarios = []
        self.listadnis = []
        self.listatarjetas =[]
        self.listacbus = []
        self.listanombres = []
        self.listapatentes = []

empresa = Empresa("Ecobicis")
