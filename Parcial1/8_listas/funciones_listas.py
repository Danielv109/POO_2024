"""
List (Array)
son colecciones o conjunto de datos/valores bajo
un mismo nombre, para acceder a los valores se 
hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite miembros duplicados.

"""

# os.system("cls")

# #Ejemplo 1 crear una lista con datos numericos e imprimir el contenido

# lista = [23,34]
# print(lista)

# #recorre la lista con el for

# for i in lista:
#     print(i)

# #recorre la lista con el while
# i = 0
# while i<=len(lista)-1:
#     print(lista[i])
#     i+=1

# #Ejemplo 2 Crear una lista de 4 palabras, solicitar una palabra y buscar la coincidencia en la lista e indicar si la encontro o no y en que posicion 
# os.system("cls")
# palabras =["hola", "2024", "bye", "UTD"]
# palabra_buscar = input("Ingresa la palabra buscar: \n")
#if palabra_buscar in palabras:
#    print("La palabra esta en la lista: ", palabra_buscar)
#else:
#    print("La palabra no se encuentra en la lista")
# noencontre = True
# for i in palabras:
#     if palabra_buscar==i:
#         print("La palabra se encuentra en la lista: ", palabra_buscar)
#         noencontre = False
# if noencontre:
#     print("La palabra no se encuentra en la lista")

#Con while:

#Agregar y eliminar elementos de una lista

# numeros = [23,24]
# print(numeros)

# #agregar un elemento
# numeros.append(100)
# numeros.insert(3, 
#                200)

# #Eliminar un elemento
# numeros.remove(100)
# print(numeros)

# numeros.pop(2)
# print(numeros)

#Ejemplo 4.- Crear unalista nultidimensional (matriz) para almacenar los contactos telefonicos.

# agenda = [
#     ["Carlos", 6182334567],
#     ["Karin", 6182334567],
#     ["Leon", 6182334567],
#     ["Pedro", 6182334567],
#     ] 

# print(agenda)

# for i in agenda:
#     print(agenda.index(i)+1)


#Ejemplo 5.- Crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar,remover,consultar peliculas
#Notas:
#1.- Utilizar funciones y mandar llamar desde otro archivo
#2.- Utilizar las listas para almacenar los nombres de las peliculas

import Archivo_funciones_peliculas

print("\t...::BIENVENIDO!::...\nA continuación se muestran las películas disponibles.\n")
peliculas = [
    "Shrek",
    "La era de Hielo",
    "Toy story",
    "Sammy y el pasaje secreto",
    "Happy feet",
]

opciones = 4  # Número de iteraciones del menú

for i in range(opciones):
    Archivo_funciones_peliculas.consultar_pelicula(peliculas)
    print("\nMenu de Opciones: ")
    print("1.-Agregar peliculas\n2.-Remover peliculas\n3.-Consultar peliculas\n4.-Salir")
    opcion = input("¿Qué deseas hacer? \n")

    if opcion == "1":
        Archivo_funciones_peliculas.agregar_pelicula(peliculas)
    elif opcion == "2":
        Archivo_funciones_peliculas.remover_pelicula(peliculas)
    elif opcion == "3":
        Archivo_funciones_peliculas.consultar_pelicula(peliculas)
    elif opcion == "4":
        print("Gracias por usar el gestor de películas. ¡Hasta luego!")
    else:
        print("Opción no válida. Intenta de nuevo.")

