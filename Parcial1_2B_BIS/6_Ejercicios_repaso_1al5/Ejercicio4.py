#solicitar 2 numeros al usuario
#y realizar todas las operaciones
#basicas de una calculadora(+,-,*,/)
#y mostrar por pantalla el resultado

print("Ingrese 2 numeros: ")
numero1 = int(input())
numero2 = int(input())
print("A continuacion se mostraran las operaciones basicas:")
operacion1 = numero1 + numero2
operacion2 = numero1 - numero2
operacion3 = numero2 - numero1
operacion4 = numero1 * numero2
operacion5 = numero1 / numero2
operacion6 = numero2 / numero1
print("El resultado de la suma de: ",numero1, "+" ,numero2, "es: \n", operacion1)
print("El resultado de la resta de: ",numero1, "-" ,numero2, "es: \n", operacion2)
print("El resultado de la resta de: ",numero2, "-" ,numero1, "es: \n", operacion3)
print("El resultado de la multiplicacion de: ",numero1, "*" ,numero2, "es: \n", operacion4)
print("El resultado de la division de: ",numero1, "/" ,numero2, "es: \n", operacion5)
print("El resultado de la division de: ",numero2, "/" ,numero1, "es: \n", operacion6)
