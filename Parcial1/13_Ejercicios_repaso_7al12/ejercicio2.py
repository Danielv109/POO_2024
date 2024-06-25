#Escribir un programa  que añada valores a una lista mientras que su longitud 
#sea menor a 120, y luego mostrar la lista: Usar un while y for

lista1 = []
nuevo_valor = input("Inserte el nuevo valor que desee agregar a la lista: \n")
for i in range(1):
    if len(nuevo_valor) < 120:
        lista1.append(nuevo_valor)
        print("El nuevo valor se ha agregado correctamente a la lista" , lista1)
    else:
        print("La longitud del valor debe de tener menos de '120'")
        break

print("Lista final usando for:" , lista1)


#Con while:

lista1 = []

# while True:
#     nuevo_valor = input("Inserte el nuevo valor que desee agregar a la lista: \n")
#     if len(nuevo_valor) < 120:
#         lista1.append(nuevo_valor)
#         print("El nuevo valor se ha agregado correctamente a la lista:", lista1)
#         break  
#     else:
#         print("La longitud del valor debe ser menor a 120 caracteres.")

# print("Lista final usando while:", lista1)