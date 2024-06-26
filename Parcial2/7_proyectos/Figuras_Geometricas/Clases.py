class Figuras:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = True

    def setX(self,x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self,y):
        self.y = y

    def getY(self):
        return self.y

    def setVisible(self, visible: bool):
        self.visible = visible

    def getVisible(self) -> bool:
        return self.visible
    
    def estaVisible (self):
        self.estaVisible 
    
    def mostrar (self):
        self.mostrar

    def ocultar (self):
        self.ocultar

    def mover (self):
        self.mover

    def calcular (self):
        self.calcular

    def getInfo(self):
        print()

class Rectangulos(Figuras):
    def __init__(self, alto, ancho):
        super().__init__()
        self._alto = alto
        self._ancho = ancho

    def setAlto(self,alto):
        self._alto = alto

    def getAlto(self):
        return self._alto

    def setAncho(self,ancho):
        self._ancho = ancho

    def getAncho(self):
        return self._ancho

    def calcularArea(self) -> float:
        return self._alto * self._ancho

class Circulos(Figuras):
    def __init__(self, radio):
        super().__init__()
        self._radio = radio

    def setRadio(self,radio):
        self._radio = radio

    def getRadio(self):
        return self._radio

    def calcularArea(self) -> float:
        return 3.14 * self._radio ** 2
