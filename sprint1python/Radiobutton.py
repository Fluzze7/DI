import tkinter as tk

def cambiar_color():
    radio = var_radio.get()
    color = "grey"
    if radio == "grey":
        color = "grey"
    if radio == "yellow":
        color = "yellow"
    if radio == "blue":
        color = "blue"
    root.config(bg=color)

root = tk.Tk()
root.title("Ejercicio5")
root.geometry("600x250")

var_radio = tk.StringVar()
var_radio.set("grey")
radio1 = tk.Radiobutton(root,text="Gris", variable=var_radio,value="grey",command=cambiar_color)
radio1.pack(pady = 5)
radio2 = tk.Radiobutton(root,text="Yellow", variable=var_radio,value="yellow",command=cambiar_color)
radio2.pack(pady = 5)
radio3 = tk.Radiobutton(root,text="Blue", variable=var_radio,value="blue",command=cambiar_color)
radio3.pack(pady = 5)
root.mainloop()
