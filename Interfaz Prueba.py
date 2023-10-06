from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super()-__init__()
        self.setWindowTitle('Maquina CNC 2D')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())