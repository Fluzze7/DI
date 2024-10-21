#clase necesaria para trabajar en interfaces gráficas
import tkinter as tk
def mostrar_texto():
    """
    Función muestra el label1 al final debajo de los botones.
    """
    label1 = tk.Label(text="TEXTO MOSTRADO EN PANTALLA")
    label1.pack(pady = 10)

def finalizar_programa():
    """
    Función que finaliza el programa al ser pulsada
    """
    root.destroy()

#Crear y dimensionar la ventana principal
root = tk.Tk()
root.geometry("500x300")
root.title("Ejercicio2")

#Insertar un botón
button1 = tk.Button(text="MOSTRAR TEXTO", command=mostrar_texto)
button1.pack(pady = 5)

#Insertar otro botón
button2 = tk.Button(text="CERRAR PROGRAMA", command=finalizar_programa)
button2.pack(pady = 5)

#Iniciar programa
root.mainloop()
