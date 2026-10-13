from herni_plocha import HerniPlocha
from model.figurka import Strelec, Jezdec, Vez, Dama
from revizor_tahu import RevizorTahu
from tah import Tah
from notace import notace_do_souradnic

class GameManager:
    def __init__(self):
        self.herni_plocha = HerniPlocha()
        self.revizor = RevizorTahu(self.herni_plocha)
        self.aktivni_hrac = 1
        self.cil_en_passant: tuple[int, int] | None = (None)

    def zkontroluj_promoci_pesce(self, r_cil: int, s_cil: int, figurka) -> None:
        cilova_rada = 7 if figurka.barva == 1 else 0

        if figurka.nazev == "Pěšec" and r_cil == cilova_rada:
            print("Promoce pěšce")
            vyber = input("Vyber novou figurku - (D)áma, (V)ěž, (S)třelec, (J)ezdec:").strip().upper()
            if vyber == "V":
                nova_fig = Vez(figurka.barva)
            elif vyber == "S":
                nova_fig = Strelec(figurka.barva)
            elif vyber == "J":
                nova_fig = Jezdec(figurka.barva)
            else:
                nova_fig = Dama(figurka.barva)

            self.herni_plocha.nastav_obsah((r_cil, s_cil), nova_fig)
            print(f"Pěšec proměněn na {nova_fig.nazev}!")

    def zahraj_tah_notaci(self, odkud_str: str, kam_str: str) -> bool:
        r_start, s_start = notace_do_souradnic(odkud_str)
        r_cil, s_cil = notace_do_souradnic(kam_str)

        figurka = self.herni_plocha.vrat_obsah((r_start, s_start))

        if not figurka:
            print("Na výchozím políčku není žádná figurka!")
            return False
        if figurka.barva != self.aktivni_hrac:
            print("Nemůžeš hrát s figurkou soupeře!")
            return False

        mozne_tahy = self.revizor.ziskat_mozne_tahy(r_start, s_start, self.cil_en_passant)
        if (r_cil, s_cil) not in mozne_tahy:
            print(f"Tento tah není pro {figurka.nazev} povolen!")
            return False

        je_en_passant = (
            figurka.nazev == "Pěšec"
            and (r_cil, s_cil) == self.cil_en_passant
            and s_start != s_cil
        )

        tah = Tah((r_start, s_start),(r_cil,s_cil), figurka)
        uspech = self.herni_plocha.posun_figurky(tah)

        if uspech:
            if figurka.nazev == "Král" and abs(s_cil -s_start) == 2:
                if s_cil == 6:
                    vez = self.herni_plocha.vrat_obsah((r_start, 7))
                    self.herni_plocha.herni_deska[r_start][5] = vez
                    self.herni_plocha.herni_deska[r_start][7] = None
                    if vez:
                        vez.pohnula_se = True

                elif s_cil == 2:
                    vez = self.herni_plocha.vrat_obsah((r_start, 0))
                    self.herni_plocha.herni_deska[r_start][3] = vez
                    self.herni_plocha.herni_deska[r_start][0] = None
                    if vez:
                        vez.pohnula_se = True

            if je_en_passant:
                vyhozeny_pesec = self.herni_plocha.vrat_obsah((r_start, s_cil))
                if vyhozeny_pesec:
                    if vyhozeny_pesec.barva == -1:
                        self.herni_plocha.vyhozene_figurky_b.append(
                            vyhozeny_pesec
                        )
                    else:
                        self.herni_plocha.vyhozene_figurky_c.append(
                            vyhozeny_pesec
                        )
                    self.herni_plocha.herni_deska[r_start][s_cil] = None

            if figurka.nazev == "Pěšec" and abs(r_cil - r_start) == 2:
                stredovy_radek = (r_start + r_cil) // 2
                self.cil_en_passant = (stredovy_radek, s_start)
            else:
                self.cil_en_passant = None

            self.zkontroluj_promoci_pesce(r_cil, s_cil, figurka)
            self.aktivni_hrac *= -1
            return True
        return False

if __name__ == "__main__":
    gm = GameManager()

    while True:
        print("ŠACHOVNICE")
        gm.herni_plocha.vykresli()

        hrac_str = "bílý" if gm.aktivni_hrac == 1 else "černý"
        print(f"\nNa tahu je: {hrac_str}")

        odkud = input("Zadej pole ODKUD (nebo 'konec'): ").strip().lower()
        if odkud == "konec":
            break

        kam = input("Zadej pole KAM: ").strip().lower()

        uspech = gm.zahraj_tah_notaci(odkud, kam)
        if not uspech:
            print("Tah se nepodařilo provést, zkus to znovu.")



