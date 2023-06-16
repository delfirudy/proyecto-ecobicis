from clase_estacion import *
from clase_alquiler import *
from clase_bicicleta import *
from clase_empresa import *
from datetime import datetime
from datetime import date

class Usuario:

    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None):

        usuario = input("Ingrese usuario: ").strip()
        while self.validarUsuario(usuario, empresa.listausuarios) == False:
            print("El usuario ya existe o el formato es incorrecto, el usuario debe contener solo letras")
            print("")
            usuario = input("Ingrese usuario: ").strip()
        contrasena = input("Ingrese contrasena: ").strip()
        while self.validarContrasena(contrasena) == False:
            print("El formato es incorrecto, la contrasena debe contener solo letras y la primera debe ser mayuscula")
            print("")
            contrasena = input("Ingrese contrasena: ").strip()
        nombre = input("Ingrese nombre: ").strip()
        while validarNombre(nombre) == False:
            print("El formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            nombre = input("Ingrese nombre: ").strip()
        dni = input("Ingrese dni: ").strip()
        while self.validarDni(dni, empresa.listadnis) == False:
            print("El dni ya existe o el formato es incorrecto, debe ser un numero de ocho caracteres")
            print("")
            dni = input("Ingrese dni: ").strip()
        fecnac = input("Ingrese fecha de nacimiento: ").strip() 
        while self.validarFecha(fecnac) == False:
            fecnac = input("Ingrese fecha de nacimiento: ").strip() 
        telefono = input("Ingrese telefono: ").strip()
        while self.validarTelefono(telefono) == False:
            print("El formato es incorrecto, el telefono debe ser un numero de diez caracteres")
            print("")
            telefono = input("Ingrese telefono: ").strip()
        mail = input("Ingrese mail: ").strip()
        while self.validarMail(mail) == False:
            print("El formato es incorrecto, el mail debe contener un @")
            print("")
            mail = input("Ingrese mail: ").strip()
        direccion = input("Ingrese direccion: ").strip()
        while validarDireccion(direccion) == False:
            print("El formato es incorrecto, la direccion debe tener letras y numeros")
            print("")
            direccion = input("Ingrese direccion: ").strip()

        self.id = usuario + contrasena
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.dni = dni
        self.fecnac = fecnac
        self.telefono = telefono
        self.mail = mail
        self.direccion = direccion

        empresa.listausuarios.append(usuario)
        empresa.listadnis.append(dni)

    def validarUsuario(self, usuario, listausuarios):
        return usuario.replace(" ","").isalpha() and usuario not in listausuarios
    
    def validarContrasena(self, contrasena):
        return contrasena.replace(" ","").isalpha() and contrasena[0].replace(" ","").isupper()
    
    def validarDni(self, dni, listadnis):
        return dni.isdigit() and len(dni) == 8 and dni not in listadnis

    def validarFecha(self, fecha):
        try:
            fecha_valida = datetime.strptime(fecha, "%Y/%m/%d").date()
            fecha_actual = date.today()
            if fecha_valida <= fecha_actual:
                return True
            else:
                print("El formato es correcto pero la fecha no es anterior a la actual")
                print("")
                return False
        except ValueError:
            print("El formato es incorrecto, la fecha debe ser de la forma YYYY/MM/DD")
            print("")
            return False
        
    def validarTelefono(self, telefono):
        return telefono.isdigit() and len(telefono) == 10

    def validarMail(self, mail):
        return "@" in mail

    def validarEstacionActual(self, estacionactual, listaestaciones, diccionariodatosestaciones):
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


    def cambio(self, tipo, diccionario):

        cambiado = "Si"
        eleccioncambio = input("Ingrese dato que quiere cambiar: ")

        if eleccioncambio == "usuario":
            usuario = input("Ingrese usuario: ").strip()
            while self.validarUsuario(usuario, empresa.listausuarios) == False:
                print("El usuario ya existe o el formato es incorrecto, el usuario debe contener solo letras")
                print("")
                usuario = input("Ingrese usuario: ").strip()
            del diccionario[self.id]
            posicion = empresa.listausuarios.index(self.usuario)
            empresa.listausuarios[posicion] = usuario
            self.usuario = usuario
            self.id = self.usuario + self.contrasena
            diccionario[self.id] = self
        elif eleccioncambio == "contrasena":
            contrasena = input("Ingrese contrasena: ").strip()
            while self.validarContrasena(contrasena) == False:
                print("El formato es incorrecto, la contrasena debe contener solo letras y la primera debe ser mayuscula")
                print("")
                contrasena = input("Ingrese contrasena: ").strip()
            del diccionario[self.id]
            self.contrasena = contrasena
            self.id = self.usuario + self.contrasena
            diccionario[self.id] = self
        elif eleccioncambio == "nombre":
            nombre = input("Ingrese nombre: ").strip()
            while validarNombre(nombre) == False:
                print("El formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
                print("")
                nombre = input("Ingrese nombre: ").strip()
            self.nombre = nombre
        elif eleccioncambio == "dni":
            dni = input("Ingrese dni: ").strip()
            while self.validarDni(dni, empresa.listadnis) == False:
                print("El dni ya existe o el formato es incorrecto, debe ser un numero de ocho caracteres")
                print("")
                dni = input("Ingrese dni: ").strip()
            posicion = empresa.listadnis.index(self.dni)
            empresa.listadnis[posicion] = dni
            self.dni = dni
        elif eleccioncambio == "fecha de nacimiento":
            fecnac = input("Ingrese fecha de nacimiento: ").strip() 
            while self.validarFecha(fecnac) == False:
                fecnac = input("Ingrese fecha de nacimiento: ").strip() 
            self.fecnac = fecnac
        elif eleccioncambio == "telefono":
            telefono = input("Ingrese telefono: ").strip()
            while self.validarTelefono(telefono) == False:
                print("El formato es incorrecto, el telefono debe ser un numero de diez caracteres")
                print("")
                telefono = input("Ingrese telefono: ").strip()
            self.telefono = telefono
        elif eleccioncambio == "mail":
            mail = input("Ingrese mail: ").strip()
            while self.validarMail(mail) == False:
                print("El formato es incorrecto, el mail debe contener un @")
                print("")
                mail = input("Ingrese mail: ").strip()
            self.mail = mail
        elif eleccioncambio == "direccion":
            direccion = input("Ingrese direccion: ").strip()
            while validarDireccion(direccion) == False:
                print("El formato es incorrecto, la direccion debe tener letras y numeros")
                print("")
                direccion = input("Ingrese direccion: ").strip()
            self.direccion = direccion
        elif eleccioncambio == "tarjeta":
            if tipo == "Cliente":
                self.cambio_tarjeta()
            else:
                cambiado = "No"
                print("No se encontro el dato")
                print("")
        elif eleccioncambio == "puesto":
            if tipo == "Trabajador":
                self.cambio_puesto()
            else:
                cambiado = "No"
                print("No se encontro el dato")
                print("")
        elif eleccioncambio == "cbu":
            if tipo == "Trabajador":
                self.cambio_trabajador()
            else:
                cambiado = "No"
                print("No se encontro el dato")
                print("")
        else:
            cambiado = "No"
            print("No se encontro el dato")
            print("")

        if cambiado == "Si":
            print("")
            print("Cambio realizado")
            print("")

    def __str__(self):

        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion)


class Cliente(Usuario):

    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None, tarjeta=0):
        
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        tarjeta = input("Ingrese tarjeta: ").strip()
        while self.validarTarjeta(tarjeta, empresa.listatarjetas) == False:
            print("La tarjeta ya existe o el formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
            print("")
            tarjeta = input("Ingrese tarjeta: ").strip()
        
        self.tarjeta = tarjeta
        empresa.listatarjetas.append(tarjeta)
        empresa.clientes[self.id] = self

        print("")
        print("Cliente ingresado")
        print("")

    def validarTarjeta(self, tarjeta, listatarjetas):
        return tarjeta.isdigit() and len(tarjeta) == 16 and tarjeta not in listatarjetas
    
    def validarEstacionSalida(self, nombre, listaestaciones, diccionariodatosestaciones):
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

    def cambio_tarjeta(self):

        tarjeta = input("Ingrese tarjeta: ").strip()
        while self.validarTarjeta(tarjeta, empresa.listatarjetas) == False:
            print("La tarjeta ya existe o el formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
            print("")
            tarjeta = input("Ingrese tarjeta: ").strip()

        posicion = empresa.listatarjetas.index(self.tarjeta)
        empresa.listatarjetas[posicion] = tarjeta
        self.tarjeta = tarjeta

    def eliminar(self):

        empresa.clientes.pop(self.id)
        empresa.listadnis.remove(self.dni)
        empresa.listatarjetas.remove(self.tarjeta)
        empresa.listausuarios.remove(self.usuario)

        print("")
        print("Cliente eliminado")
        print("")
    
    def alquilar(self):

        fecha = input("Ingrese fecha del alquiler: ").strip()
        while self.validarFecha(fecha) == False:
            fecha = input("Ingrese fecha del alquiler: ").strip() 
        duracion = input("Ingrese duracion del alquiler en minutos: ").strip()
        while validarNumero(duracion) == False:
            print("El formato es incorrecto, la duracion debe ser un numero")
            print("")
            duracion = input("Ingrese duracion: ").strip()
        estacionsalida = input("Ingrese estacion de salida: ").strip()
        while self.validarEstacionSalida(estacionsalida, empresa.listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay bicicletas o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionsalida = input("Ingrese estacion de salida: ").strip()
        estacionllegada = input("Ingrese estacion de llegada: ").strip()
        while self.validarEstacionActual(estacionllegada, empresa.listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionllegada = input("Ingrese estacion de llegada: ").strip()

        empresa.alquileres[(Alquiler.id)] = Alquiler(self.nombre, fecha, duracion, estacionsalida, estacionllegada)
        try:
            estacion = empresa.estaciones.get(estacionsalida)
            estacion.cantbicidisponible -= 1
        except KeyError:
            print("No se encontro la estacion")
        except:
            print("Error")
        try:
            estacion = empresa.estaciones.get(estacionllegada)
            estacion.cantbicidisponible += 1
        except KeyError:
            print("No se encontro la estacion")
        except:
            print("Error")
        for bicicleta in empresa.bicicletas.values():
            if bicicleta.estacionactual == estacionsalida:
                bicicleta.cantusos += 1
                bicicleta.estacionactual = estacionllegada
                break
        
        print("")
        print("Alquiler ingresado")
        print("")

    def mostrarInfo(self):
        print("Nombre    Direccion    Barrio    Capacidad    Disponible")

        for estacion in empresa.estaciones.values():
            print(str(estacion.nombre) + " " + str(estacion.direccion) + " " + str(estacion.barrio) + " " + str(estacion.cantbicitotal) + " " + str(estacion.cantbicidisponible))
            print("")

    def __str__(self):

        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nTarjeta: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.tarjeta)


class Trabajador(Usuario):

    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None, puesto=None, cbu=0):
        
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        puesto = input("Ingrese puesto: ").strip()
        while self.validarPuesto(puesto) == False:
            print("El formato es incorrecto, el puesto debe contener solo letras")
            print("")
            puesto = input("Ingrese puesto: ").strip()
        cbu = input("Ingrese cbu: ").strip()
        while self.validarCbu(cbu, empresa.listacbus) == False:
            print("El cbu ya existe o el formato es incorrecto, el cbu debe ser un numero de 22 digitos")
            print("")
            cbu = input("Ingrese el cbu: ").strip()

        self.puesto = puesto
        self.cbu = cbu
        empresa.listacbus.append(cbu)
        empresa.trabajadores[self.id] = self

        print("")
        print("Trabajador ingresado")
        print("")

    def validarPuesto(self, puesto):
        return puesto.replace(" ","").isalpha()
    
    def validarCbu(self, cbu, listacbus):
        return cbu.isdigit() and len(cbu) == 22 and cbu not in listacbus

    def cambio_puesto(self):

        puesto = input("Ingrese puesto: ").strip()
        while self.validarPuesto(puesto) == False:
            print("El formato es incorrecto, el puesto debe contener solo letras")
            print("")
            puesto = input("Ingrese puesto: ").strip()

        self.puesto = puesto

    def cambio_cbu(self):

        cbu = input("Ingrese cbu: ").strip()
        while self.validarCbu(cbu, empresa.listacbus) == False:
            print("El cbu ya existe o el formato es incorrecto, el cbu debe ser un numero de 22 digitos")
            print("")
            cbu = input("Ingrese cbu: ").strip()

        posicion = empresa.listacbus.index(self.cbu)
        empresa.listacbus[posicion] = cbu
        self.cbu = cbu

    def eliminar(self):

        empresa.trabajadores.pop(self.id)
        empresa.listacbus.remove(self.cbu)
        empresa.listadnis.remove(self.dni)
        empresa.listausuarios.remove(self.usuario)

        print("")
        print("Trabajador eliminado")
        print("")

    def agregarEstacion(self):

        nombre = input("Ingrese nombre: ").strip()
        while validarEstacion(nombre, empresa.listanombres) == False:
            print("La estacion ya existe o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            nombre = input("Ingrse nombre: ").strip()
        direccion = input("Ingrese direccion: ").strip()
        while validarDireccion(direccion) == False:
            print("El formato es incorrecto, la direccion debe tener letras y numeros")
            print("")
            direccion = input("Ingrese direccion: ").strip()
        barrio = input("Ingrese barrio: ").strip()
        while validarNombre(barrio) == False:
            print("El formato es incorrecto, el barrio debe contener solo letras y la primera debe ser mayuscula")
            print("")
            barrio = input("Ingrese barrio: ").strip()
        cantbicitotal = input("Ingrese capacidad: ").strip()
        while validarNumero(cantbicitotal) == False:
            print("El formato es incorrecto, la capacidad debe ser un numero")
            print("")
            cantbicitotal = input("Ingrese capacidad: ").strip()

        cantbicidisponible = 0
        empresa.listanombres.append(nombre)
        empresa.estaciones[nombre] = Estacion(nombre, direccion, barrio, cantbicitotal, cantbicidisponible)
        
        print("")
        print("Estacion ingresada")
        print("")

    def agregarBicicleta(self):

        patente = input("Ingrese patente: ").strip()
        while validarPatente(patente, empresa.listapatentes) == False:
            print("La patente ya existe o el formato es incorrecto, la patente debe ser un numero")
            print("")
            patente = input("Ingrese patente: ").strip()
        modelo = input("Ingrese modelo: ").strip()
        estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
        while self.validarEstacionActual(estacionactual, empresa.listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
        
        cantusos = 0
        empresa.listapatentes.append(patente)
        empresa.bicicletas[patente] = Bicicleta(patente, modelo, estacionactual, cantusos)
        try:
            estacion = empresa.estaciones.get(estacionactual)
            estacion.cantbicidisponible += 1
        except KeyError:
            print("No se encontro la estacion")
        except:
            print("Error")

        print("")
        print("Bicicleta ingresada")
        print("")

    def cambiarBicicleta(self):

        patente = input("Ingrese la patente de la bicicleta a modificar: ").strip()
        while validarPatente(patente, empresa.listapatentes) == True:
            print("Patente no encontrada")
            print("")
            patente = input("Ingrese bicicleta a modificar: ").strip()

        bicicleta = empresa.bicicletas.get(patente)
        bicicleta.cambio()

    def cambiarEstacion(self):

        nombre = input("Ingrese el nombre de la estacion a modificar: ").strip()
        while validarEstacion(nombre, empresa.listanombres) == True:
            print("Estacion no encontrada")
            print("")
            nombre = input("Ingrese el nombre de la estacion a modificar: ").strip()

        estacion = empresa.estaciones.get(nombre)
        estacion.cambio()

    def eliminarBicicleta(self):

        patente = input("Ingrese la patente de la bicicleta a eliminar: ").strip()
        while validarPatente(patente, empresa.listapatentes) == True:
            print("Patente no encontrada")
            print("")
            patente = input("Ingrese bicicleta a eliminar: ").strip()
            
        bicicleta = empresa.bicicletas.get(patente)
        bicicleta.eliminar()

    def eliminarEstacion(self):

        nombre = input("Ingrese el nombre de la estacion a eliminar: ").strip()
        while validarEstacion(nombre, empresa.listanombres) == True:
            print("Estacion no encontrada")
            print("")
            nombre = input("Ingrese el nombre de la estacion a eliminar: ").strip()

        estacion = empresa.estaciones.get(nombre)
        estacion.eliminar()

    def __str__(self):

        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nPuesto {} \nCbu: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.puesto, self.cbu)