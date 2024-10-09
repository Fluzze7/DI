from random import randrange

from Monstruo import *
from Tesoro import *


class Mazmorra:
    """
    Clase que representa una mazmorra donde el héroe se enfrentará a monstruos y buscará tesoros.

    Atributos:
        heroe (Heroe): Un objeto de la clase Heroe que participará en la mazmorra.
        monstruos (list): Lista de objetos Monstruo que el héroe enfrentará.
        tesoro (Tesoro): Objeto Tesoro que el héroe puede encontrar después de cada batalla.
    """

    def __init__(self, heroe):
        """
        Inicializa la mazmorra con un héroe, una lista de monstruos aleatorios y un tesoro.

        Args:
            heroe (Heroe): El héroe que explorará la mazmorra.
        """
        self.heroe = heroe
        # Se crea una lista de monstruos con valores aleatorios en ataque, defensa y salud.
        self.monstruos = [
            Monstruo("Zombie", 10 * randrange(3, 4, 1), 4 * randrange(2, 5, 1), 40),
            Monstruo("Esqueleto", 25, 25, 12 * randrange(2, 6, 1)),
            Monstruo("Orco", 5 * randrange(8,15,1), 25, 60)
        ]
        # Se asigna un objeto Tesoro, que interactuará con el héroe.
        self.tesoro = Tesoro(heroe)

    def jugar(self):
        """
        Inicia la secuencia del juego en la mazmorra. El héroe se enfrenta a cada monstruo de la lista.
        Después de derrotar a cada monstruo, se busca un tesoro.
        """
        self.heroe.mostrar_stats()  # Muestra las estadísticas iniciales del héroe.
        for enemigo in self.monstruos:
            print("Ha aparecido un monstruo en tu camino. Es ")
            enemigo.mostrar_stats()
            # Mientras tanto el héroe y el monstruo sigan vivos, se enfrentan.
            while enemigo.esta_vivo() and self.heroe.esta_vivo():
                self.enfrentar_enemigo(enemigo)
            if not self.heroe.esta_vivo():  # Si el héroe muere, el juego termina.
                break
            self.tesoro.encontrar_tesoro(self.heroe)  # Si el héroe sobrevive, busca un tesoro.
        if self.heroe.esta_vivo():
            print("Enhorabuena, has derrotado a todos los monstruos de la mazmorra.")
            print("Tus estadisticas finales son:")
            self.heroe.mostrar_stats()
        else:
            print("Más suerte la próxima vez.")  # El héroe ha muerto, se termina el juego.

    def enfrentar_enemigo(self, enemigo):
        """
        Gestiona el combate entre el héroe y un monstruo.

        Args:
            enemigo (Monstruo): Un objeto de la clase Monstruo con el que el héroe lucha.
        """
        a = 0
        # Bucle que se repite hasta que se elija una acción válida y mientras ambos sigan vivos.
        while a != 1 and a != 2 and a != 3 and self.heroe.esta_vivo() and enemigo.esta_vivo():
            a = input("¿Qué deseas hacer?\n1. Atacar\n2. Defender\n3. Curarse\n")
            a = int(a)
            if a == 1:
                self.heroe.atacar(enemigo)  # El héroe ataca al monstruo.
            elif a == 2:
                self.heroe.defenderse()  # El héroe se defiende.
            elif a == 3:
                self.heroe.curarse()  # El héroe se cura.
            else:
                print("Opción no válida.")

        if enemigo.esta_vivo():
            enemigo.atacar(self.heroe)  # El monstruo contraataca.
            if a == 2 and self.heroe.esta_vivo():
                self.heroe.reset_defensa()  # Vuelta a la normalidad de la defensa.
        else:
            print(f"El monstruo {enemigo.nombre} ha muerto.\nAhora descubre su tesoro.")
            return

        if not self.heroe.esta_vivo():
            print(f"El héroe {self.heroe.nombre} ha muerto.")  # Muestra por consola que el heroe ha muerto.
