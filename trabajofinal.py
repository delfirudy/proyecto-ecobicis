from funciones import *

class main:
    recorrertxt()
    seguir = "seguir"
    while seguir == "seguir":
        print("1. Ingreso de datos cliente")
        print("2. Ingreso de datos trabajador")
        print("3. Opciones cliente")
        print("4. Opciones trabajador")
        print("5. Salir")
        print("")
        eleccion = input("Ingrese opcion: ").strip()
        print("")
        if eleccion == "1":
            ingresocliente()
        elif eleccion == "2":
            ingresotrabajador()
        elif eleccion == "3":
            usuario1 = input("Ingrese usuario: ").strip()
            contrasena1 = input("Ingrese contrasena: ").strip()
            print("")
            validacioncliente = 0
            for i in empresaa.clientes:
                if i[0] == usuario1 and i[1] == contrasena1:
                    validacioncliente = 1
                    print("Cliente validado")
                    print("")
                    print("1. Alquilar")
                    print("2. Cambiar datos")
                    print("3. Informacion sobre estaciones")
                    print("")
                    eleccionusuario = input("Ingrese opcion: ").strip()
                    print("")
                    if eleccionusuario == "1":
                        alquilar(usuario1)
                    elif eleccionusuario == "2":
                        cambiocliente(usuario1)
                    elif eleccionusuario == "3":
                        mostrarinfo()
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
            for i in empresaa.trabajadores:
                if i[0] == usuario2 and i[1] == contrasena2:
                    validaciontrabajador = 1
                    print("Trabajador validado")
                    print("")
                    print("1. Ingresar estacion")
                    print("2. Ingresar bicicleta")
                    print("3. Cambiar datos")
                    print("")
                    elecciontrabajador = input("Ingrese opcion: ").strip()
                    print("")
                    if elecciontrabajador == "1":
                        ingresoestacion()
                    elif elecciontrabajador == "2":
                        ingresobicicleta()
                    elif elecciontrabajador == "3":
                        cambiotrabajador(usuario2)
                    else:
                        print("Ingreso incorrecto de opcion")
                        print("")
            if validaciontrabajador == 0:
                print("El trabajador no existe")
                print("")
        elif eleccion == "5":
            actualizartxt()
            exit()
        else:
            print("Ingreso incorrecto de opcion")
            print("")





trabajofinal = main()
