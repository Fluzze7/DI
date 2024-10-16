import tkinter as tk
from tkinter import messagebox


def close_app():
    root.quit()

root = tk.Tk()
root.title("Ejercicio9")
root.geometry("800x500")

# Crear la barra de menú
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=close_app)

def mostrar_ayuda():
    messagebox.showinfo(title="Ayuda", message="Esta ventana mostraría ayuda para entender el programa.")

menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)

root.mainloop()
