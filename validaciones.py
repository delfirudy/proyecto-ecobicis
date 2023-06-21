def validarNombre(nombre):
    """Validacion de nombres.

    Args:
        nombre (String): Nombre.

    Returns:
        Boolean: Validación o no del nombre.

    """
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper()

def validarDireccion(direccion):
    """Validacion de direcciones.

    Args:
        direccion (String): Dirección.

    Returns:
        Boolean: Validación o no de la dirección.

    """
    return direccion.replace(" ","").isalnum()

def validarEstacion(nombre, listaestaciones):
    """Validación de estaciones.

    Args:
        nombre (String): Nombre de la estación.
        listaestaciones (List): Lista con nombres de las estaciones.

    Returns:
        Boolean: Validación o no de la estación.
    """
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper() and nombre not in listaestaciones

def validarNumero(numero):
    """Validacion de números.

    Args:
        numero (Int): Nombre.

    Returns:
        Boolean: Validación o no del número.
    """
    return numero.isdigit() 

def validarPatente(patente, listapatentes):
    """Validación de patentes.

    Args:
        patente (Int): Patente de la bicicleta.
        listapatentes (List): Lista con patentes de las bicicletas.

    Returns:
        Boolean: Validación o no de la patente.
    """
    return patente.isdigit() and patente not in listapatentes
