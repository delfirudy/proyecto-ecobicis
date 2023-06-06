import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedWidget

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Add buttons for each option
        options = [
            "Ingreso de datos cliente",
            "Ingreso de datos trabajador",
            "Opciones cliente",
            "Opciones trabajador",
            "Salir"
        ]
    
        for option_text in options:
            button = QPushButton(option_text)
            button.clicked.connect(lambda _, text=option_text: self.open_submenu(text))
            layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

    def openNewWindow(self):
        new_window = NewWindow()
        self.close()
        new_window.show()

    def open_submenu(self, option_text):
        if option_text == "Ingreso de datos cliente":
            submenu_window = NewWindow(option_text)
        elif option_text == "Ingreso de datos trabajador":
            submenu_window = NewWindow(option_text)
        elif option_text == "Opciones cliente":
            submenu_window = NewWindow(option_text)
        elif option_text == "Opciones trabajador":
            submenu_window = NewWindow(option_text)
        elif option_text == "Salir":
            sys.exit()
        else:
            return
        
        self.close()
        submenu_window.show()

class NewWindow(QMainWindow):
    def __init__(self, string):
        super().__init__()
        self.initUI(string)

    def initUI(self, string):
        self.setWindowTitle(string)

        # Add widgets and set up the layout for the new window
        # ...

        self.show()
        return self


# class SubMenuWindow(QWidget):
#     def __init__(self):
#         super().__init__()

# class IngresoDatosClienteWindow(SubMenuWindow):
#     def __init__(self):
#         super().__init__()

#         layout = QVBoxLayout()
#         layout.addWidget(QPushButton("Ingreso de datos cliente"))

#         self.setLayout(layout)

# class IngresoDatosTrabajadorWindow(SubMenuWindow):
#     def __init__(self):
#         super().__init__()

#         layout = QVBoxLayout()
#         layout.addWidget(QPushButton("Ingreso de datos trabajador"))

#         self.setLayout(layout)

# class OpcionesClienteWindow(SubMenuWindow):
#     def __init__(self):
#         super().__init__()

#         layout = QVBoxLayout()
#         layout.addWidget(QPushButton("Opciones cliente"))

#         self.setLayout(layout)

# class OpcionesTrabajadorWindow(SubMenuWindow):
#     def __init__(self):
#         super().__init__()

#         layout = QVBoxLayout()
#         layout.addWidget(QPushButton("Opciones trabajador"))

#         self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("estilo.qss").read())
    main_menu = MainMenuWindow()
    main_menu.show()
    sys.exit(app.exec_())
