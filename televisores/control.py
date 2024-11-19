class Control:
    def __init__(self):
        self._tv = None
    
    def turnOn(self):
        self._tv.estado = True
    def turnOff(self):
        self._tv.estado = False
    
    def setCanal(self, canal):
        if self._tv.estado and 1 <= canal <= 120:
            self._tv.canal = canal
    def canalUp(self):
        if self._tv.estado and self._tv.canal < 120: 
            self._tv.canal += 1
    def canalDown(self):
        if self._tv.estado and self._tv.canal > 1:  
            self._tv.canal -= 1
    
    def setVolumen(self, volumen):
        if self._tv.estado and 0 <= volumen <= 7:
            self._tv.volumen = volumen
    def volumenUp(self):
        if self._tv.estado and self._tv.volumen < 7:  
            self._tv.volumen += 1
    def volumenDown(self):
        if self._tv.estado and self._tv.volumen > 0:  
            self._tv.volumen -= 1

    def enlazar(self, Tv):
        self._tv = Tv
        self._tv.control = self

    def setTv(self, Tv):
        self._tv = Tv
    def getTv(self):
        return self._tv
    