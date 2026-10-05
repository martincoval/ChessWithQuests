from herni_plocha import HerniPlocha

class RevizorTahu:
    def __init__(self, herni_plocha: HerniPlocha):
        self.herni_plocha = herni_plocha

    def ziskat_mozne_tahy(self, radek: int, sloupec: int) -> list[tuple[int,int]]:
        figurka = self.herni_plocha.vrat_obsah((radek, sloupec))
        if not figurka:
            return []

        mozne_pozice = []

        if figurka.skok_figury:
            for dr, ds in figurka.vektory:
                nr, ns = radek + dr, sloupec + ds
                if 0 <= nr < 8 and 0 <= ns < 8:
                    obsah = self.herni_plocha.vrat_obsah((nr,ns))
                    if obsah is None or obsah.barva !=figurka.barva:
                        mozne_pozice.append((nr,ns))

        else:
            for dr, ds in figurka.vektory:
                krok = 1
                while True:
                    nr, ns = radek + dr * krok, sloupec + ds * krok
                    if not (0 <= nr < 8 and 0 <= ns < 8):
                        break
                    obsah = self.herni_plocha.vrat_obsah((nr,ns))
                    if obsah is None:
                        mozne_pozice.append((nr,ns))
                    elif obsah.barva !=figurka.barva:
                        mozne_pozice.append((nr,ns))
                        break
                    else:
                        break

                    if figurka.nazev in ["Král", "Pěšec"]:
                        break
                    krok += 1
        return mozne_pozice
