#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario
print("Ingrese dos numeros: ")
numero1 = int(input())
numero2 = int(input())

if numero1 < numero2:
    for num in range(numero1 + 1, numero2):
        print("El siguiente numero esta entre el ultimo numero que agrego: \n",num)
elif numero1 > numero2:
    for num in range(numero2 + 1, numero1):
        print("El siguiente numero esta entre el ultimo numero que agrego: \n",num)
else:
    print("Los números son iguales, no hay números entre ellos.")