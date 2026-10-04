from figurka import Figurka


class Tah:
    def __init__(self, vychozi_pozice: tuple [int, int], cilova_pozice:tuple [int, int], figurka: Figurka, typ_tahu: str = "pohyb"):
        self.vychozi_pozice = vychozi_pozice
        self.cilova_pozice = cilova_pozice
        self.figurka = figurka
        self.typ_tahu = typ_tahu

    def __repr__(self):
        return f"Tah({self.figurka} z {self.vychozi_pozice} na {self.cilova_pozice})"
