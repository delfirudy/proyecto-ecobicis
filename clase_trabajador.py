from clase_usuario import *

class Trabajador(Usuario):
    """Manejo de datos de los trabajadores.

    Methods:
        validarPuesto: Validación de puesto.
        validarCbu: Validación de cbu.
        cambioPuesto: Cambio del atributo puesto.
        cambioCbu: Cambio del atributo cbu.
        eliminar: Eliminación del trabajador
        agregarEstación: Ingreso de datos de nueva estación.
        agregarBicicleta: Ingreso de datos de nueva bicicleta.
        cambiarEstación: Cambio de datos de estación.
        cambiarBicicleta: Cambio de datos de bicicleta.
        eliminarEstacion: Eliminación de estación.
        eliminarBicicleta: Eliminación de bicicleta.

    Returns:
        String: Lista con los atributos del trabajador.

    """
    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None, puesto=None, cbu=0):
        """Ingreso de datos.

        Args:
            usuario (String): Usuario del trabajador.
            contrasena (String): Contrasena del trabajador.
            nombre (String): Nombre del trabajador.
            dni (Int): Dni del trabajador.
            fecnac (Datetime): Fecha de nacimiento del trabajador.
            telefono (Int): Telefono del trabajador.
            mail (String): Mail del trabajador.
            direccion (String): Dirección del trabajador.
            puesto (String): Puesto laboral del trabajador.
            cbu (Int): Cbu del trabajador.

        """
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
        """Validación de puesto laboral.

        Args:
            puesto (String): Puesto laboral del trabajador.

        Returns:
            Boolean: Validación o no del puesto laboral.

        """
        return puesto.replace(" ","").isalpha()
    
    def validarCbu(self, cbu, listacbus):
        """Validación del cbu.

        Args:
            cbu (Int): Cbu del trabajador.
            listacbus (List): Lista con todos los cbus.

        Returns:
            Boolean: Validación o no del cbu.
        """
        return cbu.isdigit() and len(cbu) == 22 and cbu not in listacbus

    def cambioPuesto(self):
        """Cambio del atributo puesto."""
        puesto = input("Ingrese puesto: ").strip()
        while self.validarPuesto(puesto) == False:
            print("El formato es incorrecto, el puesto debe contener solo letras")
            print("")
            puesto = input("Ingrese puesto: ").strip()
        self.puesto = puesto

    def cambioCbu(self):
        """Cambio del atributo cbu."""
        cbu = input("Ingrese cbu: ").strip()
        while self.validarCbu(cbu, empresa.listacbus) == False:
            print("El cbu ya existe o el formato es incorrecto, el cbu debe ser un numero de 22 digitos")
            print("")
            cbu = input("Ingrese cbu: ").strip()
        posicion = empresa.listacbus.index(self.cbu)
        empresa.listacbus[posicion] = cbu
        self.cbu = cbu

    def eliminar(self):
        """Eliminación del trabajador."""
        empresa.trabajadores.pop(self.id)
        empresa.listacbus.remove(self.cbu)
        empresa.listadnis.remove(self.dni)
        empresa.listausuarios.remove(self.usuario)
        print("")
        print("Trabajador eliminado")
        print("")

    def agregarEstacion(self):
        """Ingreso de datos de nueva estación."""
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
        """Ingreso de datos de nueva bicicleta."""
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
        """Cambio de datos de bicicleta."""
        condicion = "Si"
        for alquiler in empresa.alquileres.values():
            if alquiler.estado == "en curso":
                condicion = "No"
                break
        if condicion == "Si":
            patente = input("Ingrese la patente de la bicicleta a modificar: ").strip()
            while validarPatente(patente, empresa.listapatentes) == True:
                print("Patente no encontrada")
                print("")
                patente = input("Ingrese bicicleta a modificar: ").strip()
            bicicleta = empresa.bicicletas.get(patente)
            bicicleta.cambio()
        else:
            print("")
            print("Hay alquileres en curso, espere a que se finalicen para cambiar")
            print("")

    def cambiarEstacion(self):
        """Cambio de datos de estación."""
        condicion = "Si"
        for alquiler in empresa.alquileres.values():
            if alquiler.estado == "en curso":
                condicion = "No"
                break
        if condicion == "Si":
            nombre = input("Ingrese el nombre de la estacion a modificar: ").strip()
            while validarEstacion(nombre, empresa.listanombres) == True:
                print("Estacion no encontrada")
                print("")
                nombre = input("Ingrese el nombre de la estacion a modificar: ").strip()
            estacion = empresa.estaciones.get(nombre)
            estacion.cambio()
        else:
            print("")
            print("Hay alquileres en curso, espere a que se finalicen para cambiar")
            print("")

    def eliminarBicicleta(self):
        """Eliminación de bicicleta."""
        condicion = "Si"
        for alquiler in empresa.alquileres.values():
            if alquiler.estado == "en curso":
                condicion = "No"
                break
        if condicion == "Si":
            patente = input("Ingrese la patente de la bicicleta a eliminar: ").strip()
            while validarPatente(patente, empresa.listapatentes) == True:
                print("Patente no encontrada")
                print("")
                patente = input("Ingrese bicicleta a eliminar: ").strip()
            bicicleta = empresa.bicicletas.get(patente)
            bicicleta.eliminar()
        else:
            print("")
            print("Hay alquileres en curso, espere a que se finalicen para eliminar")
            print("")

    def eliminarEstacion(self):
        "Eliminación de estación."
        condicion = "Si"
        for alquiler in empresa.alquileres.values():
            if alquiler.estado == "en curso":
                condicion = "No"
                break
        if condicion == "Si":
            nombre = input("Ingrese el nombre de la estacion a eliminar: ").strip()
            while validarEstacion(nombre, empresa.listanombres) == True:
                print("Estacion no encontrada")
                print("")
                nombre = input("Ingrese el nombre de la estacion a eliminar: ").strip()
            estacion = empresa.estaciones.get(nombre)
            estacion.eliminar()
        else:
            print("")
            print("Hay alquileres en curso, espere a que se finalicen para eliminar")
            print("")

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nPuesto: {} \nCbu: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.puesto, self.cbu)