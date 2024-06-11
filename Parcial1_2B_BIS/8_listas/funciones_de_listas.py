paises=["Mexico","USA","Brasil","Japon"]
numeros=[23,24,12,12.56,0.100,23]
texto=["Hola",True,23,3.1416]


# # Ordenar una lista
# print(paises)
# paises.sort()
# print(paises)

# print(numeros)
# numeros.sort()
# print(numeros)

# # Añadir elementos
# print(texto)
# texto.insert(len(texto),"True") # El insert sirve para ingresar algo en una especifica posicion
# print(texto)
# texto.insert(len(texto),True)    #Para que se ingrese algo siempre sin importar la posicion con el insert se coloca el (len(texto),VALOR A INSERTAR)
# print(texto)
# texto.append(False) # El append sirve para ingresar elemntos en la ultima posicion
# print(texto)

# # Eliminar elementos

# print(numeros)
# numeros.remove(23)   #  Para que no de error hay que poner un poner un elemnto a eliminar que se encuentre en la lista si no va dar error
# print(numeros)
# numeros.pop(0)       # Para eliminar un elemnto en una posicion debemos de usar pop, da error si no hay nada en la posicion ingresada
# print(numeros)

#Dar la vuelta a una lista

print(numeros)
numeros.reverse
print(numeros)

#Buscar un dato dentro de una lista 
respuesta = "Brasil" in paises
print(respuesta)


#Cuantas veces aparece un valor  dentro de una lista 
print(numeros)
numeros.append(23)
cuantos = numeros.count(23)
print("El numero '23' se encontro : ",cuantos)


#Unir listas 
print(paises)
paises.extend(numeros)
print(paises)
