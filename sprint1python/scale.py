import tkinter as tk

root = tk.Tk()
root.title("Ejercicio11")
root.geometry("800x500")
def show_label(value):
    l1.config(text=f"Valor de la escala: {value}")

l1 = tk.Label(root,text="Valor de la escala: 0")
l1.pack(pady=5)
scale = tk.Scale(root,from_=0,to=100,orient="horizontal",command=show_label)
scale.pack(pady = 5)

root.mainloop()