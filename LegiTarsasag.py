class LegiTarsasag:
    
    def __init__(self, nev):
        self._nev = nev
        self._jaratok = []
        self._foglalasok = []
    
    @property
    def nev(self):
        return self._nev
    
    @property        
    def jaratok(self):
        for jarat in self._jaratok:
            print(f"Járatszám: {jarat.jaratszam}, célállomás: {jarat.celallomas}, jegyár: {jarat.jegyar} huf, Elérhető: {jarat.elerheto}")
    
    @jaratok.setter
    def jaratok(self, uj_jarat):
        self._jaratok.append(uj_jarat)

    @property        
    def foglalasok(self):
        for foglalas in self._foglalasok:
            print(f"Azonosító: {foglalas.azonosito}, Járatszám: {foglalas.jaratszam}, Utas neve: {foglalas.utas}")
    
    @foglalasok.setter
    def foglalasok(self, uj_foglalas):
        self._foglalasok.append(uj_foglalas)
    
    def lemondas(self, azonosito):
        for foglalas in self._foglalasok:
            if foglalas.azonosito == azonosito:
                self._foglalasok.remove(foglalas)
    
    def azonositok(self):
        azonositok = []
        for foglalas in self._foglalasok:
            azonositok.append(foglalas.azonosito)
        return azonositok
    
    def max_azon(self):
        return max(self.azonositok())
    
    def jegyar_jaratszam(self, jaratszam):
        for jarat in self._jaratok:
            if jarat.jaratszam == jaratszam:
                jegyar = jarat.jegyar
        return jegyar
    
    def elerheto_jaratok_szamai(self):
        elerheto_jaratok_szamai = []
        for jarat in self._jaratok:
            if jarat.elerheto:
                elerheto_jaratok_szamai.append(jarat.jaratszam)
        return elerheto_jaratok_szamai
    
                