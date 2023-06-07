from clase_empresa import *
from validaciones import *

class Estacion:
    def __init__(self, nombre, direccion, barrio, cantbicitotal, cantbicidisponible):
        self.id = nombre
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.cantbicitotal = cantbicitotal
        self.cantbicidisponible = cantbicidisponible

    def cambio(self):
        eleccioncambio = input("Ingrese dato que quiere cambiar: ")
        if eleccioncambio == "nombre":
           nombre = input("Ingrese nombre: ").strip()
           while validarestacion(nombre, listanombres) == False:
                print("La estacion ya existe o el formato es incorrecto, el nombre debe contener solo letras")
                print("")
                nombre = input("Ingrese nombre: ").strip()
           posicion = listanombres.index(self.nombre)
           listanombres[posicion] = nombre
           self.nombre = nombre
        elif eleccioncambio == "direccion":
            direccion = input("Ingrese direccion: ").strip()
            while validardireccion(direccion) == False:
                print("El formato es incorrecto, la direccion debe tener letras y numeros")
                print("")
                direccion = input("Ingrese direccion: ").strip()
            self.direccion = direccion 
        elif eleccioncambio == "barrio":
            barrio = input("Ingrese barrio: ").strip()
            while validarnombre(barrio) == False:
                print("El formato es incorrecto, el barrio debe contener solo letras y la primera debe ser mayuscula")
                print("")
                barrio = input("Ingrese barrio: ").strip()
            self.barrio = barrio
        elif eleccioncambio == "cantidad total":
            cantbicitotal = input("Ingrese capacidad: ").strip()
            while validarnumero(cantbicitotal) == False:
                print("El formato es incorrecto, la capacidad debe ser un numero")
                print("")
                cantbicitotal = input("Ingrese capacidad: ").strip()
            self.cantbicitotal = cantbicitotal         

    def eliminar(self):
        empresa.estaciones.pop(self.nombre)
        bicicletas = []
        for bicicleta in empresa.bicicletas.values():
            if bicicleta.estacionactual == self.nombre:
                bicicletas.append(bicicleta.patente)
        for patente in bicicletas:
            empresa.bicicletas.pop(patente)
        listanombres.remove(self.nombre)
        print("")
        print("Estacion eliminada, reingrese las bicicletas en otra estacion")
        print("")

    def __str__(self):
        return "Nombre: {} \nDireccion: {} \nBarrio: {} \nCantidad maxima de bicicletas: {} \nCantidad disponible de bicicletas: {}".format(self.nombre, self.direccion, self.barrio, self.cantbicitotal, self.cantbicidisponible)
