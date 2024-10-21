#import de clase para interfaces gráficas
import tkinter as tk
def draw_rect():
    """
    Función que borra el canvas y pinta un rectángulo si todos los parámetros son correctos,
    en caso de no serlo, hace un print por consola
    """
    canvas.delete("all")
    try:
        canvas.create_rectangle(float(var1.get()),float(var2.get()),float(var3.get()),float(var4.get()), outline="blue")
    except ValueError as ve:
        print("Algún dato es incorrecto")
def draw_circle():
    """
    Función que borra el canvas y pinta un círlulo si todos los parámetros son correctos,
    en caso de no serlo, hace un print por consola
    """
    canvas.delete("all")
    try:
        canvas.create_oval(float(var1.get()),float(var2.get()),float(var3.get()),float(var4.get()), outline="red")
    except ValueError as ve:
        print("Algún dato es incorrecto")

#crear y dimensionar ventana principal
root = tk.Tk()
root.geometry("800x600")
root.title("Ejercicio7")

#crear y dimensionar el canvas en la ventana principal
canvas = tk.Canvas(root,width=500,height=300,bg="white", highlightthickness=5, highlightbackground="black")
canvas.pack(pady = 20)


#creado un frame principal para no trabajar sobre root
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

#frame creado para los distintos labels
frame_labels = tk.Frame(main_frame)
frame_labels.pack(side="top", pady=5)

#labels de posición creados y alineados
label1 = tk.Label(frame_labels, text="x0")
label2 = tk.Label(frame_labels, text="y0")
label3 = tk.Label(frame_labels, text="x1")
label4 = tk.Label(frame_labels, text="y1")
label1.pack(side="left", padx=60)
label2.pack(side="left", padx=10)
label3.pack(side="left", padx=60)
label4.pack(side="left", padx=0)

#segundo frame para las entrys
frame_entries = tk.Frame(main_frame)
frame_entries.pack(side="top", pady=5)

#entrys de las coordenadas creadas y alienadas
var1 = tk.Entry(frame_entries, width=10)
var2 = tk.Entry(frame_entries, width=10)
var3 = tk.Entry(frame_entries, width=10)
var4 = tk.Entry(frame_entries, width=10)
var1.pack(side="left", padx=10)
var2.pack(side="left", padx=10)
var3.pack(side="left", padx=10)
var4.pack(side="left", padx=10)

#frame para colocar ambos botones
frame_button = tk.Frame(main_frame)
frame_button.pack(side="top",pady = 10)

#boton para crear cuadrado
square_button = tk.Button(root,text="Dibujar cuadrado.",command=draw_rect)
square_button.pack(pady = 5)

#boton para crear circulo
circle_button = tk.Button(root,text="Dibujar circulo.",command=draw_circle)
circle_button.pack(pady = 5)

#inicio de programa
root.mainloop()