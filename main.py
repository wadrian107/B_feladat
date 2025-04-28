from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from LegiTarsasag import LegiTarsasag
from JegyFoglalas import JegyFoglalas

class FoglalasiRendszer:
    
    def __init__(self):
        self._legiTarsasag = LegiTarsasag("AirJet")
        self._init_data()
    
    def _init_data(self):
        self._legiTarsasag.jaratok = BelfoldiJarat(1254, "Debrecen", 11588)
        self._legiTarsasag.jaratok = NemzetkoziJarat(2243, "Prága", 35696)
        self._legiTarsasag.jaratok = NemzetkoziJarat(2567, "Helsinki", 45766)
        
        self._legiTarsasag.foglalasok = JegyFoglalas(1, 1254, "Kis Péter")
        self._legiTarsasag.foglalasok = JegyFoglalas(2, 2243, "Nagy Rozália")
        self._legiTarsasag.foglalasok = JegyFoglalas(3, 2567, "Kovács József")
        self._legiTarsasag.foglalasok = JegyFoglalas(4, 2567, "Tóth Andrea")
        self._legiTarsasag.foglalasok = JegyFoglalas(5, 1254, "Balogh Tamás")
        self._legiTarsasag.foglalasok = JegyFoglalas(6, 2243, "Kovács Ilona")

    
    def user_interact(self):
        while True:
            print("---------------------------------------------")
            print(f"Üdvözli az {self._legiTarsasag.nev} légitársaság!")
            print("Elérhető járataink:")
            self._legiTarsasag.jaratok
            print("1. Foglalások listázása")
            print("2. Jegy foglalása")
            print("3. Jegyfoglalás lemondása")
            print("4. Kilépés")
            
            menu = input("Válassz a fenti menüpontokból: ")
            print("---------------------------------------------")
            
            if menu == "1":
                self._legiTarsasag.foglalasok
            elif menu == "2":
                utas = input("Adja meg a nevét: ")
                jaratszam = int(input("Adja meg a járatszámot: "))
                if jaratszam in self._legiTarsasag.elerheto_jaratok_szamai():
                    max_azon = self._legiTarsasag.max_azon()
                    azonosito = max_azon + 1
                    self._legiTarsasag.foglalasok = JegyFoglalas(azonosito, jaratszam, utas)
                    print(f"Sikeres foglalás! A lefoglalt jegy ára: {self._legiTarsasag.jegyar_jaratszam(jaratszam)} huf")
                    print(f"A foglalás száma: {azonosito}, lemondás esetén ezt kell megadnia!")
                else:
                    print("Nincs ilyen számú elérhető járatunk jelenleg!")
            elif menu == "3":
                azonosito = int(input("Add meg a foglalás azonosítóját: "))
                if azonosito in self._legiTarsasag.azonositok():
                    self._legiTarsasag.lemondas(azonosito)
                    print("Foglalását sikeresen lemondta!")
                else:
                    print("Ilyen számon nem történt jegyfoglalás!")
            elif menu == "4":
                break
            

foglalasi_rendszer = FoglalasiRendszer()
foglalasi_rendszer.user_interact()