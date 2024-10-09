from Heroe import *

class Tesoro:
    """
    Clase que representa los distintos tesoros de la mazmorra.
    Atributos:
        beneficios (int): Valor numérico de la mejora que recibirá el héroe al encontrar el tesoro.
    Métodos:
        encontrar_tesoro(heroe): Aplica el efecto del tesoro sobre el héroe, restaurando su salud o mejorando estadísticas.
    """

    def __init__(self, beneficios):
        """
        Inicializa un tesoro con un valor de beneficios.

        Args:
            beneficios (int): Valor de los beneficios que otorgará el tesoro al héroe, como daño extra, defensa o salud.
        """
        self.beneficios = beneficios

    def encontrar_tesoro(self, heroe):
        """
        Aplica los efectos del tesoro sobre el héroe, restaurando su salud al máximo y mejorando su ataque.

        Args:
            heroe (Heroe): Un objeto de la clase Heroe.

        Al encontrar el tesoro, el héroe recupera toda su salud y su ataque aumenta en 5 puntos. Se muestra un mensaje en consola con las mejoras.
        """
        print(f"{heroe.nombre} ha encontrado un tesoro:")
        #heroe.salud = heroe.salud_maxima  # La salud del héroe se restaura al valor máximo.
        heroe.ataque += 5  # El ataque del héroe se incrementa en 5 puntos.
        print(f"El ataque de {heroe.nombre} aumenta a {heroe.ataque}.")
