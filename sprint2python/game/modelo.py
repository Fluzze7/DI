import threading
import time
import random
from datetime import datetime
import json
from math import trunc

from recursos import descargar_imagen

class GameModel:
    def __init__(self,difficulty,player_name):
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
        image_ids = list(range(self.difficulty**2//2))*2
        random.shuffle(image_ids)
        board = []
        for i in range(0, len(image_ids),self.difficulty):
            row = image_ids[i:i+self.difficulty]
            board.append(row)

        print(board)
        self.board = board

    def _load_images(self):
        base_url = "https://raw.githubusercontent.com/Fluzze7/DI/main/sprint2python/images/"
        self.hidden_image = descargar_imagen(base_url+"hidden.png",self.cell_size)

        image_id = [i for i in range(0,((self.difficulty**2)//2))]
        print(image_id)
        for images in image_id:
            image_url = f"{base_url}{images}.png"
            self.images[images] = descargar_imagen(image_url,self.cell_size)



    def images_are_loaded(self):
        return True if self.images is not None else False

    def start_timer(self):
        pass

    def check_match(self,pos1,pos2):
        return True if self.board[pos1[0]][pos1[1]] == self.board[pos2[0]][pos2[1]] else False




    def is_game_complete(self):
        pass

    def save_score(self):
        pass

    def load_scores(self):
        pass



