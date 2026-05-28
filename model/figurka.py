from abc import ABC, abstractmethod

Vektor = tuple[int, int]

class Figurka(ABC):
    def __init__(self, nazev, barva: int, pozice: Vektor):
        self.nazev:str = nazev
        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.barva:int = barva

        self.skok:bool = False

        self.pozice:Vektor = pozice

    def get_pozice(self) -> Vektor:
        pass

    def posun_figurky(self, vektor:Vektor):
        pass

class Jezdec(Figurka):
    def __init__(self, barva: int, pozice: Vektor):
        super().__init__("Jezdec", barva, pozice)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.skok:bool = True

class Kral(Figurka):
    def __init__(self, barva: int, pozice: Vektor):
        super().__init__("Král", barva, pozice)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.skok:bool = False

class Dama(Figurka):
    def __init__(self, barva: int, pozice: Vektor):
        super().__init__("Dáma", barva, pozice)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.skok:bool = False

class Vez(Figurka):
    def __init__(self, barva: int, pozice: Vektor):
        super().__init__("Věž", barva, pozice)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.skok:bool = False

class Strelec(Figurka):
    def __init__(self, barva: int, pozice: Vektor):
        super().__init__("Střelec", barva, pozice)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.skok:bool = False

class Pesec(Figurka):
    def __init__(self, barva: int, pozice: Vektor):
        super().__init__("Pěšec", barva, pozice)

        self.vektory:list[Vektor] = []
        self.vektory_utoku:list[Vektor] = []
        self.skok:bool = False




