from tkinter import messagebox,simpledialog,Toplevel,Label,Tk

from modelo import GameModel
from vista import GameView,MainMenu
import time

from tkinter import simpledialog, messagebox, Toplevel
from recursos import descargar_imagen
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

    def start_game(self):
        player_name = simpledialog.askstring("Nombre del Jugador", "Ingresa tu nombre")
        difficulty = simpledialog.askstring("Seleccionar Dificultad", "Elige una dificultad: fácil, medio o difícil")
        if player_name is None:
            player_name = "User123456"
        difficulty = {"fácil": 4, "medio": 6, "difícil": 8}.get(difficulty, 4)

        self.show_loading_window("Cargando tablero...")
        self.model = GameModel(difficulty, player_name)  # Crear modelo con los parámetros
        self.check_images_loaded()  # Verificar si las imágenes se han cargado correctamente

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
            self.root.after(100, self.check_images_loaded)  # Espera hasta que las imágenes se carguen

    def setup_game_view(self):
        self.game_view = GameView(self.on_card_click, self.update_move_count, self.update_time)  # Crear vista
        self.game_view.create_board(self.model)  # Crear el tablero en la vista con el modelo
        self.update_move_count(0)  # Iniciar contador de movimientos
        self.update_time()  # Iniciar cronómetro

    def on_card_click(self, pos):
        if not self.timer_started:
            self.model.start_timer()  # Iniciar el temporizador cuando se hace el primer clic
            self.timer_started = True
            self.update_time()

        self.selected.append(pos)
        self.game_view.update_board(pos, self.model.images.get(self.model.board[pos[0]][pos[1]]))  # Mostrar carta clickeada

        if len(self.selected) == 2:
            self.root.after(500, self.handle_card_selection)  # Compara las cartas después de medio segundo

    def handle_card_selection(self):
        pos1, pos2 = self.selected
        if self.model.check_match(pos1, pos2):
            self.game_view.update_board(pos1, self.model.images.get(self.model.board[pos1[0]][pos1[1]]))  # Mantener las cartas visibles
            self.game_view.update_board(pos2, self.model.images.get(self.model.board[pos2[0]][pos2[1]]))
        else:
            self.game_view.reset_cards(pos1, pos2, self.model)  # Restablecer las cartas si no coinciden

        self.selected.clear()
        self.update_move_count(self.model.moves)
        self.check_game_complete()

    def update_move_count(self, moves):
        self.game_view.update_move_count(moves)  # Actualizar el contador de movimientos

    def check_game_complete(self):
        if self.model.is_game_complete():  # Verificar si el juego ha terminado
            messagebox.showinfo("¡Victoria!", f"¡Has ganado en {self.model.moves} movimientos!")
            self.model.save_score()  # Guardar puntaje
            self.return_to_main_menu()

    def return_to_main_menu(self):
        self.game_view.destroy()  # Destruir la vista del juego
        self.main_menu.show()  # Volver al menú principal

    def show_stats(self):
        stats = self.model.load_scores()  # Cargar las estadísticas
        stats_message = "\n".join(
            f"{difficulty.title()}: {', '.join(f'{s['name']} - {s['moves']} movs' for s in scores)}"
            for difficulty, scores in stats.items()
        )
        messagebox.showinfo("Estadísticas", stats_message)

    def update_time(self):
        if self.timer_started:
            elapsed_time = self.model.get_time()  # Obtener el tiempo transcurrido
            self.game_view.update_time_count(elapsed_time)  # Actualizar el tiempo en la vista
            self.root.after(1000, self.update_time)  # Actualizar cada segundo
    def quit_game(self):
        self.main_menu.window.destroy()
