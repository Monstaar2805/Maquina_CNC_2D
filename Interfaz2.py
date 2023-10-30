import tkinter
from tkinter import *

Ventana1 = Tk()
Ventana1.title('Maquina CNC 2D')
Ventana1.iconbitmap("Icono.ico")           #Personaliza Icono De Ventana
img = PhotoImage(file = "Interfaz Grafica.png")
Label(Ventana1, image = img).pack()
mainloop()
def Siguiente():
    tkinter.Label(Ventana1, text = "Next" ).pack()
boton = tkinter.Button(Ventana1, text = "siguiente", command = Next, fg ="green")
boton.pack()s
boton.place(x=200, y=200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
