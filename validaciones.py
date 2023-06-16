def validarNombre(nombre):
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper()

def validarDireccion(direccion):
    return direccion.replace(" ","").isalnum()

def validarEstacion(nombre, listaestaciones):
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper() and nombre not in listaestaciones

def validarNumero(numero):
    return numero.isdigit() 

def validarPatente(patente, listapatentes):
    return patente.isdigit() and patente not in listapatentes
