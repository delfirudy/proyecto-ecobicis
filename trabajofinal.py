### DEFINICION CLASES ###


class persona:
    def __init__(self, nombre, dni, fecnac, telefono, mail, direccion):
        self.nombre = nombre
        self.dni = dni
        self.fecnac = fecnac
        self.telefono = telefono
        self.mail = mail
        self.direccion = direccion


class usuario(persona):
    def __init__(self, nombre, dni, fecnac, telefono, mail, direccion, tarjeta):
        persona.__init__(self, nombre, dni, fecnac, telefono, mail, direccion)
        self.tarjeta = tarjeta
        self.listausuario = [nombre, dni, fecnac, telefono, mail, direccion, tarjeta]


class trabajador(persona):
    def __init__(self, nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu):
        persona.__init__(self, nombre, dni, fecnac, telefono, mail, direccion)
        self.puesto = puesto
        self.cbu = cbu
        self.listatrabajador = [
            nombre,
            dni,
            fecnac,
            telefono,
            mail,
            direccion,
            puesto,
            cbu,
        ]


class estacion:
    def __init__(self, nombre, direccion, barrio, cantbicitotal, cantbicidisponible=0):
        self.nombre = nombre
        self.direccion = direccion
        self.barrio = barrio
        self.cantbicitotal = cantbicitotal
        self.cantbicidisponible = cantbicidisponible
        self.listaestacion = [
            nombre,
            direccion,
            barrio,
            cantbicitotal,
            cantbicidisponible,
        ]


class bicicleta:
    def __init__(self, patente, modelo, anno, cantusos=0):
        self.patente = patente
        self.modelo = modelo
        self.anno = anno
        self.cantusos = cantusos
        self.listabicicleta = [patente, modelo, anno, cantusos]


class alquiler(usuario, bicicleta):
    def __init__(
        self,
        nombre,
        patente,
        codigo,
        fecyhora,
        duracion,
        estacionsalida,
        estacionllegada,
    ):
        usuario.__init__(self, nombre)
        bicicleta.__init__(self, patente)
        self.codigo = codigo
        self.fecyhora = fecyhora
        self.duracion = duracion
        self.estacionsalida = estacionsalida
        self.estacionllegada = estacionllegada


class empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = []
        self.usuarios = []
        self.estaciones = []
        self.bicicletas = []


empresaa = empresa("Ecobicis")


### DEFINICION FUNCIONES ###


def ingresousuario():
    nombre = input("Ingrese nombre: ")
    dni = input("Ingrese dni: ")
    fecnac = input("Ingrese fecha de nacimiento: ")
    telefono = input("Ingrese telefono: ")
    mail = input("Ingrese mail: ")
    direccion = input("Ingrese direccion: ")
    tarjeta = input("Ingrese tarjeta: ")
    print("")
    usuarioo = usuario(nombre, dni, fecnac, telefono, mail, direccion, tarjeta)
    empresaa.usuarios.append(usuarioo.listausuario)
    print("Ingreso de datos realizado")
    print("")


def ingresotrabajador():
    nombre = input("Ingrese nombre: ")
    dni = input("Ingrese dni: ")
    fecnac = input("Ingrese fecha de nacimiento: ")
    telefono = input("Ingrese telefono: ")
    mail = input("Ingrese mail: ")
    direccion = input("Ingrese direccion: ")
    puesto = input("Ingrese puesto: ")
    cbu = input("Ingrese cbu: ")
    print("")
    trabajadorr = trabajador(
        nombre, dni, fecnac, telefono, mail, direccion, puesto, cbu
    )
    empresaa.trabajadores.append(trabajadorr.listatrabajador)
    print("Ingreso de datos realizado")
    print("")


def validacionusuario():
    global x
    dni = input("Ingrese dni: ")
    for i in empresaa.usuarios:
        if i[1] == dni:
            x = 1
    return


def alquilar():
    pass


def cambiousuario():
    pass


def mostrarinfo():
    print(empresaa.estaciones)


def validaciontrabajador():
    global y
    dni = input("Ingrese dni: ")
    for i in empresaa.trabajadores:
        if i[1] == dni:
            y = 1


def ingresoestacion():
    nombre = input("Ingrese nombre: ")
    direccion = input("Ingrese direccion: ")
    barrio = input("Ingrese barrio: ")
    cantbicitotal = input("Ingrese capacidad: ")
    print("")
    estacionn = estacion(nombre, direccion, barrio, cantbicitotal)
    empresaa.estaciones.append(estacionn.listaestacion)
    print("Ingreso de datos realizado")
    print("")


def ingresobicicleta():
    patente = input("Ingrese patente: ")
    modelo = input("Ingrese modelo: ")
    anno = input("Ingrese anno: ")
    print("")
    bicicletaa = bicicleta(patente, modelo, anno)
    empresaa.bicicletas.append(bicicletaa.listabicicleta)
    print("Ingreso de datos realizado")
    print("")


def cambiotrabajador():
    pass


### DEFINICION CLASE MAIN ###


class main:
    seguir = "seguir"
    while seguir == "seguir":
        print("1. Ingreso de datos usuario")
        print("2. Ingreso de datos trabajador")
        print("3. Opciones usuario")
        print("4. Opciones trabajador")
        print("5. Salir")
        print("")
        eleccion = input("Ingrese opcion: ")
        print("")
        if eleccion == "1":
            ingresousuario()
        elif eleccion == "2":
            ingresotrabajador()
        elif eleccion == "3":
            x = 0
            validacionusuario()
            if x == 1:
                print("1. Alquilar")
                print("2. Cambiar datos")
                print("3. Informacion")
                print("")
                eleccionusuario = input("Ingrese opcion: ")
                print("")
                if eleccionusuario == "1":
                    alquilar()
                elif eleccionusuario == "2":
                    cambiousuario()
                elif eleccionusuario == "3":
                    mostrarinfo()
                else:
                    print("Ingreso incorrecto de opcion")
                    print("")
            else:
                print("El usuario no existe")
                print("")
        elif eleccion == "4":
            y = 0
            validaciontrabajador()
            if y == 1:
                print("1. Ingresar estacion")
                print("2. Ingresar bicicleta")
                print("3. Cambiar datos")
                print("")
                elecciontrabajador = input("Ingrese opcion:")
                print("")
                if elecciontrabajador == "1":
                    ingresoestacion()
                elif elecciontrabajador == "2":
                    ingresobicicleta()
                elif elecciontrabajador == "3":
                    cambiotrabajador()
                else:
                    print("Ingreso incorrecto de opcion")
                    print("")
            else:
                print("El trabajador no existe")
                print("")
        elif eleccion == "5":
            exit()
        else:
            print("Ingreso incorrecto de opcion")
            print("")


trabajofinal = main()
