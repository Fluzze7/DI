import tkinter as tk
def mostrar_gustos():
    if leer.get():
        lee = "eres lector"
    else:
        lee = "no lees"
    if deportes.get():
        deporte = "deportista"
    else:
        deporte = "no haces deporte"
    if musica.get():
        music = "te gusta la musica"
    else:
        music = "no escuchas musica"
    label1.config(text=f"Tus gustos son: {lee}, {deporte} y {music}")
root = tk.Tk()
root.title("Ejercicio4")
root.geometry("600x250")
leer = tk.IntVar()
deportes = tk.IntVar()
musica = tk.IntVar()
checkleer = tk.Checkbutton(root, text="leer", variable=leer,command=mostrar_gustos)
checkleer.pack(pady = 5)
checkdeporte = tk.Checkbutton(root, text="deporte", variable=deportes,command=mostrar_gustos)
checkdeporte.pack(pady = 5)
checkmusica = tk.Checkbutton(root, text="musica", variable=musica,command=mostrar_gustos)
checkmusica.pack(pady = 5)
label1 = tk.Label(root)
label1.pack(pady = 5)
root.mainloop()
