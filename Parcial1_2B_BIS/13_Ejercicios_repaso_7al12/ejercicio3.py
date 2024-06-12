#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#el contenido de la lista en mayusculas

def listaa(lista):
    while not lista:
        palabra = input("Ingrese de favor una palabra o frase para llenar la lista: \n")
        if palabra:
            lista.append(palabra)

def letras_mayusculas(lista):
    for palabra in lista:
        print(palabra.upper())

lista_final = []
print("::..Bienvenido::..")
listaa(lista_final)
print("\nContenido de la lista:")
letras_mayusculas(lista_final)
