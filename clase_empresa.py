class Empresa:
    """Manejo de todos los datos
    Returns:
        None
    """
    def __init__(self, nombre): 
        """Ingreso de datos.
        Args:
            nombre (String): Nombre de la empresa
        Returns:
            None
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
