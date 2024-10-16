import tkinter as tk
from ntpath import commonpath
def show_entry():
    label3.config(text=entry.get())
def del_entry():
    label3.config(text="")
    entry.delete(0,len(entry.get()))

root = tk.Tk()
root.geometry("700x400")
root.title("Ejercicio8")
main_frame = tk.Frame(root,bg="black")
main_frame.pack(side="top",pady = 5,fill="both",expand=True)
upper_frame = tk.Frame(main_frame,bg="red")
upper_frame.pack(side="top",pady = 5,fill="both",expand=True)
lower_frame = tk.Frame(main_frame,bg="blue")
lower_frame.pack(side="top",pady = 5,fill="both",expand=True)

label1 = tk.Label(upper_frame,text="Etiqueta n1 del frame superior.")
label1.pack(pady=5)

label2 = tk.Label(upper_frame,text="Etiqueta n2 del frame superior.")
label2.pack(pady=5)
entry = tk.Entry(upper_frame,width=40)
entry.pack(pady = 5)
label3 = tk.Label(lower_frame,text="")
label3.pack(pady = 5)
button1 = tk.Button(lower_frame,text="Mostrar entry", command=show_entry)
button1.pack(pady=10)
button2 = tk.Button(lower_frame,text="Borrar entry", command=del_entry)
button2.pack(pady=10)

root.mainloop()