import threading
import time
import random
from datetime import datetime
import json

from recursos import descargar_imagen

class GameModel:
    def __init__(self,difficulty,player_name):
        print("Inicializando GameModel")
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size=100
        self.board = None
        self._generate_board()
        self.hidden_image = None
        self.images = {}
        self.images_loaded = threading.Event()
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

        image_id = [i for i in range(0,(self.difficulty*2))]

        for images in image_id:
            image_url = f"{base_url}{images}.png"
            self.images[images] = descargar_imagen(image_url,self.cell_size)



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
        return self.pairs_found == (self.difficulty **2)//2

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

        with open("ranking.txt", "w") as file:
            json.dump(scores, file)

    def load_scores(self):
        try:
            with open("ranking.txt", "r") as file:
                scores = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            scores = {"easy": [], "medium": [], "hard": []}

        return scores



