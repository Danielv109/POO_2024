#Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente:

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

#a.- 

lista1 = [2,4,6,1,3,8,7,5]

for i in lista1:
    print(i)

#b.- 

for i in lista1:
    valores= ""
    i_str = str(i)
    valores = valores +"," + i_str
    print(valores)


#c.- 

lista1.sort()
print(lista1)

#d.- 

print(len(lista1))

#e.-

buscar = int(input("Ingrese un numero que desee buscar en la lista: \n"))
if buscar in lista1:
    print("Ese valor si esta en la lista: " , buscar)
else:
    print("Ese valor no se encuentra en la lista.")

