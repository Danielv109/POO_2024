class Figuras:

    __CalcularArea = ""
    def CalcularArea(self,CalcularArea):
        self.CalcularArea = CalcularArea
        return self.CalcularArea
    
class Rectangulo(Figuras):

    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho

    def getLargo(self):
        return self.largo
    
    def setLargo(self,largo):
        self.largo = largo

    def getLargo(self):
        return self._largo
    
    def setLargo(self, value):
        self._largo = value

    def getAncho(self):
        return self._ancho
    
    def setAncho(self, value):
        self._ancho = value

    def calcular_area(self):
        return self.largo * self.ancho

class Circulo(Figuras):

    def _init_(self, radio):
        self.radio = radio

    def getRadio(self):
        return self._radio
    
    def setRadio(self, value):
        self._radio = value

    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2
