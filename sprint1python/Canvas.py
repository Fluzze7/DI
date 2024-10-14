import tkinter as tk

def dibujar_formas():
    canvas.create_rectangle(float(var1.get()),float(var2.get()),float(var3.get()),float(var4.get()))
    canvas.create_oval(float(var1.get()), float(var2.get()), float(var3.get()), float(var4.get()))
root = tk.Tk()
root.geometry("800x600")
root.title("Ejercicio7")

canvas = tk.Canvas(root,width=500,height=400,bg="white")
canvas.pack(pady = 20)


# Crear el frame principal donde estarán las filas
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# Crear un frame para las etiquetas (fila 1)
frame_labels = tk.Frame(main_frame)
frame_labels.pack(side="top", pady=5)

# Crear las etiquetas y colocarlas en fila usando pack
label1 = tk.Label(frame_labels, text="x0")
label2 = tk.Label(frame_labels, text="x1")
label3 = tk.Label(frame_labels, text="y0")
label4 = tk.Label(frame_labels, text="y1")

label1.pack(side="left", padx=60)
label2.pack(side="left", padx=10)
label3.pack(side="left", padx=60)
label4.pack(side="left", padx=0)

frame_entries = tk.Frame(main_frame)
frame_entries.pack(side="top", pady=5)

var1 = tk.Entry(frame_entries, width=10)
var2 = tk.Entry(frame_entries, width=10)
var3 = tk.Entry(frame_entries, width=10)
var4 = tk.Entry(frame_entries, width=10)

var1.pack(side="left", padx=10)
var2.pack(side="left", padx=10)
var3.pack(side="left", padx=10)
var4.pack(side="left", padx=10)

frame_button = tk.Frame(main_frame)
frame_button.pack(side="top",pady = 10)

button = tk.Button(root,text="Dibujar cuadrado.",command=dibujar_formas)
button.pack(padx = 10)

root.mainloop()