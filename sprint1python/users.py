class User:
    def __init__(self,name,age,genre):
        self.name = name
        self.age = age
        self.genre = genre

    def to_str(self):
        return f"{self.name} ,{self.age} ,{self.genre}"