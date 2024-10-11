

class Tesoro:
    """
    Clase que representa los distintos tesoros de la mazmorra.
    Atributos:
        beneficios (int): Valor numérico de la mejora que recibirá el héroe al encontrar el tesoro.
    Métodos:
        encontrar_tesoro(heroe): Aplica el efecto del tesoro sobre el héroe, restaurando su salud o mejorando estadísticas.
    """


    def __init__(self, heroe):
            """
            Inicializa un tesoro para el heroe.

            :param heroe (heroe): heroe que recibirá la recompensa

        self.heroe = heroe
            """
            self.heroe = heroe

    def encontrar_tesoro(self, beneficio):
        """
        Aplica los efectos del tesoro sobre el héroe.

        Args:
            beneficio (int):Opción de beneficio.

        Al encontrar el tesoro, se muestra un mensaje en consola con las mejoras.
        """
        print(f"{self.heroe.nombre} ha encontrado un tesoro:")
        if beneficio==1:
            self.heroe.salud = self.heroe.salud_maxima
            print("El heroe ha restaurado su salud al completo.")
        elif beneficio==2:
            self.heroe.ataque +=10
            print(f"El ataque del heroe ha aumentado a {self.heroe.ataque}")
        elif beneficio==3:
            self.heroe.defensa +=5
            print(f"La defensa del heroe ha aumentado a {self.heroe.defensa}")