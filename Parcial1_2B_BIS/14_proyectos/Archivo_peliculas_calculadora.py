def agregar_pelicula(peliculas):
    nueva_pelicula = input("Introduce el nombre de la nueva película: ")
    peliculas.append(nueva_pelicula)
    print("La película", nueva_pelicula, "ha sido agregada.")

def remover_pelicula(peliculas):
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}.- {pelicula}")
    num_pelicula = int(input("Introduce el número de la película que deseas remover: ")) - 1
    if 0 <= num_pelicula < len(peliculas):
        removida = peliculas.pop(num_pelicula)
        print(f"La película '{removida}' ha sido removida.")
    else:
        print("Número inválido.")

def consultar_pelicula(peliculas):
    print("Películas disponibles:")
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}.- {pelicula}")

def buscar_pelicula(peliculas):
    nombre = input("Introduce el nombre de la película que deseas buscar: ")
    if nombre in peliculas:
        print(f"La película '{nombre}' está en la lista.")
    else:
        print(f"La película '{nombre}' no se encuentra en la lista.")

def vaciar_lista(peliculas):
    peliculas.clear()
    print("La lista de películas ha sido vaciada.")

def actualizar_pelicula(peliculas):
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}.- {pelicula}")
    num_pelicula = int(input("Introduce el número de la película que deseas actualizar: ")) - 1
    if 0 <= num_pelicula < len(peliculas):
        nuevo_nombre = input("Introduce el nuevo nombre de la película: ")
        peliculas[num_pelicula] = nuevo_nombre
        print("La película ha sido actualizada.")
    else:
        print("Número inválido.")

#Funciones para calculadora:
import os
import math

# Función para solicitar datos
def solicitarDatos(una_raiz=False):
    print("\n")
    n1 = int(input("Ingrese el Numero '1': "))
    if una_raiz:
        return n1, None
    n2 = int(input("Ingrese el Numero '2': "))
    return n1, n2


def getCalculadora(num1, num2, operacion):
    if operacion == "1" or operacion == "+" or operacion == "SUMA":
        resultado = f"{num1} + {num2} = {int(num1) + int(num2)}"
    elif operacion == "2" or operacion == "-" or operacion == "RESTA":
        resultado = f"{num1} - {num2} = {int(num1) - int(num2)}"
    elif operacion == "3" or operacion == "*" or operacion == "MULTIPLICACION":
        resultado = f"{num1} * {num2} = {int(num1) * int(num2)}"
    elif operacion == "4" or operacion == "/" or operacion == "DIVISION":
        resultado = f"{num1} / {num2} = {int(num1) / int(num2)}"
    elif operacion == "5" or operacion == "**" or operacion == "POTENCIA":
        resultado = f"{num1} ** {num2} = {int(num1) ** int(num2)}"
    elif operacion == "6" or operacion == "RAIZ":
        resultado = f"√{num1} = {math.sqrt(num1)}"
    else:
        resultado = "Operación no válida"
    return resultado


def esperaTecla():
    print("Presiona cualquier tecla para continuar...")
    input()
