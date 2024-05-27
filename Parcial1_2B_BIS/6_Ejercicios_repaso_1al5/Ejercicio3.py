#Escribir un programa que muestre los cuadrados
#(un numero multiplicado por si mismo) de los 60 primeros
#numeros naturales. Resolverlo con while y for

numero = 1
while numero <= 60:
    cuadradoNumero = numero * numero
    print("El cuadrado de: ", numero , "es: \n", cuadradoNumero)
    numero += 1

#Ahora con for:

for numero in range(61):
    cuadradoNumero = numero * numero
    print("El cuadrado de: ", numero , "es: \n", cuadradoNumero)
