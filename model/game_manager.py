from herni_plocha import HerniPlocha
from revizor_tahu import RevizorTahu
from tah import Tah

class GameManager:
    def __init__(self):
        self.herni_plocha = HerniPlocha()
        self.revizor = RevizorTahu(self.herni_plocha)
        self.aktivni_hrac = 1

    def zahraj_tah(self, r_start: int, s_start: int, r_cil: int, s_cil: int) -> bool:
        figurka = self.herni_plocha.vrat_obsah((r_start, s_start))

        if not figurka:
            print("Na výchozím políčku není žádná figurka!")
            return False
        if figurka.barva != self.aktivni_hrac:
            print("Nemůžeš hrát s figurkou soupeře!")
            return False

        mozne_tahy = self.revizor.ziskat_mozne_tahy(r_start, s_start)
        if (r_cil, s_cil) not in mozne_tahy:
            print(f"Tento tah není pro {figurka.nazev} povolen!")
            return False

        tah = Tah((r_start, s_start),(r_cil,s_cil), figurka)
        uspech = self.herni_plocha.posun_figurky(tah)

        if uspech:
            self.aktivni_hrac *= -1
            return True
        return False

if __name__ == "__main__":
    gm = GameManager()

    print("Počáteční šachovnice")
    gm.herni_plocha.vykresli()

    print("\n--- Bílý táhne pěšákem z [1, 4] na [2, 4] ---")
    if gm.zahraj_tah(1, 4, 2, 4):
        gm.herni_plocha.vykresli()




