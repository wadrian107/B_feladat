class JegyFoglalas:
    
    def __init__(self, azonosito, jaratszam, utas):
        self._azonosito = azonosito
        self._jaratszam = jaratszam
        self._utas = utas
    
    @property
    def utas(self):
        return self._utas
    
    @property
    def azonosito(self):
        return self._azonosito
    
    @property
    def jaratszam(self):
        return self._jaratszam
    
