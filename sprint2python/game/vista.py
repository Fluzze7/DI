import tkinter as tk
from tkinter import Label, Toplevel


class GameView:
    def __init__(self,on_card_click_callback, update_move_count_callback,update_time_callback):
        self.window = None
        self.moves_label = None
        self.time_label = None
        self.labels = {}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback


    def create_board(self,model):
        self.window = Toplevel()
        self.window.title("Juego de Memoria")

        board_size = model.board_size
        for row in range(board_size):
            for col in range(board_size):
                label = Label(self.window,image=model.hidden_image)
                label.grid(row= row, column= col)

                self.labels[(row,col)] = label

                label.bind("<Button-1>",lambda event, pos=(row,col):self.on_card_click_callback(pos))

        self.moves_label = Label(self.window, text="Movimientos: 0")
        self.moves_label.grid(row = board_size,column = 0 // 2, columnspan=board_size // 2)

        self.time_label = Label(self.window, text="Tiempo: 0s")
        self.time_label.grid(row=board_size, column=board_size // 2, columnspan=board_size // 2)

    def update_board(self,pos,image_id):
        label = self.labels.get(pos)
        if label:
            label.config(image=image_id)

    def reset_cards(self,pos1,pos2,model):
        if pos1 in self.labels:
            self.labels[pos1].config(image=model.hidden_image)
        if pos2 in self.labels:
            self.labels[pos2].config(image=model.hidden_image)

    def update_move_count(self,moves):
        self.moves_label.config(text=f"Movimientos: {moves}")

    def update_time_count(self,time):
        self.moves_label.config(text=f"Movimientos: {time}s")

    def destroy(self):
        self.window.destroy()
        self.labels.clear()




class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.root = root
        self.root.title("Menú Principal")

        self.start_game_callback = start_game_callback
        self.show_stats_callback = show_stats_callback
        self.quit_callback = quit_callback

        self.play_button = tk.Button(self.root, text="Jugar", command=self.start_game_callback)
        self.play_button.pack(pady=10)

        self.stats_button = tk.Button(self.root, text="Estadísticas", command=self.show_stats_callback)
        self.stats_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Salir", command=self.quit_callback)
        self.quit_button.pack(pady=10)

    def show_stats(self, stats):
        stats_window = Toplevel(self.root)
        stats_window.title("Estadísticas")

        for difficulty, scores in stats.items():
            Label(stats_window, text=f"Dificultad: {difficulty}", font=("Arial", 12, "bold")).pack(pady=(10, 5))

            for score in scores:
                Label(stats_window, text=f"{score['name']} - Movimientos: {score['moves']}").pack()




