import tkinter as tk
from controlador import GameController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Juego de Memoria")

    controller = GameController(root)
    root.mainloop()

