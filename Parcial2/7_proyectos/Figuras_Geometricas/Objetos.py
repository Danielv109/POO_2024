
from Clases import *
#Print(Objeto 1):

rectangulo1 = Rectangulos(3, 4,True, 10,20)
rectangulo1.getInfo()

#Print(Objeto2):
circulo1 = Circulos(3, 3,True,6)
circulo1.getInfo()

print(f"Coordenadas del rectángulo: ({rectangulo1.getX()}, {rectangulo1.getY()})")
print(f"Área del rectángulo: {rectangulo1.calcularArea()}")

print(f"Radio del círculo: {circulo1.getRadio()}")
print(f"Área del círculo: {circulo1.calcularArea()}")