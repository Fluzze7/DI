#import de clase para interfaces gráficas
import tkinter as tk
def actualizar_label():
    """
    Actualiza un label con la selección de una listbox mediante click
    """
    selection = listbox.curselection()
    elementos = [listbox.get(i) for i in selection]
    label.config(text=f"Seleccionaste: {','.join(elementos)}")

#crear y dimensionar la ventana principal
root = tk.Tk()
root.title("Ejercicio6")
root.geometry("800x500")

#definiendo contenido de la listbox en una lista
opciones = ["Manzana","Pera","Platano","Naranja","Uva"]

#instancia de una listbox
listbox = tk.Listbox(root,selectmode=tk.SINGLE)

#inserción de opciones dentro de la listbox
for opcion in opciones:
    listbox.insert(tk.END,opcion)

#colocar la listbox
listbox.pack(pady = 10)

#instancia y colocar el label donde se mostrará la selección
label = tk.Label(root,text="No has seleccionado nada")
label.pack(pady = 5)

#botón que activa la función de actualizar_label
button = tk.Button(root,text="Mostrar seleccion",command=actualizar_label)
button.pack(pady = 10)

root.mainloop()