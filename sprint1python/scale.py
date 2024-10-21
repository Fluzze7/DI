#import de clase para interfaces gráficas
import tkinter as tk

#crear y dimensionar la ventana principal
root = tk.Tk()
root.title("Ejercicio11")
root.geometry("800x500")

def show_label(value):
    """
    :param value:(int) valor de la scale
    modifica el label1 con el valor ACTUAL de la escala
    """
    l1.config(text=f"Valor de la escala: {value}")

#crear el label que muestra el valor de la escala
l1 = tk.Label(root,text="Valor de la escala: 0")
l1.pack(pady=5)

#crear un scale horizontal de 0 a 100
scale = tk.Scale(root,from_=0,to=100,orient="horizontal",command=show_label)
scale.pack(pady = 5)

#iniciar el programa
root.mainloop()