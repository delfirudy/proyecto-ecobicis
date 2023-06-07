from clase_empresa import *
from validaciones import *

class Alquiler():
    id = 0

    def __init__(self, usuario, fecha, duracion, estacionsalida, estacionllegada):
        self.id = Alquiler.sumarid()
        self.usuario = usuario
        self.fecha = fecha
        self.duracion = duracion
        self.estacionsalida = estacionsalida
        self.estacionllegada = estacionllegada

    def sumarid():
        Alquiler.id += 1
        return Alquiler.id

    def __str__(self):
        return "Usuario: {} \nCodigo: {} \nFecha: {} \nDuracion: {} \nEstacion salida: {} \nEstacion llegada: {}".format(self.usuario, self.id, self.fecha, self.duracion, self.estacionsalida, self.estacionllegada)


