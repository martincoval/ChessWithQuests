from typing import List, Optional


from figurka import Figurka, Kral, Dama, Vez, Strelec, Jezdec, Pesec

Souradnice = tuple[int, int]

class Tah:
    def __init__(self, vychozi_pozice: Souradnice, cilova_pozice: Souradnice, figurka: Figurka, typ_tahu: str = "standardni"):
        self.vychozi_pozice: Souradnice = vychozi_pozice
        self.cilova_pozice: Souradnice = cilova_pozice
        self.figurka: Figurka = figurka
        self.typ_tahu: str = typ_tahu
        self.smer_pohybu: list[bool] = []

    def proved_tah(self) -> None:
        pass


class HerniPlocha:
    def __init__(self):
        self.rozmery: tuple[int, int] = (8, 8)
        self.herni_deska: list[list[Figurka | None]] = [[None for _ in range(8)] for _ in range(8)]
        self.vyhozene_figurky_b:list[Figurka] = []
        self.vyhozene_figurky_c:list[Figurka] = []

        self.tah: Optional[Tah] = None
        self.obsazene_pozice_v_seznamu: list[Souradnice] = []
        self.check_mat: bool = False
        self.check_pat: bool = False

        self._inicializuj_desku()

    def _inicializuj_desku(self) -> None:
        self.herni_deska[0][0] = Vez(barva=1)
        self.herni_deska[0][1] = Jezdec(barva=1)
        self.herni_deska[0][2] = Strelec(barva=1)
        self.herni_deska[0][3] = Dama(barva=1)
        self.herni_deska[0][4] = Kral(barva=1)
        self.herni_deska[0][5] = Strelec(barva=1)
        self.herni_deska[0][6] = Jezdec(barva=1)
        self.herni_deska[0][7] = Vez(barva=1)
        for i in range(8):
            self.herni_deska[1][i] = Pesec(barva=1)

        for i in range(8):
            self.herni_deska[6][i] = Pesec(barva=0)
        self.herni_deska[7][0] = Vez(barva=0)
        self.herni_deska[7][1] = Jezdec(barva=0)
        self.herni_deska[7][2] = Strelec(barva=0)
        self.herni_deska[7][3] = Dama(barva=0)
        self.herni_deska[7][4] = Kral(barva=0)
        self.herni_deska[7][5] = Strelec(barva=0)
        self.herni_deska[7][6] = Jezdec(barva=0)
        self.herni_deska[7][7] = Vez(barva=0)

        self._aktualizuj_obsazene_pozice()

    def _aktualizuj_obsazene_pozice(self) -> None:
        pass

    def vrat_obsah(self, souradnice: Souradnice) -> Figurka | None:
        pass

    def posun_figurky(self, tah: Tah) -> bool:
        pass

    def nahrad_figurku(self, figurka: Figurka, tah: Tah) -> None:
        pass