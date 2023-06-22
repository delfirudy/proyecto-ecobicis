from clase_empresa import *
from validaciones import *

class Alquiler():
    """Manejo de datos de los alquileres.
    Returns:
        Class object: Alquiler.
    """
    id = 0
    
    def __init__(self, usuario, fecha, inicio, fin, duracion, estacionsalida, estacionllegada, estado):
        """Ingreso de datos.
        Args:
            usuario (String): Usuario que alquila.
            fecha (Datetime): Fecha de alquiler.
            inicio (Time): Hora de inicio.
            fin (Time): Hora de finalización.
            duracion (Int): Total del alquiler.
            estacionsalida (String): Estación de inicio.
            estacionllegada (String): Estación de finalización.
            estado (String): En curso o finalizado.
        Returns:
            None
        """
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
        """Contador para código.
        Args:
            None
        Returns:
            Int: Código.
        """
        Alquiler.id += 1
        return Alquiler.id
    
    def finalizar(self, fin, duracion, estacionllegada):
        """Finaliza el alquiler.
        Args:
            fin (Time): Hora de finalización.
            duracion (Int): Total del alquiler.
            estacionllegada (String): Estación de finalización.
        Returns:
            None
        """
        self.fin = fin
        self.duracion = duracion
        self.estacionllegada = estacionllegada
        self.estado = "finalizado"
        print("Alquiler finalizado, la duracion del viaje fue {} ".format(duracion))
        print("")

    def __str__(self):
        return "Usuario: {} \nCodigo: {} \nFecha: {} \nDuracion: {} \nEstacion salida: {} \nEstacion llegada: {}".format(self.usuario, self.id, self.fecha, self.duracion, self.estacionsalida, self.estacionllegada)
