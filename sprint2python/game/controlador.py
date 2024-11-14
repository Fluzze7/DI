from tkinter import simpledialog, messagebox, Toplevel, Label
from modelo import GameModel
from vista import GameView, MainMenu


class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.game_view = None
        self.selected = []
        self.timer_started = False
        self.main_menu = MainMenu(root, start_game_callback=self.start_game,
                                  show_stats_callback=self.show_stats, quit_callback=self.quit_game)
        self.loading_window = None
        self.cards_shown = []
        self.click_blocked = False

    def start_game(self):
        player_name = simpledialog.askstring("Nombre del Jugador", "Ingresa tu nombre")
        if player_name is None:
            player_name = "User123456"

        difficulty = simpledialog.askstring("Seleccionar Dificultad", "Elige una dificultad: fácil, medio o difícil")
        difficulty = {"fácil": 4, "medio": 6, "difícil": 8}.get(difficulty, 4)

        self.model = GameModel(difficulty,player_name)

        self.game_view = GameView(on_card_click_callback=self.on_card_click,update_time_callback=self.update_time,update_move_count_callback=self.update_move_count)
        self.game_view.window = Toplevel(self.root)
        self.show_loading_window("Cargando tablero...")
        self.game_view.create_board(self.model)
        self.check_images_loaded()

    def show_loading_window(self, message):
        self.loading_window = Toplevel(self.root)
        self.loading_window.transient(self.root)
        self.loading_window.grab_set()
        Label(self.loading_window, text=message).pack(padx=20, pady=20)

    def check_images_loaded(self):
        if self.model.images_are_loaded():
            self.loading_window.destroy()
            print("Imagenes cargadas")
        else:
            self.root.after(100, self.check_images_loaded)  # Espera hasta que las imágenes se carguen


    def on_card_click(self,pos):
        if not self.click_blocked:
            self.cards_shown.append(pos)
            self.game_view.labels[(pos[0], pos[1])].config(image=self.model.images.get(self.model.board[pos[0]][pos[1]]))
            if len(self.cards_shown)== 2:
                self.click_blocked = True
                if self.model.check_match(self.cards_shown[0],self.cards_shown[1]):
                    print("Pareja encontrada")
                else:
                    self.game_view.window.after(1000, self.revert_cards)  # 1000 ms = 1 segundo


    def revert_cards(self):
        self.game_view.labels[(self.cards_shown[0][0], self.cards_shown[0][1])].config(image=self.model.hidden_image)
        self.game_view.labels[(self.cards_shown[1][0], self.cards_shown[1][1])].config(image=self.model.hidden_image)
        self.click_blocked = False
        self.cards_shown.clear()
    def handle_card_selection(self):
        pass

    def update_move_count(self, moves):
        pass

    def check_game_complete(self):
        return True if self.model.pairs_found == (self.model.difficulty**2//2) else False

    def return_to_main_menu(self):
        self.game_view.destroy()  # Destruir la vista del juego

    def show_stats(self):
        pass

    def update_time(self):
        pass

    def quit_game(self):
        self.main_menu.window.destroy()
