#import de clase para interfaces gráficas
import tkinter as tk
from tkinter import messagebox

def close_app():
    """
    Función que cierra la aplicación
    """
    root.quit()

#crear y dimensionar ventana principal
root = tk.Tk()
root.title("Ejercicio9")
root.geometry("800x500")

# Crear la barra de menú
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

#crear un desplegable para el menú Archivo
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

#agregar opción Abrir al menú Archivo
menu_archivo.add_command(label="Abrir")

#agregar separador al menú Archivo
menu_archivo.add_separator()

#agregar opción Salir al menú Archivo y asignar la función de cerrar la aplicación
menu_archivo.add_command(label="Salir", command=close_app)

def mostrar_ayuda():
    """
    Función que muestra una ventana emergente con información
    """
    messagebox.showinfo(title="Ayuda", message="Esta ventana mostraría ayuda para entender el programa.")

#crear un desplegable para el menú Ayuda
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

#agregar opción Acerca de al menú Ayuda y asignar la función mostrar_ayuda
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)

#iniciar el programa
root.mainloop()
