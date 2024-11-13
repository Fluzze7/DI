from tkinter import messagebox,simpledialog,Toplevel,Label,Tk
from modelo import GameModel
from vista import GameView,MainMenu
import time


class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.selected = []
        self.timer_started = False
        self.game_view = None
        self.main_menu = MainMenu(root,start_game_callback=self.start_game,show_stats_callback=self.show_stats,
            quit_callback=self.return_to_main_menu)
        self.main_menu.on_start_game = self.show_difficulty_selection
        self.main_menu.on_show_stats = self.show_stats
        self.main_menu.on_exit = root.quit

    def show_difficulty_selection(self):
        difficulty = simpledialog.askstring("Seleccionar Dificultad", "Elige una dificultad: fácil, medio o difícil")
        if difficulty in ["fácil", "medio", "difícil"]:
            player_name = simpledialog.askstring("Nombre del Jugador", "Ingresa tu nombre")
            if player_name:
                return player_name,difficulty

    def start_game(self):
        name_and_difficulty = self.show_difficulty_selection()
        self.show_loading_window("Cargando tablero...")
        self.model = GameModel(name_and_difficulty[0], name_and_difficulty[1])
        self.check_images_loaded()

    def show_loading_window(self, message):
        self.loading_window = Toplevel(self.root)
        self.loading_window.transient(self.root)
        self.loading_window.grab_set()
        Label(self.loading_window, text=message).pack(padx=20, pady=20)

    def check_images_loaded(self):
        if self.model.images_are_loaded():
            self.loading_window.destroy()
            self.setup_game_view()
        else:
            self.root.after(100, self.check_images_loaded)

    def setup_game_view(self):
        self.game_view = GameView(self.root, self.model.board, self.model.cell_size)
        self.game_view.on_card_click = self.on_card_click
        self.update_move_count(0)
        self.update_time()

    def on_card_click(self, pos):
        if not self.timer_started:
            self.model.start_timer()
            self.timer_started = True
            self.update_time()

        self.selected.append(pos)
        self.game_view.show_card(pos, self.model.board[pos[0]][pos[1]])

        if len(self.selected) == 2:
            self.root.after(500, self.handle_card_selection)

    def handle_card_selection(self):
        pos1, pos2 = self.selected
        if self.model.check_match(pos1, pos2):
            self.game_view.keep_cards_visible(pos1, pos2)
        else:
            self.game_view.hide_card(pos1)
            self.game_view.hide_card(pos2)

        self.selected.clear()
        self.update_move_count(self.model.moves)
        self.check_game_complete()

    def update_move_count(self, moves):
        self.game_view.update_moves(moves)

    def check_game_complete(self):
        if self.model.is_game_complete():
            messagebox.showinfo("¡Victoria!", f"¡Has ganado en {self.model.moves} movimientos!")
            self.model.save_score()
            self.return_to_main_menu()

    def return_to_main_menu(self):
        self.game_view.destroy()
        self.main_menu.show()

    def show_stats(self):
        stats = self.model.load_scores()
        stats_message = "\n".join(
            f"{difficulty.title()}: {', '.join(f'{s['player_name']} - {s['moves']} movs' for s in scores)}"
            for difficulty, scores in stats.items()
        )
        messagebox.showinfo("Estadísticas", stats_message)

    def update_time(self):
        if self.timer_started:
            elapsed_time = self.model.get_time()
            self.game_view.update_timer(elapsed_time)
            self.root.after(1000, self.update_time)