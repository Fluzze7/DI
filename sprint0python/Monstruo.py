from Heroe import *


class Monstruo:
    """
    Clase que representa a un monstruo en el juego.

    Atributos:
        nombre (str): El nombre del monstruo.
        ataque (int): La fuerza del monstruo, utilizada en combate.
        defensa (int): El valor de defensa del monstruo.
        salud (int): La cantidad de puntos de vida del monstruo.
    Métodos:
        atacar(heroe): Realiza un ataque contra el héroe.
        esta_vivo(): Devuelve True si el monstruo tiene más de 0 puntos de vida, de lo contrario False.
        mostrar_stats(): Muestra las estadísticas actuales del monstruo.
    """

    def __init__(self, nombre,ataque,defensa,salud):
        """
        Inicializa un nuevo monstruo con un nombre, ataque, defensa y salud.

        Args:
            nombre (str): El nombre del monstruo asignado.
            ataque (int): El valor de ataque del monstruo.
            defensa (int): El valor de la defensa del monstruo.
            salud (salud): El valor de la salud del monstruo.
        """
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    def atacar(self, heroe):
        """
        Realiza un ataque contra el héroe, calculando el daño basado en el ataque del monstruo y la defensa del héroe.

        Args:
            heroe (Heroe): Un objeto de la clase Heroe.

        El daño es calculado restando la defensa del héroe al ataque del monstruo.
        Si el daño es positivo, reduce la salud del héroe en esa cantidad.
        """
        print(f"El monstruo {self.nombre} ataca a {heroe.nombre}")
        damage = self.ataque - heroe.defensa
        if damage > 0:
            print(f"El héroe {heroe.nombre} ha recibido {damage} puntos de daño.")
            heroe.salud -= damage
        else:
            print("¡El héroe ha bloqueado el ataque!")

    def esta_vivo(self):
        """
        Devuelve True si el monstruo tiene más de 0 puntos de salud, de lo contrario devuelve False.

        Returns:
            bool: True si el monstruo está vivo, False si no.
        """
        return self.salud > 0

    def mostrar_stats(self):
        """
        Muestra en consola las estadísticas actuales del monstruo (ataque, defensa, salud).
        """
        print(f"un {self.nombre}:\nAtaque: {self.ataque}\nDefensa: {self.defensa}\nSalud: {self.salud}")
