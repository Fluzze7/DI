import threading
import time
import random
from datetime import datetime
import json

from recursos import descargar_imagen

class GameModel:
    def __init__(self,difficulty,player_name,cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
        self.board_size = {"easy":4,"medium":6,"hard":8}.get(difficulty,4)
        self.board = self._generate_board()
        self.hidden_image = None
        self.images = {}
        self.start_time = None
        self.moves = 0
        self.pairs_found = 0
        self.images_loaded = threading.Event()
        self._load_images()

    def _generate_board(self):
        image_ids = list(range(self.board_size**2//2))*2
        random.shuffle(image_ids)
        board = []
        for i in range(0, len(image_ids),self.board_size):
            row = image_ids[i:i+self.board_size]
            board.append(row)
        return board

    def _load_images(self):
        base_url = "https://github.com/Fluzze7/sprint2python/images"
        self.hidden_image = descargar_imagen(base_url+"hidden.png",self.cell_size)

        image_id = [i for i in range(0,self.board_size)]

        for images in image_id:
            self.images[images] = descargar_imagen(base_url+f"{images}.png")

        if len(image_id) == len(self.images):
            self.images_loaded.set()

    def images_are_loaded(self):
        return self.images_loaded.is_set()
    def start_timer(self):
        self.start_time = time.time()
    def check_match(self,pos1,pos2):
        self.moves += 1
        if self.board[pos1[0]][pos1[1]]== self.board[pos2[0]][pos2[1]]:
            self.pairs_found +=1
            return True
        return False
    def is_game_complete(self):
        return self.pairs_found == (self.board_size **2)//2

    def save_score(self):
        score_data ={
            "name" : self.player_name,
            "difficulty" : self.difficulty,
            "moves" : self.moves,
            "date" : datetime.now().strftime("%Y-%m-%d")
        }

        scores = self.load_scores()

        scores[self.difficulty].append(score_data)
        scores[self.difficulty] = sorted(scores[self.difficulty],key=lambda x: x["moves"])[:3]

        with open("ranking.txt","w")as file:
            file.write(str(scores))

    def load_scores(self):
        try:
            with open("ranking.txt", "r") as file:
                scores = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            scores = {"easy": [], "medium": [], "hard": []}

        return scores



