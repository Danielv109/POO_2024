#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?
print("Hola")
print("Ingrese el numero para sacar el porcentaje: ")
porcentaje = float(input())
print("Ingrese el número: ")
numero = float(input())
resultado = (porcentaje / 100) * numero
print(f"{porcentaje}% de {numero} es {resultado}")