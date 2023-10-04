from tkinter import*                      #importa la funcion

Ventana = Tk()

Ventana.title("Maquina CNC 2D")           #Nonmbre de la pagina

Ventana.resizable(True, True) #Tamaño minimo y maximo de la ventana

Ventana.iconbitmap("Icono.ico")           #Personaliza Icono De Ventana

Ventana.geometry("1200x600")              #Dimenciones Iniciales De La Ventana

Ventana.config(bg = "Purple")             # Colores De La Ventana

Ventana.mainloop()