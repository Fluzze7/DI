#clase utilizada por reguser.py para facilitar tareas de manejo de datos
class User:
    def __init__(self,name,age,genre):
        self.name = name
        self.age = age
        self.genre = genre

    def to_str(self):
        """
        :return:(str) Devuelve un string con todos los atributos de user
        """
        return f"{self.name} ,{self.age} ,{self.genre}"