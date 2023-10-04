from tkinter import*                      #importa la funcion

Ventana = Tk()

Ventana.title("Maquina CNC 2D")           #Nonmbre de la pagina

Ventana.resizable(True, True) #Tamaño minimo y maximo de la ventana

Ventana.iconbitmap("Icono.ico")           #Personaliza Icono De Ventana

Ventana.geometry("600x300")              #Dimenciones Iniciales De La Ventana

Ventana.config(bg = "Purple")             # Colores De La Ventana

Ventana.mainloop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())