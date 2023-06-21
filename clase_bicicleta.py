from clase_empresa import *
from validaciones import *

class Bicicleta():
    """Manejo de datos de las bicicletas.
    Methods:
        cambio: Cambio de datos.
        eliminar: Eliminar bicicleta.
    Returns:
        String: Lista con los atributos de la bicicleta.
    """

    def __init__(self, patente, modelo, estacionactual, cantusos):
        """Ingreso de datos
        Args:
            patente (Int): Patente de la bicicleta.
            modelo (String): Modelo de la bicicleta.
            estacionactual (String): Estación donde se encuentra la bicicleta
            cantusos (Int): Cantidad de usos de la bicicleta.
        """
        self.id = patente
        self.patente = patente
        self.modelo = modelo
        self.estacionactual = estacionactual
        self.cantusos = cantusos

    def cambio(self):
        """Cambio de datos."""
        cambiado  = "Si"
        eleccioncambio = input("Ingrese dato que quiere cambiar: ")
        print("")
        if eleccioncambio == "patente":
            patente = input("Ingrese patente: ").strip()
            while validarPatente(patente, empresa.listapatentes) == False:
                print("La patente ya existe o el formato es incorrecto, la patente debe ser un numero")
                print("")
                patente = input("Ingrese patente: ").strip()
                print("")
            del empresa.bicicletas[self.id]
            posicion = empresa.listapatentes.index(self.patente)
            empresa.listapatentes[posicion] = patente
            self.patente = patente
            self.id = patente
            empresa.bicicletas[self.id] = self
        elif eleccioncambio == "modelo":
            modelo = input("Ingrese modelo: ").strip()
            print("")
            self.modelo = modelo
        else:
            cambiado = "No"
            print("Dato no encontrado")
            print("")
        if cambiado == "Si":
            print("Cambio realizado")
            print("")

    def eliminar(self):
        """Eliminar bicicleta."""
        empresa.bicicletas.pop(self.patente)
        estacion = empresa.estaciones.get(self.estacionactual)
        estacion.cantbicidisponible -= 1
        empresa.listapatentes.remove(self.patente)
        print("Bicicleta eliminada")
        print("")
    
    def __str__(self):
        return "Patente: {} \nModelo: {} \nEstacion actual: {} \nCantidad de usos: {}".format(self.patente, self.modelo, self.estacionactual, self.cantusos)
