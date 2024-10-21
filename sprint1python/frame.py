#import de clase para interfaces gráficas
import tkinter as tk

def show_entry():
    """
    Función que muestra el texto ingresado del entry en el label3
    """
    label3.config(text=entry.get())

def del_entry():
    """
    Función que borra el texto del entry y limpia el label3
    """
    label3.config(text="")
    entry.delete(0, len(entry.get()))

#crear y dimensionar ventana principal
root = tk.Tk()
root.geometry("700x400")
root.title("Ejercicio8")

#crear un frame principal
main_frame = tk.Frame(root, bg="black")
main_frame.pack(side="top", pady=5, fill="both", expand=True)

#crear un frame superior dentro del frame principal
upper_frame = tk.Frame(main_frame, bg="red")
upper_frame.pack(side="top", pady=5, fill="both", expand=True)

#crear un frame inferior dentro del frame principal
lower_frame = tk.Frame(main_frame, bg="blue")
lower_frame.pack(side="top", pady=5, fill="both", expand=True)

#crear y agregar la primera label en el frame superior
label1 = tk.Label(upper_frame, text="Etiqueta n1 del frame superior.")
label1.pack(pady=5)

#crear y agrega la segunda label en el frame superior
label2 = tk.Label(upper_frame, text="Etiqueta n2 del frame superior.")
label2.pack(pady=5)

#crear y agregar un campo de entrada (entry) en el frame superior
entry = tk.Entry(upper_frame, width=40)
entry.pack(pady=5)

#crear y agregar una label en el frame inferior para mostrar resultados
label3 = tk.Label(lower_frame, text="")
label3.pack(pady=5)

#crear y agregar el primer botón en el frame inferior para mostrar el texto del entry
button1 = tk.Button(lower_frame, text="Mostrar entry", command=show_entry)
button1.pack(pady=10)

#crear y agregar el segundo botón en el frame inferior para borrar el texto del entry
button2 = tk.Button(lower_frame, text="Borrar entry", command=del_entry)
button2.pack(pady=10)

#iniciar el programa
root.mainloop()
