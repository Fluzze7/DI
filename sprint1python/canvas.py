import tkinter as tk
def draw_rect():
    canvas.delete("all")
    try:
        canvas.create_rectangle(float(var1.get()),float(var2.get()),float(var3.get()),float(var4.get()), outline="blue")
    except ValueError as ve:
        print("Algún dato es incorrecto")
def draw_circle():
    canvas.delete("all")
    try:
        canvas.create_oval(float(var1.get()),float(var2.get()),float(var3.get()),float(var4.get()), outline="red")
    except ValueError as ve:
        print("Algún dato es incorrecto")

root = tk.Tk()
root.geometry("800x600")
root.title("Ejercicio7")

canvas = tk.Canvas(root,width=500,height=300,bg="white", highlightthickness=5, highlightbackground="black")
canvas.pack(pady = 20)



main_frame = tk.Frame(root)
main_frame.pack(pady=20)


frame_labels = tk.Frame(main_frame)
frame_labels.pack(side="top", pady=5)


label1 = tk.Label(frame_labels, text="x0")
label2 = tk.Label(frame_labels, text="y0")
label3 = tk.Label(frame_labels, text="x1")
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

square_button = tk.Button(root,text="Dibujar cuadrado.",command=draw_rect)
square_button.pack(pady = 5)

circle_button = tk.Button(root,text="Dibujar circulo.",command=draw_circle)
circle_button.pack(pady = 5)

root.mainloop()