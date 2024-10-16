import tkinter as tk
def actualizar_label():
    selection = listbox.curselection()
    elementos = [listbox.get(i) for i in selection]
    label.config(text=f"Seleccionaste: {','.join(elementos)}")
root = tk.Tk()
root.title("Ejercicio6")
root.geometry("800x500")

opciones = ["Manzana","Pera","Platano","Naranja","Uva"]
listbox = tk.Listbox(root,selectmode=tk.SINGLE)
for opcion in opciones:
    listbox.insert(tk.END,opcion)
listbox.pack(pady = 10)

label = tk.Label(root,text="No has seleccionado nada")
label.pack(pady = 5)

button = tk.Button(root,text="Mostrar seleccion",command=actualizar_label)
button.pack(pady = 10)

root.mainloop()