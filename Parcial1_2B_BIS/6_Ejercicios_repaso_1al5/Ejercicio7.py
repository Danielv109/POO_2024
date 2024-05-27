#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
print("Ingrese dos numeros: ")
num1 = int(input())
num2 = int(input())

if num1 > num2:
        num1, num2 = num2, num1
print("Los numeros impares entre: ", num1 ,"y" , num2)
for num in range(num1, num2 + 1):
        if num % 2 != 0:
            print(num, end=" ")
