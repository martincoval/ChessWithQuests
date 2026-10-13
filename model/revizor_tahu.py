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

        if figurka.nazev == "Král":
            for dr, ds in figurka.vektory:
                nr, ns = radek + dr, sloupec + ds
                if 0 <= nr < 8 and 0 <= ns < 8:
                    obsah = self.herni_plocha.vrat_obsah((nr,ns))
                    if obsah is None or obsah.barva !=figurka.barva:
                        mozne_pozice.append((nr,ns))

            if not getattr(figurka, "pohnul_se", False) and sloupec == 4:
                vez_m = self.herni_plocha.vrat_obsah((radek, 7))
                if vez_m and vez_m.nazev == "Věž" and not getattr(figurka, "pohnul_se", False):
                    if (
                        self.herni_plocha.vrat_obsah((radek, 5)) is None
                        and self.herni_plocha.vrat_obsah((radek, 6)) is None
                    ):
                        mozne_pozice.append((radek, 6))

                vez_v = self.herni_plocha.vrat_obsah((radek, 0))
                if vez_v and vez_v.nazev == "Věž" and not getattr(figurka, "pohnul_se", False):
                    if (
                        self.herni_plocha.vrat_obsah((radek, 1)) is None
                        and self.herni_plocha.vrat_obsah((radek, 2)) is None
                        and self.herni_plocha.vrat_obsah((radek, 3)) is None
                    ):
                        mozne_pozice.append((radek, 2))

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

    def najdi_krale(self, barva:int) -> tuple[int, int] | None:
        for r in range(8):
            for s in range(8):
                fig = self.herni_plocha.vrat_obsah((r,s))
                if fig and fig.nazev == "Král" and fig.barva == barva:
                    return (r, s)
                return None

    def je_kral_v_sachu(self, barva:int) -> bool:
        pozice_krale = self.najdi_krale(barva)
        if not pozice_krale:
            return False

        souper_barva = -barva

        for r in range(8):
            for s in range(8):
                fig = self.herni_plocha.vrat_obsah((r,s))
                if fig and fig.barva == souper_barva:
                    if fig.nazev == "Pěšec":
                        tahy_soupere = []
                        for dr, ds in fig.vektory_utoku:
                            ur, us = r + dr, s + ds
                            if 0 <= ur < 8 and 0 <= us < 8:
                                tahy_soupere.append((ur, us))
                    else:
                        tahy_soupere = self.ziskat_mozne_tahy(r, s)

                    if pozice_krale in tahy_soupere:
                        return True
        return False