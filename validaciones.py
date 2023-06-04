from datetime import datetime
from datetime import date

def validarusuario(usuario, listausuarios):
    return usuario.replace(" ","").isalpha() and usuario not in listausuarios

def validarcontrasena(contrasena):
    return contrasena.replace(" ","").isalpha() and contrasena[0].replace(" ","").isupper()

def validarnombre(nombre):
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper()

def validardni(dni, listadnis):
    return dni.isdigit() and len(dni) == 8 and dni not in listadnis

def validarfecha(fecha):
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
    
def validartelefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

def validarmail(mail):
    return "@" in mail

def validardireccion(direccion):
    return direccion.replace(" ","").isalnum()

def validartarjeta(tarjeta, listatarjetas):
    return tarjeta.isdigit() and len(tarjeta) == 16 and tarjeta not in listatarjetas

def validarpuesto(puesto):
    return puesto.replace(" ","").isalpha()

def validarcbu(cbu, listacbus):
    return cbu.isdigit() and len(cbu) == 22 and cbu not in listacbus

def validarestacion(nombre, listaestaciones):
    return nombre.replace(" ","").isalpha() and nombre[0].replace(" ","").isupper() and nombre not in listaestaciones

def validarnumero(cantbicitotal):
    return cantbicitotal.isdigit() 

def validarpatente(patente, listapatentes):
    patente.isdigit() and patente not in listapatentes

def validarestacionsalida(nombre, listaestaciones, diccionariodatosestaciones):
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

def validarestacionactual(estacionactual, listaestaciones, diccionariodatosestaciones):
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

def validarpersona(usuario, contrasena, listapersonas):
    try:
        trabajador = listapersonas.get(usuario + contrasena)
        cumple = "Si"
    except KeyError:
        print("No se encontro el trabajador")
        cumple = "No"
    except:
        print("Error")
    return cumple == "Si"