
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox


class MainWindow(QMainWindow):






    # VENTANA PRINCIPAL
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ecobicis")
        self.setGeometry(300, 300, 350, 440)

        self.button1 = QPushButton("Ingreso de datos cliente", self)
        self.button1.setGeometry(50, 50, 250, 30)
        self.button1.clicked.connect(self.menu_ingreso_cliente)

        self.button2 = QPushButton("Ingreso de datos trabajador", self)
        self.button2.setGeometry(50, 90, 250, 30)
        self.button2.clicked.connect(self.menu_ingreso_trabajador)

        self.button3 = QPushButton("Opciones cliente", self)
        self.button3.setGeometry(50, 130, 250, 30)
        self.button3.clicked.connect(self.menu_opciones_cliente)

        self.button4 = QPushButton("Opciones trabajador", self)
        self.button4.setGeometry(50, 170, 250, 30)
        self.button4.clicked.connect(self.menu_opciones_trabajador)

        self.button5 = QPushButton("Salir", self)
        self.button5.setGeometry(50, 210, 250, 30)
        self.button5.clicked.connect(self.close)






    # VENTANA SECUNDARIA INGRESO CLIENTE
    def menu_ingreso_cliente(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingreso de datos cliente")
        dialog.setGeometry(300, 300, 350, 440)

        usuario_label = QLabel("Usuario", dialog)
        usuario_label.setGeometry(50, 30, 150, 20)
        self.usuario_input_box = QLineEdit(dialog)
        self.usuario_input_box.setGeometry(200, 30, 100, 20)

        contrasena_label = QLabel("Contrasena", dialog)
        contrasena_label.setGeometry(50, 60, 150, 20)
        self.contrasena_input_box = QLineEdit(dialog)
        self.contrasena_input_box.setGeometry(200, 60, 100, 20)

        nombre_label = QLabel("Nombre", dialog)
        nombre_label.setGeometry(50, 90, 150, 20)
        self.nombre_input_box = QLineEdit(dialog)
        self.nombre_input_box.setGeometry(200, 90, 100, 20)

        dni_label = QLabel("Dni", dialog)
        dni_label.setGeometry(50, 120, 150, 20)
        self.dni_input_box = QLineEdit(dialog)
        self.dni_input_box.setGeometry(200, 120, 100, 20)

        fecha_label = QLabel("Fecha de nacimiento", dialog)
        fecha_label.setGeometry(50, 150, 150, 20)
        self.fecha_input_box = QLineEdit(dialog)
        self.fecha_input_box.setGeometry(200, 150, 100, 20)

        telefono_label = QLabel("Telefono", dialog)
        telefono_label.setGeometry(50, 180, 150, 20)
        self.telefono_input_box = QLineEdit(dialog)
        self.telefono_input_box.setGeometry(200, 180, 100, 20)

        mail_label = QLabel("Mail", dialog)
        mail_label.setGeometry(50, 210, 150, 20)
        self.mail_input_box = QLineEdit(dialog)
        self.mail_input_box.setGeometry(200, 210, 100, 20)

        direccion_label = QLabel("Direccion", dialog)
        direccion_label.setGeometry(50, 240, 150, 20)
        self.direccion_input_box = QLineEdit(dialog)
        self.direccion_input_box.setGeometry(200, 240, 100, 20)

        tarjeta_label = QLabel("Tarjeta", dialog)
        tarjeta_label.setGeometry(50, 270, 150, 20)
        self.tarjeta_input_box = QLineEdit(dialog)
        self.tarjeta_input_box.setGeometry(200, 270, 100, 20)

        ingresar_button = QPushButton("Ingresar", dialog)
        ingresar_button.setGeometry(50, 300, 250, 30)
        ingresar_button.clicked.connect(self.ingreso_cliente)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 340, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingreso_cliente(self):
        usuario = self.usuario_input_box.text()
        contrasena = self.contrasena_input_box.text()
        nombre = self.nombre_input_box.text()
        dni = self.dni_input_box.text()
        fecha = self.fecha_input_box.text()
        telefono = self.telefono_input_box.text()
        mail = self.mail_input_box.text()
        direccion = self.direccion_input_box.text()
        tarjeta = self.tarjeta_input_box.text()

        if self.validacion_ingreso_cliente(usuario, contrasena, nombre, dni, fecha, telefono, mail, direccion, tarjeta) == True: 

            QMessageBox.about(self, "Ingreso de datos cliente", "Ingreso realizado")

    def validacion_ingreso_cliente(self, usuario, contrasena, nombre, dni, fecha, telefono, mail, direccion, tarjeta):

        return True





    # VENTANA SECUNDARIA INGRESO TRABAJADOR    
    def menu_ingreso_trabajador(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingreso de datos trabajador")
        dialog.setGeometry(300, 300, 350, 440)

        usuario_label = QLabel("Usuario", dialog)
        usuario_label.setGeometry(50, 30, 150, 20)
        self.usuario_input_box = QLineEdit(dialog)
        self.usuario_input_box.setGeometry(200, 30, 100, 20)

        contrasena_label = QLabel("Contrasena", dialog)
        contrasena_label.setGeometry(50, 60, 150, 20)
        self.contrasena_input_box = QLineEdit(dialog)
        self.contrasena_input_box.setGeometry(200, 60, 100, 20)

        nombre_label = QLabel("Nombre", dialog)
        nombre_label.setGeometry(50, 90, 150, 20)
        self.nombre_input_box = QLineEdit(dialog)
        self.nombre_input_box.setGeometry(200, 90, 100, 20)

        dni_label = QLabel("Dni", dialog)
        dni_label.setGeometry(50, 120, 150, 20)
        self.dni_input_box = QLineEdit(dialog)
        self.dni_input_box.setGeometry(200, 120, 100, 20)

        fecha_label = QLabel("Fecha de nacimiento", dialog)
        fecha_label.setGeometry(50, 150, 150, 20)
        self.fecha_input_box = QLineEdit(dialog)
        self.fecha_input_box.setGeometry(200, 150, 100, 20)

        telefono_label = QLabel("Telefono", dialog)
        telefono_label.setGeometry(50, 180, 150, 20)
        self.telefono_input_box = QLineEdit(dialog)
        self.telefono_input_box.setGeometry(200, 180, 100, 20)

        mail_label = QLabel("Mail", dialog)
        mail_label.setGeometry(50, 210, 150, 20)
        self.mail_input_box = QLineEdit(dialog)
        self.mail_input_box.setGeometry(200, 210, 100, 20)

        direccion_label = QLabel("Direccion", dialog)
        direccion_label.setGeometry(50, 240, 150, 20)
        self.direccion_input_box = QLineEdit(dialog)
        self.direccion_input_box.setGeometry(200, 240, 100, 20)

        puesto_label = QLabel("Puesto", dialog)
        puesto_label.setGeometry(50, 270, 150, 20)
        self.puesto_input_box = QLineEdit(dialog)
        self.puesto_input_box.setGeometry(200, 270, 100, 20)

        cbu_label = QLabel("Cbu", dialog)
        cbu_label.setGeometry(50, 300, 150, 20)
        self.cbu_input_box = QLineEdit(dialog)
        self.cbu_input_box.setGeometry(200, 300, 100, 20)

        ingresar_button = QPushButton("Ingresar", dialog)
        ingresar_button.setGeometry(50, 330, 250, 30)
        ingresar_button.clicked.connect(self.ingreso_trabajador)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 370, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingreso_trabajador(self):
        usuario = self.usuario_input_box.text()
        contrasena = self.contrasena_input_box.text()
        nombre = self.nombre_input_box.text()
        dni = self.dni_input_box.text()
        fecha = self.fecha_input_box.text()
        telefono = self.telefono_input_box.text()
        mail = self.mail_input_box.text()
        direccion = self.direccion_input_box.text()
        puesto = self.puesto_input_box.text()
        cbu = self.cbu_input_box.text()

        if self.validacion_ingreso_trabajador(usuario, contrasena, nombre, dni, fecha, telefono, mail, direccion, puesto, cbu) == True:

            QMessageBox.about(self, "Ingreso de datos trabajador", "Ingreso realizado")

    def validacion_ingreso_trabajador(self, usuario, contrasena, nombre, dni, fecha, telefono, mail, direccion, puesto, cbu):

        return True





    # VENTANA SECUNDARIA OPCIONES CLIENTE
    def menu_opciones_cliente(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Opciones cliente")
        dialog.setGeometry(300, 300, 350, 440)

        usuario_label = QLabel("Usuario", dialog)
        usuario_label.setGeometry(50, 30, 100, 20)
        self.usuario_input_box = QLineEdit(dialog)
        self.usuario_input_box.setGeometry(150, 30, 100, 20)

        contrasena_label = QLabel("Contraseña", dialog)
        contrasena_label.setGeometry(50, 70, 100, 20)
        self.contrasena_input_box = QLineEdit(dialog)
        self.contrasena_input_box.setGeometry(150, 70, 100, 20)

        validar_button = QPushButton("Validar", dialog)
        validar_button.setGeometry(50, 110, 250, 30)
        validar_button.clicked.connect(self.submenu_opciones_cliente)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 150, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def submenu_opciones_cliente(self):
        usuario = self.usuario_input_box.text()
        contrasena = self.usuario_input_box.text()

        if self.validacion_opciones_cliente(usuario, contrasena) == True:
            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Opciones cliente")
            self.dialog.setGeometry(300, 300, 350, 440)

            alquiler_button = QPushButton("Alquilar", self.dialog)
            alquiler_button.setGeometry(50, 30, 250, 30)
            alquiler_button.clicked.connect(self.alquilar)

            info_button = QPushButton("Informacion", self.dialog)
            info_button.setGeometry(50, 70, 250, 30)
            info_button.clicked.connect(self.mostrar_informacion)

            cambiar_button = QPushButton("Cambiar datos", self.dialog)
            cambiar_button.setGeometry(50, 110, 250, 30)
            cambiar_button.clicked.connect(self.cambiar)

            baja_button = QPushButton("Dar de baja", self.dialog)
            baja_button.setGeometry(50, 150, 250, 30)
            baja_button.clicked.connect(self.dar_baja_cliente)

            volver_button = QPushButton("Volver", self.dialog)
            volver_button.setGeometry(50, 190, 250, 30)
            volver_button.clicked.connect(self.dialog.close)

            self.dialog.exec_()

    def validacion_opciones_cliente(self, usuario, contrasena):

        return True






    # FUNCIONES EN OPCIONES CLIENTE   
    def alquilar(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Alquilar")
        dialog.setGeometry(300, 300, 350, 440)

        fecha_label = QLabel("Fecha", dialog)
        fecha_label.setGeometry(50, 30, 150, 20)
        self.fecha_input_box = QLineEdit(dialog)
        self.fecha_input_box.setGeometry(200, 30, 100, 20)

        duracion_label = QLabel("Duracion", dialog)
        duracion_label.setGeometry(50, 60, 150, 20)
        self.duracion_input_box = QLineEdit(dialog)
        self.duracion_input_box.setGeometry(200, 60, 100, 20)

        salida_label = QLabel("Estacion salida", dialog)
        salida_label.setGeometry(50, 90, 150, 20)
        self.salida_input_box = QLineEdit(dialog)
        self.salida_input_box.setGeometry(200, 90, 100, 20)

        llegada_label = QLabel("Estacion llegada", dialog)
        llegada_label.setGeometry(50, 120, 150, 20)
        self.llegada_input_box = QLineEdit(dialog)
        self.llegada_input_box.setGeometry(200, 120, 100, 20)

        alquilar_button = QPushButton("Alquilar", dialog)
        alquilar_button.setGeometry(50, 160, 250, 30)
        alquilar_button.clicked.connect(self.ingresar_alquiler)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 200, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingresar_alquiler(self):
        fecha = self.fecha_input_box.text()
        duracion = self.duracion_input_box.text()
        salida = self.salida_input_box.text()
        llegada = self.llegada_input_box.text()

        if self.validacion_datos_alquiler(fecha, duracion, salida, llegada) == True:

            QMessageBox.about(self, "Ingreso de datos alquiler", "Alquiler realizado")

    def validacion_datos_alquiler(self, fecha, duracion, salida, llegada):
        
        return True

    def mostrar_informacion(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Informacion")
        dialog.setGeometry(300, 300, 350, 440)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 200, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def cambiar(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Cambiar datos")
        dialog.setGeometry(300, 300, 350, 440)

        viejo_label = QLabel("Dato a cambiar", dialog)
        viejo_label.setGeometry(50, 30, 150, 20)
        self.viejo_input_box = QLineEdit(dialog)
        self.viejo_input_box.setGeometry(200, 30, 100, 20)

        nuevo_label = QLabel("Dato nuevo", dialog)
        nuevo_label.setGeometry(50, 70, 150, 20)
        self.nuevo_input_box = QLineEdit(dialog)
        self.nuevo_input_box.setGeometry(200, 70, 100, 20)

        cambiar_button = QPushButton("Cambiar", dialog)
        cambiar_button.setGeometry(50, 110, 250, 30)
        cambiar_button.clicked.connect(self.ingresar_cambio)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 150, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingresar_cambio(self):
        viejo = self.viejo_input_box.text()
        nuevo = self.nuevo_input_box.text()

        if self.validacion_datos_cambio(viejo, nuevo) == True:

            QMessageBox.about(self, "Cambio de datos", "Cambio realizado")

    def validacion_datos_cambio(self, viejo, nuevo):
        
        return True

    def dar_baja_cliente(self):
        QMessageBox.about(self, "Dar de baja", "Baja realizada")

        self.dialog.close()






    # VENTANA SECUNDARIA OPCIONES TRABAJADOR
    def menu_opciones_trabajador(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Opciones trabajador")
        dialog.setGeometry(300, 300, 350, 440)

        usuario_label = QLabel("Usuario", dialog)
        usuario_label.setGeometry(50, 30, 100, 20)
        self.usuario_input_box = QLineEdit(dialog)
        self.usuario_input_box.setGeometry(150, 30, 100, 20)

        contrasena_label = QLabel("Contraseña", dialog)
        contrasena_label.setGeometry(50, 70, 100, 20)
        self.contrasena_input_box = QLineEdit(dialog)
        self.contrasena_input_box.setGeometry(150, 70, 100, 20)

        validate_button = QPushButton("Validar", dialog)
        validate_button.setGeometry(50, 110, 250, 30)
        validate_button.clicked.connect(self.submenu_opciones_trabajador)
    
        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 150, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def submenu_opciones_trabajador(self):
        usuario = self.usuario_input_box.text()
        contrasena = self.contrasena_input_box.text()

        if self.validacion_opciones_trabajador(usuario, contrasena) == True:
            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Opciones trabajador")
            self.dialog.setGeometry(300, 300, 350, 440)

            estacion_button = QPushButton("Ingresar estacion", self.dialog)
            estacion_button.setGeometry(50, 30, 250, 30)
            estacion_button.clicked.connect(self.estacion)

            bicicleta_button = QPushButton("Ingresar bicicleta", self.dialog)
            bicicleta_button.setGeometry(50, 70, 250, 30)
            bicicleta_button.clicked.connect(self.bicicleta)

            cambiar_button = QPushButton("Cambiar datos", self.dialog)
            cambiar_button.setGeometry(50, 110, 250, 30)
            cambiar_button.clicked.connect(self.cambiar_menu)

            baja_button = QPushButton("Dar de baja", self.dialog)
            baja_button.setGeometry(50, 150, 250, 30)
            baja_button.clicked.connect(self.baja_menu)
    
            volver_button = QPushButton("Volver", self.dialog)
            volver_button.setGeometry(50, 190, 250, 30)
            volver_button.clicked.connect(self.dialog.close)

            self.dialog.exec_()

    def validacion_opciones_trabajador(self, usuario, contrasena):

        return True






    # FUNCIONES EN OPCIONES TRABAJADOR
    def estacion(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingresar estacion")
        dialog.setGeometry(300, 300, 350, 440)

        nombre_label = QLabel("Nombre", dialog)
        nombre_label.setGeometry(50, 30, 150, 20)
        self.nombre_input_box = QLineEdit(dialog)
        self.nombre_input_box.setGeometry(200, 30, 100, 20)

        direccion_label = QLabel("Direccion", dialog)
        direccion_label.setGeometry(50, 60, 150, 20)
        self.direccion_input_box = QLineEdit(dialog)
        self.direccion_input_box.setGeometry(200, 60, 100, 20)

        barrio_label = QLabel("Barrio", dialog)
        barrio_label.setGeometry(50, 90, 150, 20)
        self.barrio_input_box = QLineEdit(dialog)
        self.barrio_input_box.setGeometry(200, 90, 100, 20)

        capacidad_label = QLabel("Capacidad", dialog)
        capacidad_label.setGeometry(50, 120, 150, 20)
        self.capacidad_input_box = QLineEdit(dialog)
        self.capacidad_input_box.setGeometry(200, 120, 100, 20)

        ingresar_button = QPushButton("Ingresar", dialog)
        ingresar_button.setGeometry(50, 150, 250, 30)
        ingresar_button.clicked.connect(self.ingresar_estacion)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 190, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingresar_estacion(self):
        nombre = self.nombre_input_box.text()
        direccion = self.direccion_input_box.text()
        barrio = self.barrio_input_box.text()
        capacidad = self.capacidad_input_box.text()

        if self.validacion_ingreso_estacion(nombre, direccion, barrio, capacidad) == True: 

            QMessageBox.about(self, "Ingreso de datos estacion", "Ingreso realizado")

    def validacion_ingreso_estacion(self, nombre, direccion, barrio, capacidad):

        return True

    def bicicleta(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingresar bicicleta")
        dialog.setGeometry(300, 300, 350, 440)

        patente_label = QLabel("Patente", dialog)
        patente_label.setGeometry(50, 30, 150, 20)
        self.patente_input_box = QLineEdit(dialog)
        self.patente_input_box.setGeometry(200, 30, 100, 20)

        modelo_label = QLabel("Modelo", dialog)
        modelo_label.setGeometry(50, 60, 150, 20)
        self.modelo_input_box = QLineEdit(dialog)
        self.modelo_input_box.setGeometry(200, 60, 100, 20)

        actual_label = QLabel("Estacion actual", dialog)
        actual_label.setGeometry(50, 90, 150, 20)
        self.actual_input_box = QLineEdit(dialog)
        self.actual_input_box.setGeometry(200, 90, 100, 20)

        ingresar_button = QPushButton("Ingresar", dialog)
        ingresar_button.setGeometry(50, 130, 250, 30)
        ingresar_button.clicked.connect(self.ingresar_bicicleta)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 170, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingresar_bicicleta(self):
        patente = self.patente_input_box.text()
        modelo = self.modelo_input_box.text()
        actual = self.actual_input_box.text()

        if self.validacion_ingreso_bicicleta(patente, modelo, actual) == True: 

            QMessageBox.about(self, "Ingreso de datos bicicleta", "Ingreso realizado")

    def validacion_ingreso_bicicleta(self, patente, modelo, actual):

        return True






    # VENTANA CAMBIO DE DATOS DENTRO DE TRABAJADOR
    def cambiar_menu(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Cambiar datos")
        dialog.setGeometry(300, 300, 350, 440)

        trabajador_button = QPushButton("Cambiar datos trabajador", dialog)
        trabajador_button.setGeometry(50, 30, 250, 30)
        trabajador_button.clicked.connect(self.cambiar)

        estacion_button = QPushButton("Cambiar datos estacion", dialog)
        estacion_button.setGeometry(50, 70, 250, 30)
        estacion_button.clicked.connect(self.cambio_estacion)

        bicicleta_button = QPushButton("Cambiar datos bicicleta", dialog)
        bicicleta_button.setGeometry(50, 110, 250, 30)
        bicicleta_button.clicked.connect(self.cambio_bicicleta)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 150, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()






    # FUNCIONES EN CAMBIO DE DATOS TRABAJADOR
    def cambio_estacion(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Cambiar datos")
        dialog.setGeometry(300, 300, 350, 440)

        label = QLabel("Nombre", dialog)
        label.setGeometry(50, 30, 150, 20)

        input_box = QLineEdit(dialog)
        input_box.setGeometry(200, 30, 100, 20)

        cambio_button = QPushButton("Cambiar", dialog)
        cambio_button.setGeometry(50, 70, 250, 30)
        cambio_button.clicked.connect(self.cambiar)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 110, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def cambio_bicicleta(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Cambiar datos")
        dialog.setGeometry(300, 300, 350, 440)

        label = QLabel("Patente", dialog)
        label.setGeometry(50, 30, 150, 20)

        input_box = QLineEdit(dialog)
        input_box.setGeometry(200, 30, 100, 20)

        cambio_button = QPushButton("Cambiar", dialog)
        cambio_button.setGeometry(50, 70, 250, 30)
        cambio_button.clicked.connect(self.cambiar)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 110, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()




    # VENTANA BAJA DE OBJETOS DENTRO DE TRABAJADOR
    def baja_menu(self):
        self.dialog1 = QDialog(self)
        self.dialog1.setWindowTitle("Dar de baja")
        self.dialog1.setGeometry(300, 300, 350, 440)

        trabajador_button = QPushButton("Dar de baja trabajador", self.dialog1)
        trabajador_button.setGeometry(50, 30, 250, 30)
        trabajador_button.clicked.connect(self.dar_baja_trabajador)

        estacion_button = QPushButton("Dar de baja estacion", self.dialog1)
        estacion_button.setGeometry(50, 70, 250, 30)
        estacion_button.clicked.connect(self.baja_estacion)

        bicicleta_button = QPushButton("Dar de baja bicicleta", self.dialog1)
        bicicleta_button.setGeometry(50, 110, 250, 30)
        bicicleta_button.clicked.connect(self.baja_bicicleta)

        volver_button = QPushButton("Volver", self.dialog1)
        volver_button.setGeometry(50, 150, 250, 30)
        volver_button.clicked.connect(self.dialog1.close)

        self.dialog1.exec_()






    # FUNCIONES EN BAJA DE OBJETOS TRABAJADOR
    def baja_estacion(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dar de baja estacion")
        dialog.setGeometry(300, 300, 350, 440)

        label = QLabel("Nombre", dialog)
        label.setGeometry(50, 30, 150, 20)

        input_box = QLineEdit(dialog)
        input_box.setGeometry(200, 30, 100, 20)

        baja_button = QPushButton("Dar de baja", dialog)
        baja_button.setGeometry(50, 70, 250, 30)
        baja_button.clicked.connect(self.dar_baja)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 110, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def baja_bicicleta(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dar de baja bicicleta")
        dialog.setGeometry(300, 300, 350, 440)

        label = QLabel("Patente", dialog)
        label.setGeometry(50, 30, 150, 20)

        input_box = QLineEdit(dialog)
        input_box.setGeometry(200, 30, 100, 20)

        baja_button = QPushButton("Dar de baja", dialog)
        baja_button.setGeometry(50, 70, 250, 30)
        baja_button.clicked.connect(self.dar_baja)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 110, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def dar_baja(self):
        QMessageBox.about(self, "Dar de baja", "Baja realizada")

    def dar_baja_trabajador(self):
        QMessageBox.about(self, "Dar de baja", "Baja realizada")

        self.dialog1.close()
        self.dialog.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("interfaz_estilo.qss").read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
