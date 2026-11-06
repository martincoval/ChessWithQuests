import tkinter as tk

class GameView:
    def __init__(self, root):
        self.root = root
        self.root.title("Šachy")

        self.velikost_pole = 60
        velikost_okna = self.velikost_pole * 8

        # Vytvoření plátna (Canvas) namísto mřížky tlačítek
        self.canvas = tk.Canvas(root, width=velikost_okna, height=velikost_okna)
        self.canvas.pack(padx=10, pady=10)

        self.vykresli_sachovnici()

    def vykresli_sachovnici(self):
        barva1 = "#f0d9b5"
        barva2 = "#b58863"

        for radek in range(8):
            for sloupec in range(8):
                gui_radek = 7 - radek
                gui_sloupec = sloupec

                x1 = gui_sloupec * self.velikost_pole
                y1 = gui_radek * self.velikost_pole
                x2 = x1 + self.velikost_pole
                y2 = y1 + self.velikost_pole

                aktualni_barva = barva1 if (radek + sloupec) % 2 == 0 else barva2

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=aktualni_barva, outline="")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameView(root)
    root.mainloop()