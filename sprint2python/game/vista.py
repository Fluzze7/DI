import tkinter as tk
from tkinter import Label, Toplevel


class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.window = None
        self.labels = {}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.moves_label = None
        self.times_label = None


    def create_board(self,model):
        k = 0
        j = 0
        for row in model.board:
            j = 0
            for i in row:
                label = Label(self.window, text="", image=model.hidden_image)
                label.bind("<Button-1>", lambda event, pos=(j, k): self.on_card_click_callback(pos))
                label.grid(row=k, column=j)
                self.labels[(j, k)] = label
                j += 1
            k += 1




        self.moves_label= Label(self.window,text=f"Movimientos: 0")
        self.moves_label.grid(row=k,column= (j//2))
        self.times_label = Label(self.window, text=f"Tiempo: 0")
        self.times_label.grid(row=k, column=(j // 2)+1)

    def set_moves(self,param):
        self.moves_label.config(text=f"Movimientos: {param}")

    def set_time(self, param):
        self.times_label.config(text=f"Tiempo: {param}")

    def update_move_count(self,moves):
      pass


class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.geometry("300x150")
        self.window.title("Juego de Memoria")
        (tk.Button(self.window, text="Jugar", command=start_game_callback).grid(row= 0, column=1))
        (tk.Button(self.window, text="Estadísticas", command=show_stats_callback).grid(row= 1, column=1))
        (tk.Button(self.window, text="Salir", command=quit_callback).grid(row= 2, column=1))
