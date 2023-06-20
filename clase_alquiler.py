from clase_empresa import *
from validaciones import *

class Alquiler():
    
    id = 0

    def __init__(self, usuario, fecha, inicio, fin, duracion, estacionsalida, estacionllegada, estado):
        self.id = Alquiler.sumarId()
        self.usuario = usuario
        self.fecha = fecha
        self.inicio = inicio
        self.fin = fin
        self.duracion = duracion
        self.estacionsalida = estacionsalida
        self.estacionllegada = estacionllegada
        self.estado = estado

    def sumarId():
        Alquiler.id += 1
        return Alquiler.id
    
    def finalizarAlquiler(self, fin, duracion, estacionllegada):
        self.fin = fin
        self.duracion = duracion
        self.estacionllegada = estacionllegada
        print("")
        print("Alquiler finalizado, la duracion del viaje fue {} ".format(duracion))
        print("")

    def __str__(self):
        return "Usuario: {} \nCodigo: {} \nFecha: {} \nDuracion: {} \nEstacion salida: {} \nEstacion llegada: {}".format(self.usuario, self.id, self.fecha, self.duracion, self.estacionsalida, self.estacionllegada)


