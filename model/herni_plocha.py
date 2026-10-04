from figurka import Figurka, Kral, Dama, Strelec, Jezdec, Vez, Pesec

class HerniPlocha:
    def __init__(self):
        self.rozmery: tuple[int,int] = (8,8)
        self.herni_deska: list[list[Figurka | None]] = [
            [None for _ in range(8)] for _ in range(8)
        ]
        self.vyhozene_figurky_b: list[Figurka] = []
        self.vyhozene_figurky_c: list[Figurka] = []

        self.inicializuj_desku()

    def vrat_obsah(self, souradnice:tuple[int,int]) -> Figurka | None:
        r,s = souradnice
        if 0 <= r < 8 and 0 <= s < 8:
            return self.herni_deska[r][s]
        return None

    def inicializuj_desku(self):
        self.herni_deska[0] = [
            Vez(1), Jezdec(1), Strelec(1), Dama(1), Kral(1), Strelec(1), Jezdec(1), Vez(1)]
        self.herni_deska[1] = [Pesec(1) for _ in range(8)]

        self.herni_deska[6] = [Pesec(-1) for _ in range(8)]
        self.herni_deska[7] = [
            Vez(-1), Jezdec(-1), Strelec(-1), Dama(-1), Kral(-1), Strelec(-1), Jezdec(-1), Vez(-1),]

    def vykresli(self):
        print("  0 1 2 3 4 5 6 7")
        for idx, radek in enumerate(reversed(self.herni_deska)):
            cislo_radku = 7 - idx
            r_str = " ".join([str(fig) if fig else "." for fig in radek])
            print(f"{cislo_radku} {r_str}")

    def posun_figurky(self, tah) -> bool:
        r_start, s_start = tah.vychozi_pozice
        r_cil, s_cil = tah.cilova_pozice

        figurka = self.herni_deska[r_start][s_start]
        if not(figurka):
            return False

        target = self.herni_deska[r_cil][s_cil]
        if target:
            if target.barva == 1:
                self.vyhozene_figurky_b.append(target)
            else:
                self.vyhozene_figurky_c.append(target)

        self.herni_deska[r_cil][s_cil] = figurka
        self.herni_deska[r_start][s_start] = None
        return True

if __name__ == "__main__":
    plocha = HerniPlocha()
    plocha.vykresli()
