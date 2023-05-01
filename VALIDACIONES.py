
#     #fecnac
#     while True:
#         fecha = input("Ingrese una fecha en formato YYYY/MM/DD: ")

#         try:
#             fecha_valida = datetime.strptime(fecha, "%Y/%m/%d").date()
#             fecha_actual = date.today()
#             if fecha_valida < fecha_actual:
#                 print("La fecha ingresada es:", fecha_valida)
#                 fecnac = fecha_valida
#                 break
#             else:
#                 print("La fecha es válida pero no es anterior a la fecha actual.")
#                 continue
#         except ValueError:
#             print("La fecha no tiene el formato esperado. Ingrese la fecha nuevamente.")
#             continue



# # DESCRIPCION
# # Ingreso todos los datos de la estacion
# # Se genera la listaestacion, con todos los datos sobre la estacion
# # Se agrega a estaciones la listaestacion
# def ingresoestacion():
#     nombre = input("Ingrese nombre: ")
#     direccion = input("Ingrese direccion: ")
#     barrio = input("Ingrese barrio: ")
#     cantbicitotal = int(input("Ingrese capacidad: "))
#     print("")
#     estacionn = Estacion(nombre, direccion, barrio, cantbicitotal)
#     empresaa.estaciones.append(estacionn.listaestacion)
#     print("Ingreso de datos realizado")
#     print("")
#     texto = ""
#     for i in estacionn.listaestacion:
#         texto += " " + str(i)
#     f = open("datosestaciones.txt","a")
#     f.write("\n" + texto)
#     f.close()


# # DESCRIPCION
# # Ingreso todos los datos de la bicicleta
# # Si no hay lugar en la estacionactual para guardar la bicicleta se cancela el ingreso y le pide al trabajador que ingrese la bicicleta en otra estacion antes de volver a cargar el ingreso
# # Si hay lugar en la estacionactual hace lo siguiente
# # Se genera la listabicicleta, con todos los datos sobre la bicicleta
# # Se agrega a bicicletas la listabicicleta
# # Se suma 1 a la cantidad disponible de bicicletas en la estacionactual
# def ingresobicicleta():
#     patente = input("Ingrese patente: ")
#     modelo = input("Ingrese modelo: ")
#     anno = input("Ingrese anno: ")
#     estacionactual = input("Ingrese estacion donde se ingresa la bicicleta: ")
#     print("")
#     x = 0
#     for i in empresaa.estaciones:
#         if i[0] == estacionactual:
#             x = 1
#             if i[3] == i[4]:
#                 print("No hay lugar en la estacion, ingrese la bicicleta en otra estacion")
#                 print("")
#             else:
#                 bicicletaa = Bicicleta(patente, modelo, anno, estacionactual)
#                 empresaa.bicicletas.append(bicicletaa.listabicicleta)
#                 i[4] += 1
#                 print("Ingreso de datos realizado")
#                 print("")
#     if x == 0:
#         print("No se encontro la estacion")
#         print("")
#     texto = ""
#     for i in bicicletaa.listabicicleta:
#         texto += " " + str(i)
#     f = open("datosbicicletas.txt","a")
#     f.write("\n" + texto)
#     f.close()


# # DESCRIPCION
# # Ingreso de los datos necesarios para el alquiler
# # Genera codigo del alquiler automaticamente
# # Chequea que existan la patente, estacion de llegada y estacion de salida en las listas
# # Si no hay lugar en la estacion llegada cancela el alquiler y le pide al cliente que deje la bicicleta en otra estacion antes de volver a cargar el alquiler
# # Si hay lugar en la estacion llegada para guardar la bicicleta hace lo siguiente
# # Suma 1 a la cantidad de usos de la bicicleta
# # Resta 1 a la cantidad disponible de bicicletas en la estacion de salida y suma 1 a la cantidad de bicicletas disponible de la estacion llegada
# codigo = 0
# def alquilar(usuario):
#     global codigo
#     patente = input("Ingrese patente de la bicicleta: ")
#     fecyhora = input("Ingrese fecha y hora del alquiler: ")
#     duracion = input("Ingrese duracion del alquiler: ")
#     estacionsalida = input("Ingrese estacion de salida: ")
#     estacionllegada = input("Ingrese estacion de llegada: ")
#     print("")
#     x = 0
#     for i in empresaa.estaciones:
#         if i[0] == estacionllegada:
#             x = 1
#     for n in empresaa.estaciones:
#         if n[0] == estacionsalida:
#             x = 2
#     for k in empresaa.bicicletas:
#         if k[0] == patente:
#             x = 3
#     if x == 3:
#         for m in empresaa.estaciones:
#             if m[0] == estacionllegada:
#                 if m[3] == m[4]:
#                     print("No hay lugar para dejar la bicicleta, dejarla en otra estacion")
#                     print("")
#                 else:
#                     codigo += 1
#                     alquilerr = Alquiler(usuario,patente,codigo,fecyhora,duracion,estacionsalida,estacionllegada)
#                     empresaa.alquileres.append(alquilerr.listaalquiler)
#                     m[4] += 1
#                     for p in empresaa.estaciones:
#                         if p[0] == estacionsalida:
#                             p[4] -= 1
#                     print("Ingreso de alquiler realizado")
#                     print("")
#     else:
#         print("No se encontro patente, estacion de salida o estacion de llegada")
#         print("")
#     texto = ""
#     for i in alquilerr.listaalquiler:
#         texto += " " + str(i)
#     f = open("datosalquileres.txt","a")
#     f.write("\n" + texto)
#     f.close()


# # DESCRIPCION
# # Muestra la informacion de las estaciones, con sus bicicletas
# def mostrarinfo():
#     print(empresaa.estaciones)
#     print("")


# # DESCRIPCION
# # Pide valor actual que se desea cambiar (dato)
# # Pide valor nuevo (cambio)
# # Realiza el cambio de dato y altera todas las listas que lo tienen.
# # Anotacion: Cuando pasemos todo a diccionarios, dato va a ser contrasena, nombre etc. Por ahora es el valor actual
# # No se puede cambiar el usuario
# def cambiocliente(usuario):
#     dato = input("Ingrese dato que desea cambiar: ")
#     for i in empresaa.clientes:
#         if i[0] == usuario:
#             for n in range(1,9):
#                 if i[n] == dato:
#                     cambio = input("Ingrese valor nuevo: ")
#                     print("")
#                     i[n] = cambio
#                     print("Cambio realizado")
#                     print("")


# # DESCRIPCION
# # Pide valor actual que se desea cambiar (dato)
# # Pide valor nuevo (cambio)
# # Realiza el cambio de dato y altera todas las listas que lo tienen.
# # Anotacion: Cuando pasemos todo a diccionarios, dato va a ser contrasena, nombre etc. Por ahora es el valor actual
# # No se puede cambiar el usuario
# def cambiotrabajador(usuario):
#     dato = input("Ingrese que dato quiere cambiar: ")
#     for i in empresaa.trabajadores:
#         if i[0] == usuario:
#             for n in range(1,10):
#                 if i[n] == dato:
#                     cambio = input("Ingrese valor nuevo: ")
#                     print("")
#                     i[n] = cambio
#                     print("Cambio realizado")
#                     print("")
