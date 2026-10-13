from herni_plocha import HerniPlocha

class RevizorTahu:
    def __init__(self, herni_plocha: HerniPlocha):
        self.herni_plocha = herni_plocha

    def ziskat_mozne_tahy(self, radek: int, sloupec: int, cil_en_passant=None) -> list[tuple[int,int]]:
        figurka = self.herni_plocha.vrat_obsah((radek, sloupec))
        if not figurka:
            return []

        mozne_pozice = []

        if figurka.nazev == "Pěšec":
            posun = 1 * figurka.barva
            startovni_rada = 1 if figurka.barva == 1 else 6

            nr = radek + posun
            if 0 <= nr < 8 and self.herni_plocha.vrat_obsah((nr,sloupec)) is None:
                mozne_pozice.append((nr,sloupec))

                nr2 = radek + 2 * posun
                if radek == startovni_rada and self.herni_plocha.vrat_obsah((nr2,sloupec)) is None:
                    mozne_pozice.append((nr2,sloupec))

                    for dr, ds in figurka.vektory_utoku:
                        ur, us = radek + dr, sloupec + ds
                        if 0 <= ur < 8 and 0 <= us < 8:
                            obsah = self.herni_plocha.vrat_obsah((ur,us))
                            if obsah is not None and obsah.barva !=figurka.barva:
                                mozne_pozice.append((ur, us))

                            elif (
                                obsah is None
                                and cil_en_passant is not None
                                and (ur, us) == cil_en_passant
                            ):
                                mozne_pozice.append((ur, us))

                    return mozne_pozice

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
