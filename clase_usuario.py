from clase_estacion import *
from clase_alquiler import *
from clase_bicicleta import *
from validaciones import *

class Usuario:
    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None):
        # Ingreso de datos del usuario
        usuario = input("Ingrese usuario: ").strip()
        while validarUsuario(usuario, listausuarios) == False:
            print("El usuario ya existe o el formato es incorrecto, el usuario debe contener solo letras")
            print("")
            usuario = input("Ingrese usuario: ").strip()
        contrasena = input("Ingrese contrasena: ").strip()
        while validarContrasena(contrasena) == False:
            print("El formato es incorrecto, la contrasena debe contener solo letras y la primera debe ser mayuscula")
            print("")
            contrasena = input("Ingrese contrasena: ").strip()
        nombre = input("Ingrese nombre: ").strip()
        while validarNombre(nombre) == False:
            print("El formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            nombre = input("Ingrese nombre: ").strip()
        dni = input("Ingrese dni: ").strip()
        while validarDni(dni, listadnis) == False:
            print("El dni ya existe o el formato es incorrecto, debe ser un numero de ocho caracteres")
            print("")
            dni = input("Ingrese dni: ").strip()
        fecnac = input("Ingrese fecha de nacimiento: ").strip() 
        while validarFecha(fecnac) == False:
            fecnac = input("Ingrese fecha de nacimiento: ").strip() 
        telefono = input("Ingrese telefono: ").strip()
        while validarTelefono(telefono) == False:
            print("El formato es incorrecto, el telefono debe ser un numero de diez caracteres")
            print("")
            telefono = input("Ingrese telefono: ").strip()
        mail = input("Ingrese mail: ").strip()
        while validarMail(mail) == False:
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
        # Agregado de usuario a la lista de usuarios
        listausuarios.append(usuario)
        # Agregado de dni a la lista de dnis
        listadnis.append(dni)

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion)


class Cliente(Usuario):
    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None, tarjeta=0):
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        # Ingreso de datos del cliente
        tarjeta = input("Ingrese tarjeta: ").strip()
        while validarTarjeta(tarjeta, listatarjetas) == False:
            print("La tarjeta ya existe o el formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
            print("")
            tarjeta = input("Ingrese tarjeta: ").strip()
        self.tarjeta = tarjeta
        # Agregado de tarjeta a la lista de tarjetas
        listatarjetas.append(tarjeta)
        # Agregado de cliente al diccionario de clientes
        empresa.clientes[self.id] = self
        print("")
        print("Cliente ingresado")
        print("")

    def cambio(self):
        eleccioncambio = input("Ingrese dato que quiere cambiar: ")
        if eleccioncambio == "usuario":
            usuario = input("Ingrese usuario: ").strip()
            while validarUsuario(usuario, listausuarios) == False:
                print("El usuario ya existe o el formato es incorrecto, el usuario debe contener solo letras")
                print("")
                usuario = input("Ingrese usuario: ").strip()
            posicion = listausuarios.index(self.usuario)
            listausuarios[posicion] = usuario
            self.usuario = usuario
        elif eleccioncambio == "contrasena":
            contrasena = input("Ingrese contrasena: ").strip()
            while validarContrasena(contrasena) == False:
                print("El formato es incorrecto, la contrasena debe contener solo letras y la primera debe ser mayuscula")
                print("")
                contrasena = input("Ingrese contrasena: ").strip()
            self.contrasena = contrasena
        elif eleccioncambio == "nombre":
            nombre = input("Ingrese nombre: ").strip()
            while validarNombre(nombre) == False:
                print("El formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
                print("")
                nombre = input("Ingrese nombre: ").strip()
            self.nombre = nombre
        elif eleccioncambio == "dni":
            dni = input("Ingrese dni: ").strip()
            while validarDni(dni, listadnis) == False:
                print("El dni ya existe o el formato es incorrecto, debe ser un numero de ocho caracteres")
                print("")
                dni = input("Ingrese dni: ").strip()
            posicion = listadnis.index(self.dni)
            listadnis[posicion] = dni
            self.dni = dni
        elif eleccioncambio == "fecha de nacimiento":
            fecnac = input("Ingrese fecha de nacimiento: ").strip() 
            while validarFecha(fecnac) == False:
                fecnac = input("Ingrese fecha de nacimiento: ").strip() 
            self.fecnac = fecnac
        elif eleccioncambio == "telefono":
            telefono = input("Ingrese telefono: ").strip()
            while validarTelefono(telefono) == False:
                print("El formato es incorrecto, el telefono debe ser un numero de diez caracteres")
                print("")
                telefono = input("Ingrese telefono: ").strip()
            self.telefono = telefono
        elif eleccioncambio == "mail":
            mail = input("Ingrese mail: ").strip()
            while validarMail(mail) == False:
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
        elif eleccioncambio == "Tarjeta":
            tarjeta = input("Ingrese tarjeta: ").strip()
            while validarTarjeta(tarjeta, listatarjetas) == False:
                print("La tarjeta ya existe o el formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
                print("")
                tarjeta = input("Ingrese tarjeta: ").strip()
            posicion = listatarjetas.index(self.tarjeta)
            listatarjetas[posicion] = tarjeta
            self.tarjeta = tarjeta
        else:
            print("No se encontro el dato")
            print("")

    def eliminar(self):
        empresa.clientes.pop(self.usuario + self.contrasena)
        listadnis.remove(self.dni)
        listatarjetas.remove(self.tarjeta)
        listausuarios.remove(self.usuario)
        print("")
        print("Cliente eliminado")
        print("")
    
    def alquilar(self):
        # Ingreso de datos del alquiler
        fecha = input("Ingrese fecha del alquiler: ").strip()
        while validarFecha(fecha) == False:
            fecha = input("Ingrese fecha del alquiler: ").strip() 
        duracion = input("Ingrese duracion del alquiler en minutos: ").strip()
        while validarNumero(duracion) == False:
            print("El formato es incorrecto, la duracion debe ser un numero")
            print("")
            duracion = input("Ingrese duracion: ").strip()
        estacionsalida = input("Ingrese estacion de salida: ").strip()
        while validarEstacionSalida(estacionsalida, listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay bicicletas o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionsalida = input("Ingrese estacion de salida: ").strip()
        estacionllegada = input("Ingrese estacion de llegada: ").strip()
        while validarEstacionActual(estacionllegada, listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionllegada = input("Ingrese estacion de llegada: ").strip()
        # Agregado de alquiler al diccionario de alquileres
        empresa.alquileres[(Alquiler.id)] = Alquiler(self.nombre, fecha, duracion, estacionsalida, estacionllegada)
        # Resta uno a cantbicidisponible de la estacion salida
        try:
            estacion = empresa.estaciones.get(estacionsalida)
            estacion.cantbicidisponible -= 1
        except KeyError:
            print("No se encontro la estacion")
        except:
            print("Error")
        # Suma uno a cantbicidisponible de la estacion llegada 
        try:
            estacion = empresa.estaciones.get(estacionllegada)
            estacion.cantbicidisponible += 1
        except KeyError:
            print("No se encontro la estacion")
        except:
            print("Error")
        # Mueve la bicicleta de una estacion a la otra
        # Suma uno a cantusos de la bicicleta
        for bicicleta in empresa.bicicletas.values():
            if bicicleta.estacionactual == estacionsalida:
                bicicleta.cantusos += 1
                bicicleta.estacionactual = estacionllegada
                break
        print("")
        print("Alquiler ingresado")
        print("")

    def mostrarInfo(self):
        for estacion in empresa.estaciones.values():
            print(str(estacion.nombre) + " " + str(estacion.direccion) + " " + str(estacion.barrio) + " " + str(estacion.cantbicitotal) + " " + str(estacion.cantbicidisponible))
            print("")

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nTarjeta: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.tarjeta)


class Trabajador(Usuario):
    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None, puesto=None, cbu=0):
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        # Ingreso de datos del trabajador
        puesto = input("Ingrese puesto: ").strip()
        while validarPuesto(puesto) == False:
            print("El formato es incorrecto, el puesto debe contener solo letras")
            print("")
            puesto = input("Ingrese puesto: ").strip()
        cbu = input("Ingrese cbu: ").strip()
        while validarCbu(cbu, listacbus) == False:
            print("El cbu ya existe o el formato es incorrecto, el cbu debe ser un numero de 22 digitos")
            print("")
            cbu = input("Ingrese el cbu: ").strip()
        self.puesto = puesto
        self.cbu = cbu
        # Agregado del cbu a la lista de cbus
        listacbus.append(cbu)
        # Agregado de trabajador al diccionario de trabajadores
        empresa.trabajadores[self.id] = self
        print("")
        print("Trabajador ingresado")
        print("")

    def cambio(self):
        eleccioncambio = input("Ingrese dato que quiere cambiar: ")
        if eleccioncambio == "usuario":
            usuario = input("Ingrese usuario: ").strip()
            while validarUsuario(usuario, listausuarios) == False:
                print("El usuario ya existe o el formato es incorrecto, el usuario debe contener solo letras")
                print("")
                usuario = input("Ingrese usuario: ").strip()
            posicion = listausuarios.index(self.usuario)
            listausuarios[posicion] = usuario
            self.usuario = usuario
        elif eleccioncambio == "contrasena":
            contrasena = input("Ingrese contrasena: ").strip()
            while validarContrasena(contrasena) == False:
                print("El formato es incorrecto, la contrasena debe contener solo letras y la primera debe ser mayuscula")
                print("")
                contrasena = input("Ingrese contrasena: ").strip()
            self.contrasena = contrasena
        elif eleccioncambio == "nombre":
            nombre = input("Ingrese nombre: ").strip()
            while validarNombre(nombre) == False:
                print("El formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
                print("")
                nombre = input("Ingrese nombre: ").strip()
            self.nombre = nombre
        elif eleccioncambio == "dni":
            dni = input("Ingrese dni: ").strip()
            while validarDni(dni, listadnis) == False:
                print("El dni ya existe o el formato es incorrecto, debe ser un numero de ocho caracteres")
                print("")
                dni = input("Ingrese dni: ").strip()
            posicion = listadnis.index(self.dni)
            listadnis[posicion] = dni
            self.dni = dni
        elif eleccioncambio == "fecha de nacimiento":
            fecnac = input("Ingrese fecha de nacimiento: ").strip() 
            while validarFecha(fecnac) == False:
                fecnac = input("Ingrese fecha de nacimiento: ").strip() 
            self.fecnac = fecnac
        elif eleccioncambio == "telefono":
            telefono = input("Ingrese telefono: ").strip()
            while validarTelefono(telefono) == False:
                print("El formato es incorrecto, el telefono debe ser un numero de diez caracteres")
                print("")
                telefono = input("Ingrese telefono: ").strip()
            self.telefono = telefono
        elif eleccioncambio == "mail":
            mail = input("Ingrese mail: ").strip()
            while validarMail(mail) == False:
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
        elif eleccioncambio == "puesto":
            puesto = input("Ingrese puesto: ").strip()
            while validarPuesto(puesto) == False:
                print("El formato es incorrecto, el puesto debe contener solo letras")
                print("")
                puesto = input("Ingrese puesto: ").strip()
            self.puesto = puesto
        elif eleccioncambio == "cbu":
            cbu = input("Ingrese cbu: ").strip()
            while validarCbu(cbu, listacbus) == False:
                print("El cbu ya existe o el formato es incorrecto, el cbu debe ser un numero de 22 digitos")
                print("")
                cbu = input("Ingrese cbu: ").strip()
            posicion = listacbus.index(self.cbu)
            listacbus[posicion] = cbu
            self.cbu = cbu
        else:
            print("No se encontro el dato")
            print("")

    def eliminar(self):
        empresa.trabajadores.pop(self.usuario + self.contrasena)
        listacbus.remove(self.cbu)
        listadnis.remove(self.dni)
        listausuarios.remove(self.usuario)
        print("")
        print("Trabajador eliminado")
        print("")

    def agregarEstacion(self):
        # Ingreso de datos de la estacion
        nombre = input("Ingrese nombre: ").strip()
        while validarEstacion(nombre, listanombres) == False:
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
        # Agregado de nombre a la lista de nombres
        listanombres.append(nombre)
        # Agregado de estacion al diccionario de estaciones
        empresa.estaciones[nombre] = Estacion(nombre, direccion, barrio, cantbicitotal, cantbicidisponible)
        print("")
        print("Estacion ingresada")
        print("")

    def agregarBicicleta(self):
        # Ingreso de datos de la bicicleta
        patente = input("Ingrese patente: ").strip()
        while validarPatente(patente, listapatentes) == False:
            print("La patente ya existe o el formato es incorrecto, la patente debe ser un numero")
            print("")
            patente = input("Ingrese patente: ").strip()
        modelo = input("Ingrese modelo: ").strip()
        estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
        while validarEstacionActual(estacionactual, listanombres, empresa.estaciones) == False:
            print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
            print("")
            estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ").strip()
        cantusos = 0
        # Agregado de patente a la lista de patentes
        listapatentes.append(patente)
        # Agregado de bicicleta al diccionario de bicicletas
        empresa.bicicletas[patente] = Bicicleta(patente, modelo, estacionactual, cantusos)
        # Suma uno a cantbicidiponible de la estacion actual
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

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nPuesto {} \nCbu: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.puesto, self.cbu)
