from typing import List, Optional
from abc import ABC, abstractmethod
from herni_plocha import HerniPlocha, Tah, Souradnice

class Hra:
    def __init__(self, herni_rezim: int, aktualni_uzivatel: str):
        self.herni_rezim:int = herni_rezim
        self.aktualni_uzivatel:str = aktualni_uzivatel

        def get_herni_rezim() -> int:
            return self.herni_rezim

