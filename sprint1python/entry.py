#import de clase para interfaces gráficas
import tkinter as tk

def saludar():
    """
    Función que cambia el texto de un label según un entry de texto
    """
    nombre = entry.get()
    label2.config(text=f"Buenas {nombre}, que tengas un gran día.")

#crear y dimensionar la ventana principal
root = tk.Tk()
root.geometry("500x200")
root.title("Ejercicio3")

#crear un label
label1 = tk.Label(root,text="Introduce tu nombre.")
label1.pack(pady = 5)

#crear un entry
entry = tk.Entry(root,width=40)
entry.pack(pady = 5)

#botón para ejecutar la función saludar
button1 = tk.Button(text="Recibe un saludo personalizado.", command=saludar)
button1.pack(pady = 5)
#label que se modificará posteriormente
label2 = tk.Label(root)
label2.pack(pady = 5)
#inicio de programa
root.mainloop()