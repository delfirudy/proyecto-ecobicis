import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton


class MainWindow(QMainWindow):

    # VENTANA PRINCIPAL
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ecobicis")
        self.setGeometry(300, 300, 350, 440)

        self.button1 = QPushButton("Ingreso de datos cliente", self)
        self.button1.setGeometry(50, 50, 250, 30)
        self.button1.clicked.connect(self.show_client_data_dialog)

        self.button2 = QPushButton("Ingreso de datos trabajador", self)
        self.button2.setGeometry(50, 90, 250, 30)
        self.button2.clicked.connect(self.show_worker_data_dialog)

        self.button3 = QPushButton("Opciones cliente", self)
        self.button3.setGeometry(50, 130, 250, 30)
        self.button3.clicked.connect(self.show_client_options_dialog)

        self.button4 = QPushButton("Opciones trabajador", self)
        self.button4.setGeometry(50, 170, 250, 30)
        self.button4.clicked.connect(self.show_worker_options_dialog)

        self.button5 = QPushButton("Salir", self)
        self.button5.setGeometry(50, 210, 250, 30)
        self.button5.clicked.connect(self.close)

    # VENTANA SECUNDARIA INGRESO CLIENTE
    def show_client_data_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingreso de datos cliente")
        dialog.setGeometry(300, 300, 350, 440)

        label_titles = ["Usuario", "Contrasena", "Nombre", "Dni", "Fecha de nacimiento", "Telefono", "Mail", "Direccion", "Tarjeta"]
        for i in range(len(label_titles)):
            label = QLabel(label_titles[i], dialog)
            label.setGeometry(50, 30 + 30 * i, 150, 20)

            input_box = QLineEdit(dialog)
            input_box.setGeometry(200, 30 + 30 * i, 100, 20)

        ingresar_button = QPushButton("Ingresar", dialog)
        ingresar_button.setGeometry(50, 300, 250, 30)
        ingresar_button.clicked.connect(self.ingresar_cliente)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 340, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    # VENTANA SECUNDARIA INGRESO TRABAJADOR    
    def show_worker_data_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingreso de datos trabajador")
        dialog.setGeometry(300, 300, 350, 440)

        label_titles = ["Usuario", "Contrasena", "Nombre", "Dni", "Fecha de nacimiento", "Telefono", "Mail", "Direccion", "Puesto", "Cbu"]
        for i in range(len(label_titles)):
            label = QLabel(label_titles[i], dialog)
            label.setGeometry(50, 30 + 30 * i, 150, 20)

            input_box = QLineEdit(dialog)
            input_box.setGeometry(200, 30 + 30 * i, 100, 20)

        ingresar_button = QPushButton("Ingresar", dialog)
        ingresar_button.setGeometry(50, 330, 250, 30)
        ingresar_button.clicked.connect(self.ingresar_trabajador)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 370, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    # VENTANA SECUNDARIA OPCIONES CLIENTE
    def show_client_options_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Opciones cliente")
        dialog.setGeometry(300, 300, 350, 440)

        username_label = QLabel("Usuario", dialog)
        username_label.setGeometry(50, 30, 100, 20)
        self.username_input = QLineEdit(dialog)
        self.username_input.setGeometry(150, 30, 100, 20)

        password_label = QLabel("Contraseña", dialog)
        password_label.setGeometry(50, 70, 100, 20)
        self.password_input = QLineEdit(dialog)
        self.password_input.setGeometry(150, 70, 100, 20)

        validate_button = QPushButton("Validar", dialog)
        validate_button.setGeometry(50, 110, 250, 30)
        validate_button.clicked.connect(self.validate_client_credentials)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 150, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    # VENTANA SECUNDARIA OPCIONES TRABAJADOR
    def show_worker_options_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Opciones trabajador")
        dialog.setGeometry(300, 300, 350, 440)

        username_label = QLabel("Usuario", dialog)
        username_label.setGeometry(50, 30, 100, 20)
        self.username_input = QLineEdit(dialog)
        self.username_input.setGeometry(150, 30, 100, 20)

        password_label = QLabel("Contraseña", dialog)
        password_label.setGeometry(50, 70, 100, 20)
        self.password_input = QLineEdit(dialog)
        self.password_input.setGeometry(150, 70, 100, 20)

        validate_button = QPushButton("Validar", dialog)
        validate_button.setGeometry(50, 110, 250, 30)
        validate_button.clicked.connect(self.validate_worker_credentials)
    
        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 150, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    # VENTANAS VALIDACIONES CLIENTE Y TRABAJADOR
    def validate_client_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.validate_credentials(username, password):
            dialog = QDialog(self)
            dialog.setWindowTitle("Opciones cliente")
            dialog.setGeometry(300, 300, 350, 440)

            alquiler_button = QPushButton("Alquilar", dialog)
            alquiler_button.setGeometry(50, 30, 250, 30)
            alquiler_button.clicked.connect(self.alquiler)

            info_button = QPushButton("Informacion", dialog)
            info_button.setGeometry(50, 70, 250, 30)
            info_button.clicked.connect(self.mostrar_informacion)

            cambiar_button = QPushButton("Cambiar datos", dialog)
            cambiar_button.setGeometry(50, 110, 250, 30)
            cambiar_button.clicked.connect(self.cambiar)

            baja_button = QPushButton("Dar de baja", dialog)
            baja_button.setGeometry(50, 150, 250, 30)
            baja_button.clicked.connect(self.dar_baja)

            volver_button = QPushButton("Volver", dialog)
            volver_button.setGeometry(50, 190, 250, 30)
            volver_button.clicked.connect(dialog.close)

            dialog.exec_()

    def validate_worker_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.validate_credentials(username, password):
            dialog = QDialog(self)
            dialog.setWindowTitle("Opciones trabajador")
            dialog.setGeometry(300, 300, 350, 440)

            estacion_button = QPushButton("Ingresar estacion", dialog)
            estacion_button.setGeometry(50, 30, 250, 30)
            estacion_button.clicked.connect(self.estacion)

            bicicleta_button = QPushButton("Ingresar bicicleta", dialog)
            bicicleta_button.setGeometry(50, 70, 250, 30)
            bicicleta_button.clicked.connect(self.bicicleta)

            cambiar_button = QPushButton("Cambiar datos", dialog)
            cambiar_button.setGeometry(50, 110, 250, 30)
            cambiar_button.clicked.connect(self.cambiar_menu)

            baja_button = QPushButton("Dar de baja", dialog)
            baja_button.setGeometry(50, 150, 250, 30)
            baja_button.clicked.connect(self.baja_menu)
    
            volver_button = QPushButton("Volver", dialog)
            volver_button.setGeometry(50, 190, 250, 30)
            volver_button.clicked.connect(dialog.close)

            dialog.exec_()

    # VENTANAS DENTRO DE TRABAJADOR
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

    def baja_menu(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dar de baja")
        dialog.setGeometry(300, 300, 350, 440)

        trabajador_button = QPushButton("Dar de baja trabajador", dialog)
        trabajador_button.setGeometry(50, 30, 250, 30)
        trabajador_button.clicked.connect(self.dar_baja)

        estacion_button = QPushButton("Dar de baja estacion", dialog)
        estacion_button.setGeometry(50, 70, 250, 30)
        estacion_button.clicked.connect(self.baja_estacion)

        bicicleta_button = QPushButton("Dar de baja bicicleta", dialog)
        bicicleta_button.setGeometry(50, 110, 250, 30)
        bicicleta_button.clicked.connect(self.baja_bicicleta)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 150, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    # FUNCIONES PRINCIPALES

    def validate_credentials(self, username, password):

        # Aca el codigo de validacion de trabajador y cliente

        return True

    def alquiler(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Alquilar")
        dialog.setGeometry(300, 300, 350, 440)

        label_titles = ["Fecha", "Duracion", "Estacion salida", "Estacion llegada"]
        for i in range(len(label_titles)):
            label = QLabel(label_titles[i], dialog)
            label.setGeometry(50, 30 + 30 * i, 150, 20)

            input_box = QLineEdit(dialog)
            input_box.setGeometry(200, 30 + 30 * i, 100, 20)

        alquilar_button = QPushButton("Alquilar", dialog)
        alquilar_button.setGeometry(50, 160, 250, 30)
        alquilar_button.clicked.connect(self.ingresar_alquiler)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 200, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def estacion(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingresar estacion")
        dialog.setGeometry(300, 300, 350, 440)

        label_titles = ["Nombre", "Direccion", "Barrio", "Capacidad"]
        for i in range(len(label_titles)):
            label = QLabel(label_titles[i], dialog)
            label.setGeometry(50, 30 + 30 * i, 150, 20)

            input_box = QLineEdit(dialog)
            input_box.setGeometry(200, 30 + 30 * i, 100, 20)

        ingresar_button = QPushButton("Ingresar", dialog)
        ingresar_button.setGeometry(50, 150, 250, 30)
        ingresar_button.clicked.connect(self.ingresar_estacion)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 190, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def bicicleta(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingresar bicicleta")
        dialog.setGeometry(300, 300, 350, 440)

        label_titles = ["Patente", "Modelo", "Estacion actual"]
        for i in range(len(label_titles)):
            label = QLabel(label_titles[i], dialog)
            label.setGeometry(50, 30 + 30 * i, 150, 20)

            input_box = QLineEdit(dialog)
            input_box.setGeometry(200, 30 + 30 * i, 100, 20)

        ingresar_button = QPushButton("Ingresar", dialog)
        ingresar_button.setGeometry(50, 130, 250, 30)
        ingresar_button.clicked.connect(self.ingresar_bicicleta)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 170, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def cambiar(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Cambiar datos")
        dialog.setGeometry(300, 300, 350, 440)

        label = QLabel("Dato a cambiar", dialog)
        label.setGeometry(50, 30, 150, 20)

        input_box = QLineEdit(dialog)
        input_box.setGeometry(200, 30, 100, 20)

        cambiar_button = QPushButton("Cambiar", dialog)
        cambiar_button.setGeometry(50, 70, 250, 30)
        cambiar_button.clicked.connect(self.cambiar_datos)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 110, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

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

    # FUNCIONES DE AVISO Y EJECUCION
    def ingresar_cliente(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingreso de datos cliente")
        dialog.setGeometry(300, 300, 350, 440)

        # Aca codigo de ingreso de cliente

        label = QLabel("Ingreso realizado", dialog)
        label.setGeometry(50, 30, 150, 20)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 70, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingresar_trabajador(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingreso de datos trabajador")
        dialog.setGeometry(300, 300, 350, 440)

        # Aca codigo de ingreso de trabajador

        label = QLabel("Ingreso realizado", dialog)
        label.setGeometry(50, 30, 150, 20)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 70, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingresar_alquiler(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Alquilar")
        dialog.setGeometry(300, 300, 350, 440)

        # Aca el codigo de ingreso de alquiler

        label = QLabel("Alquiler ingresado", dialog)
        label.setGeometry(50, 30, 150, 20)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 70, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_() 

    def ingresar_estacion(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingresar estacion")
        dialog.setGeometry(300, 300, 350, 440)

        # Aca el codigo de ingreso de estacion

        label = QLabel("Estacion ingresada", dialog)
        label.setGeometry(50, 30, 150, 20)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 70, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def ingresar_bicicleta(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ingresar bicicleta")
        dialog.setGeometry(300, 300, 350, 440)

        # Aca el codigo de ingreso de bicicleta

        label = QLabel("Bicicleta ingresada", dialog)
        label.setGeometry(50, 30, 150, 20)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 70, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def mostrar_informacion(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Informacion")
        dialog.setGeometry(300, 300, 350, 440)

        # Aca el codigo de mostrar informacion

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 200, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def cambiar_datos(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Cambiar datos")
        dialog.setGeometry(300, 300, 350, 440)

        # Aca el codigo de cambio de datos

        label = QLabel("Datos cambiados", dialog)
        label.setGeometry(50, 30, 150, 20)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 70, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()

    def dar_baja(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dar de baja")
        dialog.setGeometry(300, 300, 350, 440)

        # Aca el codigo de baja de objetos

        label = QLabel("Dado de baja", dialog)
        label.setGeometry(50, 30, 150, 20)

        volver_button = QPushButton("Volver", dialog)
        volver_button.setGeometry(50, 70, 250, 30)
        volver_button.clicked.connect(dialog.close)

        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("interfaz_estilo.qss").read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
