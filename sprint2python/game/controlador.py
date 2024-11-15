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
        self.is_game_won = False
        self.cards_clicked = []

    def start_game(self):
        player_name = simpledialog.askstring("Nombre del Jugador", "Ingresa tu nombre")
        if player_name is None:
            player_name = "User123456"

        difficulty = simpledialog.askstring("Seleccionar Dificultad", "Elige una dificultad: fácil, medio o difícil")
        difficulty = {"fácil": 4, "medio": 6, "difícil": 8}.get(difficulty, 4)

        self.model = GameModel(difficulty, player_name)
        self.timer_started = False
        self.model.start_time = None

        self.game_view = GameView(on_card_click_callback=self.on_card_click,
                                  update_time_callback=self.update_time,
                                  update_move_count_callback=self.update_move_count)
        self.game_view.window = Toplevel(self.root)
        self.show_loading_window("Cargando tablero...")
        self.game_view.create_board(self.model)
        self.check_images_loaded()

    def update_time(self):
        self.game_view.set_time(self.model.get_elapsed_time())

        if not self.is_game_won:
            self.root.after(1000, self.update_time)

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

    def on_card_click(self, pos):
        # Evitar que se haga clic en una carta emparejada
        if pos in self.cards_clicked:
            return

        if not self.timer_started:
            self.model.start_timer()
            self.update_time()
            self.timer_started = True

        if not self.click_blocked:
            # Añadir la carta seleccionada
            self.cards_shown.append(pos)

            if pos not in self.cards_clicked:
                self.update_move_count()
            self.cards_clicked.append(pos)

            # Mostrar la carta en la vista
            self.game_view.labels[(pos[0], pos[1])].config(
                image=self.model.images.get(self.model.board[pos[0]][pos[1]]))

            if len(self.cards_shown) == 2:
                self.click_blocked = True
                if self.model.check_match(self.cards_shown[0], self.cards_shown[1]):
                    self.model.pairs_found += 1
                    self.cards_clicked.extend(
                        self.cards_shown)  # Añadir las cartas emparejadas a la lista de cartas clicadas
                    self.cards_shown.clear()
                    self.check_game_complete()
                    self.click_blocked = False
                else:
                    # Espera 500 ms para deshacer las cartas
                    self.game_view.window.after(500, self.revert_cards)  # 500 ms = 0.5 segundo

    def revert_cards(self):
        # Revertir las cartas que no son una pareja
        self.game_view.labels[(self.cards_shown[0][0], self.cards_shown[0][1])].config(image=self.model.hidden_image)
        self.game_view.labels[(self.cards_shown[1][0], self.cards_shown[1][1])].config(image=self.model.hidden_image)

        # Eliminar las cartas del historial de clics
        self.cards_clicked.remove(self.cards_shown[0])
        self.cards_clicked.remove(self.cards_shown[1])

        # Limpiar la lista de cartas mostradas
        self.cards_shown.clear()

        # Desbloquear los clics para la siguiente selección
        self.click_blocked = False

    def update_move_count(self):
        self.model.moves += 1
        self.game_view.set_moves(self.model.moves)

    def check_game_complete(self):
        if self.model.pairs_found == (self.model.difficulty ** 2 // 2):
            self.game_view.show_victory(self.model.moves, self.model.get_elapsed_time(),self.model.player_name)  # Llamada correcta al método
            return True
        return False
    def end_game(self):
        self.model.save_score(self.model.difficulty,self.model.player_name,self.model.moves,self.model.get_elapsed_time())
        self.return_to_main_menu()
    def return_to_main_menu(self):
        self.game_view.window.destroy()  # Destruir la vista del juego
        self.game_view = None

    def show_stats(self):
        pass

    def quit_game(self):
        self.main_menu.window.destroy()
