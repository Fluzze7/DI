#import de clase para interfaces gráficas
import tkinter as tk

def cambiar_color():
    """
    Función que cambia el color de fondo de la ventana principal
    """
    radio = var_radio.get()
    color = "grey"
    if radio == "grey":
        color = "grey"
    if radio == "yellow":
        color = "yellow"
    if radio == "blue":
        color = "blue"

    root.config(bg=color)

#crear y dimensionar la ventana principal
root = tk.Tk()
root.title("Ejercicio5")
root.geometry("600x250")

#definir variable del radiobutton
var_radio = tk.StringVar()

#poner valor por defecto
var_radio.set("grey")

#crear radiobuttons con las distintas opciones
radio1 = tk.Radiobutton(root,text="Gris", variable=var_radio,value="grey",command=cambiar_color)
radio1.pack(pady = 5)
radio2 = tk.Radiobutton(root,text="Yellow", variable=var_radio,value="yellow",command=cambiar_color)
radio2.pack(pady = 5)
radio3 = tk.Radiobutton(root,text="Blue", variable=var_radio,value="blue",command=cambiar_color)
radio3.pack(pady = 5)

#iniciar el programa
root.mainloop()
