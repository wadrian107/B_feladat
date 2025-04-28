from Jarat import Jarat

class NemzetkoziJarat(Jarat):
    
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)
    
    @property
    def jaratszam(self):
        return self._jaratszam
    
    @property
    def celallomas(self):
        return self._celallomas
    
    @property
    def jegyar(self):
        return self._jegyar
    
    @property
    def elerheto(self):
        return self._elerheto