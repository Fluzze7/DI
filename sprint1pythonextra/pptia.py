from random import randint

class IA:
    def __init__(self):
        self.option = ["rock","paper","scissors"]

    def answer(self):
        file = open("C:\\Users\\josea\\Desktop\\git\\DI\\sprint1pythonextra\\tendencies", "r+")
        rock_count = int(file.readline().split(":")[1])
        paper_count = int(file.readline().split(":")[1])
        scissors_count = int(file.readline().split(":")[1])
        total_picks = rock_count + paper_count + scissors_count
        rock_probability = round(rock_count / total_picks * 100,2)
        paper_probability = round(paper_count / total_picks * 100,2)
        selection = randint(0,100)

        if selection <= rock_probability:
            return self.option[0]
        if rock_probability < selection <= (paper_probability+rock_probability):
            return  self.option[1]
        else:
            return self.option[2]
