#import de clase para interfaces gráficas
import tkinter as tk

def change_text():
    """
    Función que cambia el texto del label3
    """
    label3.config(text="Texto cambiado :)")

#crear y dimensionar ventana principal
root = tk.Tk()
root.title("Label")
root.geometry("600x400")
root.title("Ejercicio1")

#crear y agregar el primer label con texto de bienvenida
label1 = tk.Label(root, text="Bienvenido al primer programa", font=("Helvetica", 14, "italic"))
label1.pack(pady=5)

#crear y agregar el segundo label con nombre
label2 = tk.Label(root, text="Mi nombre es Jose Antonio Prego Fraga", font=("Helvetica", 14, "italic"))
label2.pack(pady=5)

#crear y agregar el tercer label con texto que será cambiado
label3 = tk.Label(root, text="Texto cambiante", font=("Helvetica", 14, "italic"))
label3.pack(pady=5)

#crear y agregar un botón que cambia el texto del tercer label
button = tk.Button(root, text="Texto a cambiar....", command=change_text)
button.pack(pady=5)

#iniciar el programa
root.mainloop()
