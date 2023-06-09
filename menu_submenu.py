from clase_cliente import *
from clase_trabajador import *

def validarPersona(usuario, contrasena, diccionariopersonas):
    """Validación de existencia de trabajador o cliente.
    Args:
        usuario (String): Usuario del cliente o trabajador.
        contrasena (String): Contrasena del cliente o trabajador.
        listapersonas (Dict): Puede ser el diccionario de clientes o de trabajadores.
    Returns:
        Boolean: Existencia o no del cliente o trabajador.
    """
    cumple = "No"
    for id in diccionariopersonas.keys():
        if id == usuario + contrasena:
            cumple = "Si"
            break
    return cumple == "Si"

def submenuCambio(trabajador):
    """Manejo de opciones del submenu de cambio para el trabajador.
    Args:
        trabajador (class object): Trabajador que utiliza el submenu.
    Returns:
        None
    """
    seguir3 = True
    while seguir3 == True:
        print("1. Cambiar datos trabajador")
        print("2. Cambiar datos bicicleta")
        print("3. Cambiar datos estacion")
        print("4. Volver a opciones trabajador")
        print("")
        eleccioncambio = input("Ingrese opcion: ")
        print("")
        if eleccioncambio == "1":
            trabajador.cambio("Trabajador", empresa.trabajadores)
        elif eleccioncambio == "2":
            trabajador.cambiarBicicleta()
        elif eleccioncambio == "3":
            trabajador.cambiarEstacion()
        elif eleccioncambio == "4":
            seguir3 = False
        else:
            print("Ingreso incorrecto de opcion")
            print("")

def submenuEliminar(trabajador):
    """Manejo de opciones del submenu de eliminación para el trabajador.
    Args:
        trabajador (class object): Trabajador que utiliza el submenu.
    Returns:
        None
    """
    seguir4 = True
    while seguir4 == True:
        print("1. Eliminar trabajador")
        print("2. Eliminar bicicleta")
        print("3. Eliminar estacion")
        print("4. Volver a opciones trabajador")
        print("")
        eleccioneliminar = input("Ingrese opcion: ")
        print("")
        if eleccioneliminar == "1":
            trabajador.eliminar()
            seguir4 = False
        elif eleccioneliminar == "2":
            trabajador.eliminarBicicleta()
        elif eleccioneliminar == "3":
            trabajador.eliminarEstacion()
        elif eleccioneliminar == "4":
            seguir4 = False
        else:
            print("Ingreso incorrecto de opcion")
            print("")

def subMenuTrabajador():
    """Manejo de opciones del submenu trabajador.
    Args:
        None
    Returns:
        None
    """
    volvio = "No"
    usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    print("")
    while validarPersona(usuario, contrasena, empresa.trabajadores) == False:
        print("Trabajador no encontrado")
        print("")
        volver = input("Ingrese 1 si quiere volver al menu principal: ")
        print("")
        if volver == "1":
            volvio = "Si"
            break
        else:
            volvio = "No"
            usuario = input("Ingrese usuario: ").strip()
            contrasena = input("Ingrese contrasena: ").strip()
        print("")
    if volvio == "No":
        trabajador = empresa.trabajadores.get(usuario + contrasena)
        print("Trabajador validado")
        print("")
        seguir1 = True
        while seguir1 == True:
            print("1. Ingresar estacion")
            print("2. Ingresar bicicleta")
            print("3. Cambiar datos")
            print("4. Dar de baja")
            print("5. Volver al menu principal")
            print("")
            elecciontrabajador = input("Ingrese opcion: ").strip()
            print("")
            if elecciontrabajador == "1":
                trabajador.agregarEstacion()
            elif elecciontrabajador == "2":
                trabajador.agregarBicicleta()
            elif elecciontrabajador == "3":
                submenuCambio(trabajador)
            elif elecciontrabajador == "4":
                submenuEliminar(trabajador)
                seguir1 = False
            elif elecciontrabajador == "5":
                seguir1 = False
            else:
                print("Ingreso incorrecto de opcion")
                print("")

def subMenuCliente():
    """Manejo de opciones del submenu cliente.
    Args:
        None
    Returns:
        None
    """
    volvio = "No"
    usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    print("")
    while validarPersona(usuario, contrasena, empresa.clientes) == False:
        print("Cliente no encontrado")
        print("")
        volver = input("Ingrese 1 si quiere volver al menu principal, otro numero si quiere seguir: ")
        print("")
        if volver == "1":
            volvio = "Si"
            break
        else:
            volvio = "No"
            usuario = input("Ingrese usuario: ").strip()
            contrasena = input("Ingrese contrasena: ").strip()
        print("")
    if volvio == "No":
        cliente = empresa.clientes.get(usuario + contrasena)
        print("Cliente validado")
        print("")
        seguir2 = True
        while seguir2 == True:
            print("1. Alquilar")
            print("2. Finalizar alquiler")
            print("3. Información sobre estaciones")
            print("4. Cambiar datos")
            print("5. Dar de baja")
            print("6. Volver al menu principal")
            print("")
            eleccionusuario = input("Ingrese opcion: ").strip()
            print("")
            if eleccionusuario == "1":
                cliente.alquilar()
            elif eleccionusuario == "2":
                cliente.finalizarAlquiler()
            elif eleccionusuario == "3":
                cliente.mostrarInfo()
            elif eleccionusuario == "4":
                cliente.cambio("Cliente", empresa.clientes)
            elif eleccionusuario == "5":
                cliente.eliminar()
                seguir2 = False
            elif eleccionusuario == "6":
                seguir2 = False
            else:
                print("Ingreso incorrecto de opcion")
                print("")

