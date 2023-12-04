import sys, subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def accion_clic():
    print("El botón ha sido clicado")

# Crear la aplicación PyQt
app = QApplication(sys.argv)
ventana = QMainWindow()
ventana.setWindowTitle("Ejemplo de clic en PyQt5")

# Crear un botón
boton = QPushButton("Haz clic aquí", ventana)
boton.clicked("hola")  # Conectar evento clic al método accion_clic



# Añadir el botón a la ventana
ventana.setCentralWidget(boton)
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec_())
