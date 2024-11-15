from tkinter import simpledialog, messagebox, Toplevel, Label
from modelo import GameModel,load_results
from vista import GameView, MainMenu
import pygame as musica


class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.game_view = None
        self.selected = []
        self.timer_started = False
        self.main_menu = MainMenu(root, start_game_callback=self.start_game,
                                  show_stats_callback=self.show_stats, quit_callback=self.quit_game)
        self.button_effect =  musica.mixer.Sound("../musica/boton.mp3")
        self.button_effect.set_volume(0.5)
        self.card_effect = musica.mixer.Sound("../musica/carta.mp3")
        self.card_effect.set_volume(0.5)
        self.wrong_card = musica.mixer.Sound("../musica/fallo.mp3")
        self.wrong_card.set_volume(0.15)
        self.loading_window = None
        self.cards_shown = []
        self.click_blocked = False
        self.is_game_won = False
        self.cards_clicked = []

    def start_game(self):
        self.button_effect.play()
        player_name = simpledialog.askstring("Nombre del Jugador", "Ingresa tu nombre")
        self.button_effect.play()
        if player_name is None:
            player_name = "User123456"

        difficulty = simpledialog.askstring("Seleccionar Dificultad", "Elige una dificultad: fácil, medio o difícil")
        self.button_effect.play()
        difficulty = {"fácil": 4, "medio": 6, "difícil": 8}.get(difficulty, 4)
        self.model = GameModel(difficulty, player_name)

        self.timer_started = False
        self.model.start_time = None

        # Mostrar la ventana de carga antes de cargar las imágenes
        self.game_view = GameView(on_card_click_callback=self.on_card_click,
                                  update_time_callback=self.update_time,
                                  update_move_count_callback=self.update_move_count)
        self.game_view.window = Toplevel(self.root)
        self.game_view.window.resizable(False, False)


        # Después de que las imágenes se carguen, crea el tablero
        self.game_view.create_board(self.model)

    def update_time(self):
        if self.game_view is not None:
            self.game_view.set_time(self.model.get_elapsed_time())

            if not self.is_game_won:
                self.root.after(1000, self.update_time)


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



            # Mostrar la carta en la vista
            self.card_effect.play()
            self.game_view.labels[(pos[0], pos[1])].config(
                image=self.model.images.get(self.model.board[pos[0]][pos[1]]))


            if len(self.cards_shown) == 2:
                self.update_move_count()
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
        self.wrong_card.play()
        self.game_view.labels[(self.cards_shown[0][0], self.cards_shown[0][1])].config(image=self.model.hidden_image)
        self.game_view.labels[(self.cards_shown[1][0], self.cards_shown[1][1])].config(image=self.model.hidden_image)
        # Limpiar la lista de cartas mostradas
        self.cards_shown.clear()

        # Desbloquear los clics para la siguiente selección
        self.click_blocked = False

    def update_move_count(self):
        self.model.moves += 1
        self.game_view.set_moves(self.model.moves)

    def check_game_complete(self):
        if self.model.pairs_found == (self.model.difficulty ** 2 // 2):
            self.game_view.show_victory(self.model.moves, self.model.get_elapsed_time(),self.model.player_name)
            self.is_game_won = True
            self.end_game()# Llamada correcta al método

            return True
        return False

    def end_game(self):
        self.model.save_score(self.model.difficulty, self.model.player_name, self.model.moves,
                              self.model.get_elapsed_time())
        self.return_to_main_menu()

    def return_to_main_menu(self):
        self.game_view.window.destroy()  # Destruir la vista del juego
        self.game_view = None
        self.model = None
        self.cards_clicked.clear()
        self.timer_started = False
        self.loading_window = None
        self.is_game_won = False

    def show_stats(self):
        self.button_effect.play()
        # Cargar los resultados desde el archivo JSON
        results = load_results()

        # Crear el contenido para mostrar en el messagebox
        message = "Tabla de Puntuaciones\n\n"
        for difficulty, scores in results.items():
            message += f"Dificultad {difficulty}:\n"
            if not scores:
                message += "  No hay puntuaciones.\n"
            else:
                for i, score in enumerate(scores):
                    message += f"  {i + 1}. {score['nombre']} - Movimientos: {score['movimientos']} - Tiempo: {score['tiempo']}s - Fecha: {score['fecha']}\n"
            message += "\n"

        # Mostrar el messagebox con los resultados
        messagebox.showinfo("Historial de Resultados", message)
    def quit_game(self):
        self.button_effect.play()
        self.main_menu.window.destroy()
