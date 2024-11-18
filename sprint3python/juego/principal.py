from Heroe import Heroe
from Monstruo import Monstruo
from Mazmorra import Mazmorra

def main():
    nombre_heroe = input("Introduce el nombre del héroe: ")
    heroe = Heroe(nombre_heroe)

    monstruos = [
        Monstruo("Goblin", 8, 3, 30),
        Monstruo("Orco", 12, 5, 50),
        Monstruo("Dragón", 20, 10, 100)
    ]

    mazmorra = Mazmorra(heroe, monstruos)
    mazmorra.jugar()

if __name__ == "__main__":
    main()
