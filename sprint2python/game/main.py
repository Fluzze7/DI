import tkinter as tk
from controlador import GameController
from vista import MainMenu

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Juego de Memoria")
    root.geometry("800x600")

    controller = GameController(root)

    root.mainloop()

