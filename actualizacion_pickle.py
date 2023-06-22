from clase_empresa import *
import pickle

def recorrerPickle():
    """Recorre los archivos pickle y recupera la información en forma de diccionarios y listas.
    Args:
        None
    Returns:
        None
    """
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
        empresa.listausuarios.append(cliente.usuario)
        empresa.listatarjetas.append(cliente.tarjeta)
        empresa.listadnis.append(cliente.dni)
    for trabajador in empresa.trabajadores.values():
        empresa.listausuarios.append(trabajador.usuario)
        empresa.listacbus.append(trabajador.cbu)
        empresa.listadnis.append(trabajador.dni)
    for estacion in empresa.estaciones.values():
        empresa.listanombres.append(estacion.nombre)
    for bicicleta in empresa.bicicletas.values():
        empresa.listapatentes.append(bicicleta.patente)

def actualizarPickle():
    """Recorre los diccionarios y las listas para guardar la información en los archivos pickle.
    Args:
        None
    Returns:
        None
    """
    nombrespickle = ["datos_clientes.pickle", "datos_trabajadores.pickle", "datos_estaciones.pickle", "datos_bicicletas.pickle", "datos_alquileres.pickle"]
    diccionarios = [empresa.clientes, empresa.trabajadores, empresa.estaciones, empresa.bicicletas, empresa.alquileres]
    for nombrepickle, diccionario in zip(nombrespickle, diccionarios):
        with open(nombrepickle, "wb") as archivopickle:
            for objeto in diccionario.values():
                pickle.dump(objeto, archivopickle)
                