from funciones import *

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
            usuario1 = input("Ingrese usuario: ")
            contrasena1 = input("Ingrese contrasena: ")
            print("")
            validacionusuario(usuario1,contrasena1)
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
                    dato = input("Ingrese dato que desea cambiar: ")
                    cambiousuario(dato,usuario1)
                elif eleccionusuario == "3":
                    mostrarinfo()
                else:
                    print("Ingreso incorrecto de opcion")
                    print("")
            else:
                print("El usuario no existe")
                print("")
        elif eleccion == "4":
            usuario2 = input("Ingrese usuario: ")
            contrasena2 = input("Ingrese contrasena: ")
            print("")
            validaciontrabajador(usuario2,contrasena2)
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
                    dato = input("Ingrese que dato quiere cambiar: ")
                    cambiotrabajador(dato,usuario2)
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
