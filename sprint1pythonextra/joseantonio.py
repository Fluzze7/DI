from random import randint
def get_jugada():
    z = randint(0,10)
    valor = "tijeras"
    if z < 4:
        valor = "piedra"
    elif 3 < z < 8:
        valor = "papel"
    return valor


