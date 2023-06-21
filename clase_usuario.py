from clase_estacion import *
from clase_alquiler import *
from clase_bicicleta import *
from clase_empresa import *
from datetime import datetime
from datetime import date

class Usuario:
    """Manejo de datos de los usuarios.

    Methods:
        validarUsuario: Validación de usuario.
        validarContrasena: Validación de contrasena.
        validarDni: Validación de dni.
        validarFecha: Validación de fecha.
        validarTelefono: Validación de teléfono.
        validarMail: Validación de mail.
        validarEstacionActual: Validación de estación actual.
        cambio: Cambio de datos.

    Returns:
        String: Lista con los atributos del usuario.

    """
    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None):
        """_summary_

        Args:
            usuario (String): Usuario.
            contrasena (String): Contrasena.
            nombre (String): Nombre.
            dni (Int): Dni.
            fecnac (Datetime): Fecha de nacimiento.
            telefono (Int): Teléfono.
            mail (String): Mail.
            direccion (String): Dirección.
        """
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
        """Validación de usuario.

        Args:
            usuario (String): Usuario.
            listausuarios (List): Lista con todos los usuarios.

        Returns:
            Boolean: Validación o no del usuario.
        """
        return usuario.replace(" ","").isalpha() and usuario not in listausuarios
    
    def validarContrasena(self, contrasena):
        """Validación de contrasena.

        Args:
            contrasena (String): Contrasena.

        Returns:
            Boolean: Validación o no de la contrasena.
        """
        return contrasena.replace(" ","").isalpha() and contrasena[0].replace(" ","").isupper()
    
    def validarDni(self, dni, listadnis):
        """Validación del dni.

        Args:
            dni (Int): Dni.
            listadnis (List): Lista con todos los dnis.

        Returns:
            Boolean: Validación o no del dni.
        """
        return dni.isdigit() and len(dni) == 8 and dni not in listadnis

    def validarFecha(self, fecha):
        """Validación de fecha.

        Args:
            fecha (Datetime): Fecha.

        Returns:
            Boolean: Validación o no de la fecha.
        """
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
        """Validación de teléfono.

        Args:
            telefono (Int): Teléfono.

        Returns:
            Boolean: Validación o no del teléfono.
        """
        return telefono.isdigit() and len(telefono) == 10

    def validarMail(self, mail):
        """Validación de mail.

        Args:
            mail (String): Mail.

        Returns:
            Boolean: Validación o no del mail.
        """
        return "@" in mail

    def validarEstacionActual(self, estacionactual, listaestaciones, diccionariodatosestaciones):
        """Validación de estación actual.

        Args:
            estacionactual (String): Nombre de la estación.
            listaestaciones (List): Lista con todos los nombres de las estaciones.
            diccionariodatosestaciones (Dict): Diccionario de las estaciones.

        Returns:
            Boolean: Validación o no de la estación.
        """
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
        """Cambio de datos.

        Args:
            tipo (String): Cliente o trabajador.
            diccionario (Dict): Diccionario de clientes o trabajadores.
            
        """
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
                self.cambioTarjeta()
            else:
                cambiado = "No"
                print("")
                print("No se encontro el dato")
                print("")
        elif eleccioncambio == "puesto":
            if tipo == "Trabajador":
                self.cambioPuesto()
            else:
                cambiado = "No"
                print("")
                print("No se encontro el dato")
                print("")
        elif eleccioncambio == "cbu":
            if tipo == "Trabajador":
                self.cambioCbu()
            else:
                cambiado = "No"
                print("")
                print("No se encontro el dato")
                print("")
        else:
            cambiado = "No"
            print("")
            print("No se encontro el dato")
            print("")
        if cambiado == "Si":
            print("")
            print("Cambio realizado")
            print("")

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion)
