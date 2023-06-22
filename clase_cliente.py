from clase_usuario import *

class Cliente(Usuario):
    """Manejo de datos de los clientes.
    Returns:
        Class object: Cliente.
    """
    def __init__(self, usuario=None, contrasena=None, nombre=None, dni=0, fecnac=None, telefono=0, mail=None, direccion=None, tarjeta=0):    
        """Ingreso de datos.
        Args:
            usuario (String): Usuario del cliente.
            contrasena (String): Contrasena del cliente.
            nombre (String): Nombre del cliente.
            dni (Int): Dni del cliente.
            fecnac (Datetime): Fecha de nacimiento del cliente.
            telefono (Int): Teléfono del cliente.
            mail (String): Mail del cliente.
            direccion (String): Dirección del cliente.
            tarjeta (Int): Tarjeta del cliente.
        Returns:
            None
        """
        Usuario.__init__(self, usuario, contrasena, nombre, dni, fecnac, telefono, mail, direccion)
        tarjeta = input("Ingrese tarjeta: ").strip()
        print("")
        while self.validarTarjeta(tarjeta, empresa.listatarjetas) == False:
            print("La tarjeta ya existe o el formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
            print("")
            tarjeta = input("Ingrese tarjeta: ").strip()
            print("")
        self.tarjeta = tarjeta
        empresa.listatarjetas.append(tarjeta)
        empresa.clientes[self.id] = self
        print("Cliente ingresado")
        print("")

    def validarTarjeta(self, tarjeta, listatarjetas):
        """Validación de tarjeta.
        Args:
            tarjeta (Int): Tarjeta del cliente.
            listatarjetas (List): Lista con todas las tarjetas.
        Returns:
            Boolean: Validación o no de la tarjeta.
        """
        return tarjeta.isdigit() and len(tarjeta) == 16 and tarjeta not in listatarjetas
    
    def validarEstacionSalida(self, nombre, listaestaciones, diccionariodatosestaciones):
        """Validación de estación salida.
        Args:
            nombre (String): Nombre de la estación.
            listaestaciones (List): Lista de nombres de las estaciones.
            diccionariodatosestaciones (Dict): Diccionario con todas las estaciones.
        Returns:
            Boolean: Validación o no de estación.
        """
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

    def validarHoraInicio(self, hora):
        """Validación formato hora inicio.
        Args:
            hora (Time): Horas y minutos.
        Returns:
            Boolean: Validación o no de la hora.
        """
        try:
            datetime.strptime(hora, '%H:%M')
            return True
        except ValueError:
            print("El formato es incorrecto, la hora debe ser de la forma HH:mm")
            return False
        
    def validarHoraFin(self, inicio, fin):
        """Validación formato y posterioridad hora fin.
        Args:
            inicio (Time): Horas y minutos de inicio.
            fin (Time): Horas y minutos de fin.
        Returns:
            Boolean: Validación o no de la hora.
        """
        try:
            datetime.strptime(fin, '%H:%M')
            return inicio < fin
        except ValueError:
            return False
        
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
            if fecha_valida >= fecha_actual:
                return True
            else:
                print("El formato es correcto pero la fecha no es posterior a la actual")
                print("")
                return False
        except ValueError:
            print("El formato es incorrecto, la fecha debe ser de la forma YYYY/MM/DD")
            print("")
            return False

    def cambioTarjeta(self):
        """Cambio de atributo tarteja.
        Args:
            None
        Returns:
            None
        """
        tarjeta = input("Ingrese tarjeta: ").strip()
        print("")
        while self.validarTarjeta(tarjeta, empresa.listatarjetas) == False:
            print("La tarjeta ya existe o el formato es incorrecto, la tarjeta debe ser un numero de 16 digitos")
            print("")
            tarjeta = input("Ingrese tarjeta: ").strip()
            print("")
        posicion = empresa.listatarjetas.index(self.tarjeta)
        empresa.listatarjetas[posicion] = tarjeta
        self.tarjeta = tarjeta

    def eliminar(self):
        """Eliminación de cliente.
        Args:
            None
        Returns:
            None
        """
        condicion = "Si"
        for alquiler in empresa.alquileres:
            if alquiler.usuario == self.usuario and alquiler.estado == "en curso":
                condicion = "No"
                break
        if condicion == "Si":
            empresa.clientes.pop(self.id)
            empresa.listadnis.remove(self.dni)
            empresa.listatarjetas.remove(self.tarjeta)
            empresa.listausuarios.remove(self.usuario)
            print("Cliente eliminado")
            print("")
        else:
            print("Usted tiene un alquiler en progreso, finalicelo para eliminar su usuario")
            print("")
    
    def alquilar(self):
        """Alquiler de bicicleta.
        Args:
            None
        Returns:
            None
        """
        validado = "Si"
        for alquiler in empresa.alquileres.values():
            if alquiler.usuario == self.nombre and alquiler.estado == "en curso":
                validado = "No"
                break
        if validado == "Si":
            fecha = input("Ingrese fecha del alquiler: ").strip()
            print("")
            while self.validarFecha(fecha) == False:
                fecha = input("Ingrese fecha del alquiler: ").strip() 
                print("")
            inicio = input("Ingrese hora de inicio: ").strip()
            print("")
            while self.validarHoraInicio(inicio) == False:
                inicio = input("Ingrese hora de inicio: ").strip()
                print("")
            estacionsalida = input("Ingrese estacion de salida: ").strip()
            print("")
            while self.validarEstacionSalida(estacionsalida, empresa.listanombres, empresa.estaciones) == False:
                print("No se encontro la estacion, no hay bicicletas o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
                print("")
                estacionsalida = input("Ingrese estacion de salida: ").strip()
                print("")
            empresa.alquileres[(Alquiler.id)] = Alquiler(self.nombre, fecha, inicio, "0", "0", estacionsalida, " ", "en curso")
            estacion = empresa.estaciones.get(estacionsalida)
            estacion.cantbicidisponible -= 1 
            print("Alquiler ingresado")
            print("")
        else:
            print("Ya tiene un alquiler en curso")
            print("")

    def finalizarAlquiler(self):
        """Finalización de alquiler de bicicleta.
        Args:
            None
        Returns:
            None
        """
        validado = "No"
        for alquiler in empresa.alquileres.values():
            if alquiler.usuario == self.nombre and alquiler.estado == "en curso":
                validado = "Si"
                alquiler_actual = alquiler
                break
        if validado == "Si":
            fin = input("Ingrese hora de finalizacion: ").strip()
            print("")
            while self.validarHoraFin(alquiler_actual.inicio, fin) == False:
                print("El formato es incorrecto o la hora de finalizacion es anterior a la hora de inicio, la hora debe ser de la forma HH:mm")
                print("")
                fin = input("Ingrese hora de finalizacion: ").strip()
                print("")
            duracion = datetime.strptime(fin, '%H:%M') - datetime.strptime(alquiler_actual.inicio, '%H:%M')
            estacionllegada = input("Ingrese estacion de llegada: ").strip()
            print("")
            while self.validarEstacionActual(estacionllegada, empresa.listanombres, empresa.estaciones) == False:
                print("No se encontro la estacion, no hay lugar para dejar la bicicleta o el formato es incorrecto, el nombre debe contener solo letras y la primera debe ser mayuscula")
                print("")
                estacionllegada = input("Ingrese estacion de llegada: ").strip()
                print("")
            estacion = empresa.estaciones.get(estacionllegada)
            estacion.cantbicidisponible += 1
            for bicicleta in empresa.bicicletas.values():
                if bicicleta.estacionactual == alquiler_actual.estacionsalida:
                    bicicleta.cantusos += 1
                    bicicleta.estacionactual = estacionllegada
                    break
            alquiler_actual.finalizar(fin, duracion, estacionllegada) 
        else:
            print("No tiene alquileres en curso")
            print("")

    def mostrarInfo(self):
        """Información sobre las estaciones.
        Args:
            None
        Returns:
            None
        """
        for estacion in empresa.estaciones.values():
            print(estacion)
            print("")

    def __str__(self):
        return "Usuario: {} \nContrasena: {} \nNombre: {} \nDni: {} \nFecha de nacimiento: {} \nTelefono: {} \nMail: {} \nDireccion: {} \nTarjeta: {}".format(self.usuario, self.contrasena, self.nombre, self.dni, self.fecnac, self.telefono, self.mail, self.direccion, self.tarjeta)
