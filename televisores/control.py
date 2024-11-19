class Control:
    def __init__(self):
        self._tv = None
    
    def turnOn(self):
        self._tv.estado = True
    def turnOff(self):
        self._tv.estado = False
    
    def canalUp(self):
        if self._tv.estado == True:
            if self._tv.canal >=1 and self._tv.canal <120:
                self._tv.canal +=1
    def canalDown(self):
        if self._tv.estado == True:
            if self._tv.canal>1 and self._tv.canal >=120:
                self._tv.canal -=1
    
    def volumenUp(self):
        if self._tv.estado == True:
            if self._tv.volumen >=0 and self._tv.volumen<7:
                self._tv.volumen +=1
    def volumenDown(self):
        if self._tv.estado == True:
            if self._tv.volumen>0 and self._tv.volumen<=7:
                self._tv.volumen -=1
    
    def enlazar(self, Tv):
        self._tv = Tv
        self._tv.control = self

    def setTv(self, Tv):
        self._tv = Tv
    def getTv(self):
        return self._tv
    