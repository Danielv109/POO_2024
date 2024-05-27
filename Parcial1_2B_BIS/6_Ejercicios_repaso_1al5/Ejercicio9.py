#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa
print("Ingrese un numero (ingresar '111' para salir): ")
numero = int(input())

while numero != 111:
    print("Ingrese otro numero porfavor: ")
    numero = int(input())
else:
    print("Gracias")
