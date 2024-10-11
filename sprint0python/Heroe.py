from random import randrange #metodo utilizado para obtener un numero aleatorio en distintos atributos


class Heroe:
    """
        Clase que representa a un héroe en el juego.

    Atributos:
        nombre (str): El nombre del héroe.
        ataque (int): La fuerza del héroe, utilizada en combate.
        defensa (int): El armadura del héroe, utilizada en combate.
        salud (int): La cantidad de puntos de vida del héroe.
        salud_maxima (int): Valor numerico máximo de la vida del heroe
    Métodos:
        atacar(enemigo): Ataca a un enemigo y reduce su salud en función del ataque y la defensa.
        curarse(): Aumenta la salud del héroe, hasta un máximo de 100 puntos de vida.
        defenderse(): Incrementa temporalmente la defensa del héroe.
        reset_defensa(): Restaura la defensa del héroe a su estado original.
        esta_vivo(): Retorna True si el héroe tiene más de 0 puntos de salud.
        mostrar_stats(): Muestra las estadísticas actuales del héroe.

    """
    def __init__(self,nombre):
        """
        :param nombre: String
        El nombre es asignado manualmente.
        El resto de parametros están preestablecidos o se asignan aleatoriamente en un rango con randrange()
        """
        self.nombre = nombre
        self.ataque = 10*randrange(3,4,1)
        self.defensa = 12*randrange(2,3,1)
        self.salud = 100
        self.salud_maxima = 100

    def atacar(self,enemigo):
        """
        :param enemigo: un objecto de la clase Monstruo
        El objeto enemigo recibe una reducción de su salud {enemigo.salud} - {heroe.ataque}
        """
        print("El heroe ataca a",enemigo.nombre)
        damage = self.ataque - enemigo.defensa
        if damage > 0:
            print("El enemigo ",enemigo.nombre," ha recibido ",damage," puntos de daño.")
            enemigo.salud -= damage
        else:
            print("El enemigo ha bloqueado el ataque!")

    def curarse(self):
        """
        El objeto heroe aumenta su salud {heroe.salud} 10 puntos de vida. Como máximo tendrá 100 puntos de vida.
        """
        if self.salud>90:
            self.salud=100
            print("La salud esta al máximo.")
        else:
            self.salud += 10
            print("El heroe se ha curado. Salud actual = ",self.salud)

    def defenderse(self):
        """
        El objeto heroe aumentará su defensa {heroe.defensa} en 5.
        """
        self.defensa += 5
        print("Defensa aumentada temporalmente a = ",self.defensa)



    def reset_defensa(self):
        """
        El objeto heroe reducirá su defensa {heroe.defensa} al estado base.
        """
        print("La defensa de ", self.nombre," ha vuelto a la normalidad.")
        self.defensa -= 5

    def esta_vivo(self):
        """
        Función que devuelve True si la salud del heroe {heroe.salud} > 0, sino devuelve Flase.
        :return: boolean
        """
        return self.salud > 0

    def mostrar_stats(self):
        """
        Muestra en consola el valor de los distintos atributos del objeto heroe.
        """
        print("Ataque: ",self.ataque,"\nDefensa: ",self.defensa,"\nSalud: ",self.salud)