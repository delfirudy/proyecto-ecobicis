from clase_empresa import *
import pickle

def recorrerpickle():
    nombrespickle = ["datos_clientes.pickle", "datos_trabajadores.pickle", "datos_estaciones.pickle", "datos_bicicletas.pickle", "datos_alquileres.pickle"]
    diccionarios = [empresa.clientes, empresa.trabajadores, empresa.estaciones, empresa.bicicletas, empresa.alquileres]
    for nombrepickle, diccionario in zip(nombrespickle, diccionarios): 
        with open(nombrepickle, "rb") as archivopickle:
            try:
                while True:
                    objeto = pickle.load(archivopickle)
                    diccionario[(objeto.id)] = objeto
            except EOFError:
                pass
    for cliente in empresa.clientes.values():
        listausuarios.append(cliente.nombre)
        listatarjetas.append(cliente.tarjeta)
        listadnis.append(cliente.dni)
    for trabajador in empresa.trabajadores.values():
        listausuarios.append(trabajador.nombre)
        listacbus.append(trabajador.cbu)
        listadnis.append(trabajador.dni)
    for estacion in empresa.estaciones.values():
        listanombres.append(estacion.nombre)
    for bicicleta in empresa.bicicletas.values():
        listapatentes.append(bicicleta.patente)


def actualizarpickle():
    nombrespickle = ["datos_clientes.pickle", "datos_trabajadores.pickle", "datos_estaciones.pickle", "datos_bicicletas.pickle", "datos_alquileres.pickle"]
    diccionarios = [empresa.clientes, empresa.trabajadores, empresa.estaciones, empresa.bicicletas, empresa.alquileres]
    for nombrepickle, diccionario in zip(nombrespickle, diccionarios):
        with open(nombrepickle, "wb") as archivopickle:
            for objeto in diccionario.values():
                pickle.dump(objeto, archivopickle)