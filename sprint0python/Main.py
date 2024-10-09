#imports de metodos y clases necesarias para instanciar el heroe y la mazmorra.
from Heroe import Heroe
from Mazmorra import Mazmorra

def main():
    """
    Instancia el nombre del objeto heroe para una partida, y crea una mazmorra con ese
    heroe a la que posteriormente se accede.
    """
    nombre_heroe = input("Nombre del heroe: ")
    heroe = Heroe(nombre_heroe)
    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()

if __name__ == "__main__": #Se asegura que se ejecute la función main() exclusivamente si el
    # archivo ejecutado es Main.py
    main()