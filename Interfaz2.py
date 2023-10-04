from tkinter import *

root = Tk()
root.title('Maquina CNC 2D')
root.iconbitmap("Icono.ico")           #Personaliza Icono De Ventana
img = PhotoImage(file = "Interfaz Grafica.png")
Label(root, image = img).pack()

mainloop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
