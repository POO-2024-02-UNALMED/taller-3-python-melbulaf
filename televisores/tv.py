class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self.canal = 1
        self._precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        self._numTV +=1
    
    def setMarca(self,marc):
        self._marca = marc
    def getMarca(self):
        return self._marca
    
    def setPrecio(self, pre):
        self._precio = pre
    def getPrecio(self):
        return self._precio
    
    def setControl(self, cont):
        self.control = cont
    def getControl(self):
        return self.control
    
    def setCanal(self, cl):
        if self.estado == True:
            if cl >= 1 and cl <= 120:
                self.canal = cl
    def getCanal(self):
        return self.canal
    
    def setVolumen(self, vol):
        if self.estado == True:
            if vol >= 0 and vol <= 7:
                self.volumen = vol
    def getVolumen(self):
        return self.volumen
    
    @classmethod
    def setNumTV(self, num):
        self._numTV = num
    @classmethod
    def getNumTV(self):
        return self._numTV
    
    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False
    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado == True:
            if self.canal >=1 and self.canal <120:
                self.canal +=1
    def canalDown(self):
        if self.estado == True:
            if self.canal>1 and self.canal >=120:
                self.canal -=1
    
    def volumenUp(self):
        if self.estado == True:
            if self.volumen >=0 and self.volumen<7:
                self.volumen +=1
    def volumenDown(self):
        if self.estado == True:
            if self.volumen>0 and self.volumen<=7:
                self.volumen -=1
    

