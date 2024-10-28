import tkinter as tk
from view import View
from controller import Controller
from model import NotasModel

# Crear la instancia principal de Tkinter
root = tk.Tk()

# Crear instancias de View, Model, y Controller
model = NotasModel()
view = View(root)
controller = Controller(model, view)



# Ejecutar el bucle principal de Tkinter
root.mainloop()
