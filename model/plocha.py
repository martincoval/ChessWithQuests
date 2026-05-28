from typing import List

from figurka import Figurka

Souradnice = tuple[int, int]

class HerniPlocha:
    def __init__(self):
        self.rozmery: tuple[int, int] = (8, 8)
        self.herni_deska: list[list[Figurka | None]] = [[None for _ in range(8)] for _ in range(8)]
        self.vyhozene_figurky_b:list[Figurka] = []
        self.vyhozene_figurky_c:list[Figurka] = []

    def vrat_obsah(self, souradnice: Souradnice) -> Figurka | None:
        pass