from clases_funciones import *

class main:
    recorrerpickle()
    print(empresa.clientes)
    seguir = "Seguir"
    while seguir == "Seguir":
        print("1. Ingreso de datos cliente")
        print("2. Ingreso de datos trabajador")
        print("3. Opciones cliente")
        print("4. Opciones trabajador")
        print("5. Salir")
        print("")
        eleccion = input("Ingrese opcion: ").strip()
        print("")
        if eleccion == "1":
            Cliente()
        elif eleccion == "2":
            Trabajador()
        elif eleccion == "3":
            usuario1 = input("Ingrese usuario: ").strip()
            contrasena1 = input("Ingrese contrasena: ").strip()
            print("")
            validacioncliente = 0
            for cliente in empresa.clientes:
                if cliente.usuario == usuario1 and cliente.contrasena == contrasena1:
                    validacioncliente = 1
                    print("Cliente validado")
                    print("")
                    seguir1 = "Seguir"
                    while seguir1 == "Seguir":
                        print("1. Alquilar")
                        print("2. Información sobre estaciones")
                        print("3. Volver al menu principal")
                        print("")
                        eleccionusuario = input("Ingrese opcion: ").strip()
                        print("")
                        if eleccionusuario == "1":
                            cliente.alquilar()
                        elif eleccionusuario == "2":
                            cliente.mostrarinfo()
                        elif eleccionusuario == "3":
                            seguir1 = "No seguir"
                        else:
                            print("Ingreso incorrecto de opcion")
                            print("")
            if validacioncliente == 0:
                print("El cliente no existe")
                print("")
        elif eleccion == "4":
            usuario2 = input("Ingrese usuario: ").strip()
            contrasena2 = input("Ingrese contrasena: ").strip()
            print("")
            validaciontrabajador = 0
            for trabajador in empresa.trabajadores:
                if trabajador.nombre == usuario2 and trabajador.contrasena == contrasena2:
                    validaciontrabajador = 1
                    print("Trabajador validado")
                    print("")
                    seguir2 = "Seguir"
                    while seguir2 == "Seguir":
                        print("1. Ingresar estacion")
                        print("2. Ingresar bicicleta")
                        print("3. Volver al menu principal")
                        print("")
                        elecciontrabajador = input("Ingrese opcion: ").strip()
                        print("")
                        if elecciontrabajador == "1":
                            trabajador.agregarestacion()
                        elif elecciontrabajador == "2":
                            trabajador.agregarbicicleta()
                        elif elecciontrabajador == "3":
                            seguir2 = "No seguir"
                        else:
                            print("Ingreso incorrecto de opcion")
                            print("")
            if validaciontrabajador == 0:
                print("El trabajador no existe")
                print("")
        elif eleccion == "5":
            actualizarpickle()
            exit()
        else:
            print("Ingreso incorrecto de opcion")
            print("")

trabajofinal = main()
