from abc import ABC, abstractmethod

Vektor = tuple[int, int]

class Figurka(ABC):
    def __init__(self, nazev, barva: int, skok_figury:bool):
        self.nazev:str = nazev
        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.barva:int = barva
        self.skok_figury: bool = skok_figury

    def __repr__(self):
        pismeno = self.nazev[0]
        return pismeno.upper() if self.barva == 1 else pismeno.lower()


class Jezdec(Figurka):
    def __init__(self, barva: int):
        super().__init__("Jezdec", barva, skok_figury = True)

        self.vektory:list[Vektor] = [
            (2, 1), (2,-1), (-2,1), (-2,-1),
            (1,2), (1,-2), (-1,2), (-1,-2),
        ]
        self.vektory_utoku:list[Vektor] = self.vektory

class Kral(Figurka):
    def __init__(self, barva: int):
        super().__init__("Král", barva, skok_figury = False)

        self.vektory:list[Vektor] = [
            (1,0), (0,1), (-1,0), (0,-1),
            (1, 1), (1,-1), (-1,-1), (-1,1),
            ]
        self.vektory_utoku:list[Vektor] = self.vektory

class Dama(Figurka):
    def __init__(self, barva: int):
        super().__init__("Dáma", barva, skok_figury = False)

        self.vektory:list[Vektor] = [
            (1,0), (0,1), (-1,0), (0,-1),
            (1, 1), (1,-1), (-1,-1), (-1,1),
        ]
        self.vektory_utoku:list[Vektor] = self.vektory

class Vez(Figurka):
    def __init__(self, barva: int):
        super().__init__("Věž", barva, skok_figury = False)

        self.vektory:list[Vektor] = [
            (1,0), (0,1), (-1,0), (0,-1),
        ]
        self.vektory_utoku:list[Vektor] = self.vektory

class Strelec(Figurka):
    def __init__(self, barva: int):
        super().__init__("Střelec", barva, skok_figury = False)

        self.vektory:list[Vektor] = [
            (1,1), (1,-1), (-1,1), (-1,-1),
        ]
        self.vektory_utoku:list[Vektor] = self.vektory

class Pesec(Figurka):
    def __init__(self, barva: int):
        super().__init__("Pěšec", barva, skok_figury = False)

        self.vektory:list[Vektor] = [
            (1 * self.barva, 0)
        ]
        self.vektory_utoku:list[Vektor] = [(1 * self.barva, 1), (1 * self.barva, -1)]