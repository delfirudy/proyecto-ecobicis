from datetime import datetime
from datetime import date

def validarUsuario(usuario, listausuarios):
    return usuario.replace(" ","").isalpha() and usuario not in listausuarios

def validarContrasena(contrasena):
    return contrasena.replace(" ","").isalpha() and contrasena[0].replace(" ","").isupper()

def validarNombre(nombre):
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper()

def validarDni(dni, listadnis):
    return dni.isdigit() and len(dni) == 8 and dni not in listadnis

def validarFecha(fecha):
    try:
        fecha_valida = datetime.strptime(fecha, "%Y/%m/%d").date()
        fecha_actual = date.today()
        if fecha_valida < fecha_actual:
            return True
        else:
            print("El formato es correcto pero la fecha no es anterior a la actual")
            print("")
            return False
    except ValueError:
        print("El formato es incorrecto, la fecha debe ser de la forma YYYY/MM/DD")
        print("")
        return False
    
def validarTelefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

def validarMail(mail):
    return "@" in mail

def validarDireccion(direccion):
    return direccion.replace(" ","").isalnum()

def validarTarjeta(tarjeta, listatarjetas):
    return tarjeta.isdigit() and len(tarjeta) == 16 and tarjeta not in listatarjetas

def validarPuesto(puesto):
    return puesto.replace(" ","").isalpha()

def validarCbu(cbu, listacbus):
    return cbu.isdigit() and len(cbu) == 22 and cbu not in listacbus

def validarEstacion(nombre, listaestaciones):
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper() and nombre not in listaestaciones

def validarNumero(cantbicitotal):
    return cantbicitotal.isdigit() 

def validarPatente(patente, listapatentes):
    return patente.isdigit() and patente not in listapatentes

def validarEstacionSalida(nombre, listaestaciones, diccionariodatosestaciones):
    try:
        estacion = diccionariodatosestaciones.get(nombre)
        if estacion.cantbicidisponible != 0:
            cumple = "Si"
        else:
            cumple = "No"
    except KeyError:
        print("No se encontro la estacion")
    except:
        print("Error")
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper() and nombre in listaestaciones and cumple == "Si"

def validarEstacionActual(estacionactual, listaestaciones, diccionariodatosestaciones):
    try:
        estacion = diccionariodatosestaciones.get(estacionactual)
        if estacion.cantbicitotal != str(estacion.cantbicidisponible):
            cumple = "Si"
        else:
            cumple = "No"
    except KeyError:
        print("No se encontro la estacion")
    except:
        print("Error")
    return estacionactual.replace(" ","").isalpha() and estacionactual[0].replace(" ","").isupper() and estacionactual in listaestaciones and cumple == "Si"

def validarPersona(usuario, contrasena, listapersonas):
    try:
        persona = listapersonas.get(usuario + contrasena)
        cumple = "Si"
    except KeyError:
        print("No se encontro a la persona")
        cumple = "No"
    except:
        print("Error")
    return cumple == "Si"