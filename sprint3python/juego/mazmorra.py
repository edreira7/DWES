from Heroe import Heroe
from Monstruo import Monstruo
from Tesoro import Tesoro

class Mazmorra:
    def __init__(self, heroe, monstruos):
        self.heroe = heroe
        self.monstruos = monstruos
        self.tesoro = Tesoro()

    def jugar(self):
        print("Héroe entra en la mazmorra.")
        for monstruo in self.monstruos:
            print(f"Te has encontrado con un {monstruo.nombre}.")
            self.enfrentar_enemigo(monstruo)
            if not self.heroe.esta_vivo():
                print("Héroe ha sido derrotado en la mazmorra.")
                return
            self.buscar_tesoro()
        print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")

    def enfrentar_enemigo(self, enemigo):
        while self.heroe.esta_vivo() and enemigo.esta_vivo():
            print("\n¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defenderse")
            print("3. Curarse")
            eleccion = input("Elige una opción (1/2/3): ")

            if eleccion == "1":
                self.heroe.atacar(enemigo)
            elif eleccion == "2":
                self.heroe.defenderse()
            elif eleccion == "3":
                self.heroe.curarse()
            else:
                print("Opción no válida.")

            if enemigo.esta_vivo():
                enemigo.atacar(self.heroe)

            self.heroe.reset_defensa()

    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)
