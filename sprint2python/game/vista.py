import tkinter as tk
from tkinter import Label, Toplevel


class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.window = None
        self.labels = {}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.move_count = 0

    def create_board(self,model):
        k = 0
        j = 0
        for row in model.board:
            for i in row:
                self.labels[(j,k)] = Label(self.window,text="",image=model.images.get(i))
                j+=1
            k+=1

    def update_move_count(self,moves):
      self.move_count+=1


class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.geometry("300x150")
        self.window.title("Juego de Memoria")
        (tk.Button(self.window, text="Jugar", command=start_game_callback).pack(pady = 10))
        (tk.Button(self.window, text="Estadísticas", command=show_stats_callback).pack(pady = 10))
        (tk.Button(self.window, text="Salir", command=quit_callback).pack(pady = 10))
