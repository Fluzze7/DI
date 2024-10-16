import tkinter as tk
def mostrar_texto():
    label1 = tk.Label(text="TEXTO MOSTRADO EN PANTALLA")
    label1.pack(pady = 10)

def finalizar_programa():
    root.destroy()
root = tk.Tk()
root.geometry("500x300")
root.title("Ejercicio2")
button1 = tk.Button(text="MOSTRAR TEXTO", command=mostrar_texto)
button1.pack(pady = 5)
button2 = tk.Button(text="CERRAR PROGRAMA", command=finalizar_programa)
button2.pack(pady = 5)
root.mainloop()
