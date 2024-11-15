
import threading
import time
import random
import os
import json
from datetime import datetime
from recursos import descargar_imagen


class GameModel:
    def __init__(self, difficulty, player_name):
        print("Inicializando GameModel")
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = 100
        self.board = None
        self._generate_board()
        self.hidden_image = None
        self.images = {}
        self.images_loaded = False
        self._load_images()
        self.start_time = None
        self.moves = 0
        self.pairs_found = 0

    def _generate_board(self):
        image_ids = list(range(self.difficulty**2//2)) * 2
        random.shuffle(image_ids)
        board = []
        for i in range(0, len(image_ids), self.difficulty):
            row = image_ids[i:i + self.difficulty]
            board.append(row)
        self.board = board

    def _load_images(self):
        base_url = "https://raw.githubusercontent.com/Fluzze7/DI/main/sprint2python/images/"
        self.hidden_image = descargar_imagen(base_url + "hidden.png", self.cell_size)

        image_ids = [i for i in range(0, (self.difficulty**2)//2)]
        for image_id in image_ids:
            image_url = f"{base_url}{image_id}.png"
            self.images[image_id] = descargar_imagen(image_url, self.cell_size)

        # Comprobación de que todas las imágenes están cargadas
        self.images_loaded = len(self.images) == (self.difficulty**2 // 2)

    def images_are_loaded(self):
        return self.images_loaded

    def start_timer(self):
        self.start_time = time.time()  # Establecemos el tiempo inicial

    def get_elapsed_time(self):
        if self.start_time is None:
            return 0
        return int(time.time() - self.start_time)

    def check_match(self, pos1, pos2):
        return self.board[pos1[0]][pos1[1]] == self.board[pos2[0]][pos2[1]]

    def save_score(self, difficulty, name, moves, seconds):
        file_path = "ranking.json"
        results = self.load_results()
        print(f"Guardando resultado: {name}, {difficulty}, {moves}, {seconds}")

        if difficulty not in results:
            results[difficulty] = []

        new_result = {
            "nombre": name,
            "movimientos": moves,
            "tiempo": seconds,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Añadir el nuevo resultado y ordenar la lista por movimientos y tiempo
        results[difficulty].append(new_result)
        results[difficulty].sort(key=lambda x: (x["movimientos"], x["tiempo"]))

        # Mantener solo los tres mejores resultados
        results[difficulty] = results[difficulty][:3]
        try:
            with open(file_path, 'w') as f:
                # Escribir un diccionario vacío para borrar el contenido
                json.dump({}, f, indent=4)
            print("Contenido del archivo JSON borrado correctamente.")
        except Exception as e:
            print(f"Error al borrar el archivo JSON: {e}")

        try:
            with open(file_path, 'w') as f:
                print("Resultados guardados correctamente")
                json.dump(results, f, indent=4)
        except Exception as e:
            print(f"Error al guardar los resultados: {e}")

    def load_results(self):
        file_path = "ranking.json"
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    results = json.load(f)
                    print(f"Resultados cargados: {results}")  # Agregar para depuración
                    return results
            except json.JSONDecodeError:
                print("Error al leer el archivo JSON. El archivo puede estar corrupto.")
                return {4: [], 6: [], 8: []}
        else:
            print("Archivo ranking.json no encontrado. Se creará uno nuevo.")  # Agregar para depuración
            return {4: [], 6: [], 8: []}

