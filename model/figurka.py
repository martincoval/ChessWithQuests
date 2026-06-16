from abc import ABC, abstractmethod

Vektor = tuple[int, int]

class Figurka(ABC):
    def __init__(self, nazev, barva: int, skok_figury:bool):
        self.nazev:str = nazev
        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.barva:int = barva
        self.skok_figury: bool = skok_figury


class Jezdec(Figurka):
    def __init__(self, barva: int):
        super().__init__("Jezdec", barva, skok_figury = True)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []

class Kral(Figurka):
    def __init__(self, barva: int):
        super().__init__("Král", barva, skok_figury = False)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []

class Dama(Figurka):
    def __init__(self, barva: int):
        super().__init__("Dáma", barva, skok_figury = False)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []

class Vez(Figurka):
    def __init__(self, barva: int):
        super().__init__("Věž", barva, skok_figury = False)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []

class Strelec(Figurka):
    def __init__(self, barva: int):
        super().__init__("Střelec", barva, skok_figury = False)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []

class Pesec(Figurka):
    def __init__(self, barva: int):
        super().__init__("Pěšec", barva, skok_figury = False)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []