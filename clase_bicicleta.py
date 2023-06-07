from clase_empresa import *
from validaciones import *

class Bicicleta():
    def __init__(self, patente, modelo, estacionactual, cantusos):
        self.id = patente
        self.patente = patente
        self.modelo = modelo
        self.estacionactual = estacionactual
        self.cantusos = cantusos

    def cambio(self):
        eleccioncambio = input("Ingrese dato que quiere cambiar: ")
        if eleccioncambio == "patente":
            patente = input("Ingrese patente: ").strip()
            while validarpatente(patente, listapatentes) == False:
                print("La patente ya existe o el formato es incorrecto, la patente debe ser un numero")
                print("")
                patente = input("Ingrese patente: ").strip()
            posicion = listapatentes.index(self.patente)
            listapatentes[posicion] = patente
            self.patente = patente
        elif eleccioncambio == "modelo":
            modelo = input("Ingrese modelo: ").strip()
            self.modelo = modelo

    def eliminar(self):
        empresa.bicicletas.pop(self.patente)
        estacion = empresa.estaciones.get(self.estacionactual)
        estacion.cantbicidisponible -= 1
        listapatentes.remove(self.patente)
        print("")
        print("Bicicleta eliminada")
        print("")
    
    def __str__(self):
        return "Patente: {} \nModelo: {} \nEstacion actual: {} \nCantidad de usos: {}".format(self.patente, self.modelo, self.estacionactual, self.cantusos)
