def notace_do_souradnic(zapis: str) ->tuple [int, int]:
    zapis = zapis.lower().strip()
    sloupec = ord(zapis[0]) - ord('a')
    radek = int(zapis[1]) - 1
    return sloupec, radek

def souradnice_do_notace(souradnice: tuple[int, int]) -> str:
    radek, sloupec = souradnice
    pismeno = chr(ord('a') + sloupec)
    cislo = radek + 1
    return f"{pismeno}{cislo}"