import tkinter as tk

def change_text():
    label3.config(text="Texto cambiado :)")

root =tk.Tk()
root.title("Label")
root.geometry("600x400")
root.title("Ejercicio1")
label1 = tk.Label(root,text="Bienvenido al primer programa", font=("Helvetica", 14 ,"italic"))
label1.pack(pady=5)
label2 = tk.Label(root,text="Mi nombre es Jose Antonio Prego Fraga", font=("Helvetica", 14 ,"italic"))
label2.pack(pady=5)
label3 = tk.Label(root,text="Texto cambiante", font=("Helvetica", 14 ,"italic"))
label3.pack(pady=5)
button = tk.Button(root,text="Texto a cambiar....",command=change_text)
button.pack(pady=5)
root.mainloop()