class Empresa:
    """Manejo de todos los datos"""
    def __init__(self, nombre): 
        """Ingreso de datos.
        Args:
            nombre (String): Nombre de la empresa
        """
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
