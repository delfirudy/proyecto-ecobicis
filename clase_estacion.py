from clase_empresa import *
from validaciones import *

class Estacion:
    """Manejo de datos de las estaciones.
    Methods:
        cambio: Cambio de datos.
        eliminar: Eliminar estación.
    Returns:
        String: Lista con los atributos de la estación.
    """
    def __init__(self, nombre, direccion, barrio, cantbicitotal, cantbicidisponible):
        """Ingreso de datos.
        Args:
            nombre (String): Nombre de la estación.
            direccion (String): Dirección de la estación.
            barrio (String): Barrio donde se encuentra la estación.
            cantbicitotal (Int): Capacidad de la estación.
            cantbicidisponible (Int): Bicicletas disponibles para alquiler.
        """
        self.id = nombre
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.cantbicitotal = cantbicitotal
        self.cantbicidisponible = cantbicidisponible

    def cambio(self):
        """Cambio de datos."""
        cambiado = "Si"
        eleccioncambio = input("Ingrese dato que quiere cambiar: ")
        print("")
        if eleccioncambio == "nombre":
            nombre = input("Ingrese nombre: ").strip()
            print("")
            while validarEstacion(nombre, empresa.listanombres) == False:
                print("La estacion ya existe o el formato es incorrecto, el nombre debe contener solo letras")
                print("")
                nombre = input("Ingrese nombre: ").strip()
            for bicicleta in empresa.bicicletas.values():
                if bicicleta.estacionactual == self.nombre:
                    bicicleta.estacionactual = nombre
            del empresa.estaciones[self.id]
            posicion = empresa.listanombres.index(self.nombre)
            empresa.listanombres[posicion] = nombre
            self.nombre = nombre
            self.id = nombre
            empresa.estaciones[self.id] = self
        elif eleccioncambio == "direccion":
            direccion = input("Ingrese direccion: ").strip()
            print("")
            while validarDireccion(direccion) == False:
                print("El formato es incorrecto, la direccion debe tener letras y numeros")
                print("")
                direccion = input("Ingrese direccion: ").strip()
            self.direccion = direccion 
        elif eleccioncambio == "barrio":
            barrio = input("Ingrese barrio: ").strip()
            print("")
            while validarNombre(barrio) == False:
                print("El formato es incorrecto, el barrio debe contener solo letras y la primera debe ser mayuscula")
                print("")
                barrio = input("Ingrese barrio: ").strip()
            self.barrio = barrio
        elif eleccioncambio == "cantidad total":
            cantbicitotal = input("Ingrese capacidad: ").strip()
            print("")
            while validarNumero(cantbicitotal) == False:
                print("El formato es incorrecto, la capacidad debe ser un numero")
                print("")
                cantbicitotal = input("Ingrese capacidad: ").strip()
            self.cantbicitotal = cantbicitotal
        else:
            cambiado = "No"
            print("Dato no encontrado")
            print("")  
        if cambiado == "Si":
            print("Cambio realizado")
            print("")       

    def eliminar(self):
        """Eliminar estación."""
        empresa.estaciones.pop(self.nombre)
        empresa.listanombres.remove(self.nombre)
        bicicletas = []
        for bicicleta in empresa.bicicletas.values():
            if bicicleta.estacionactual == self.nombre:
                bicicletas.append(bicicleta.patente)
        for patente in bicicletas:
            empresa.bicicletas.pop(patente)
            empresa.listapatentes.remove(patente)
        print("Estacion eliminada, reingrese las bicicletas en otra estacion")
        print("")

    def __str__(self):
        return "Nombre: {} \nDireccion: {} \nBarrio: {} \nCantidad maxima de bicicletas: {} \nCantidad disponible de bicicletas: {}".format(self.nombre, self.direccion, self.barrio, self.cantbicitotal, self.cantbicidisponible)
