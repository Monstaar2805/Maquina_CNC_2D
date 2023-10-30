import sys
from PySide6.QtCore import (QTimer, Qt)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton

class ImageTransitionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Transición de Imágenes")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Lista de rutas de imágenes para la transición
        self.image_paths = ["imagen1.jpg", "imagen2.jpg", "imagen3.jpg", "imagen4.jpg"]
        self.current_image_index = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.transition_images)
        self.timer.start(6000)  # Tiempo de cada imagen

        #Bon
        button1= QPushButton(self)


    def transition_images(self):
        # Cargar la siguiente imagen en la lista
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_paths):
            self.current_image_index = 3

        image_path = self.image_paths[self.current_image_index]
        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageTransitionApp()
    window.show()
    sys.exit(app.exec_())