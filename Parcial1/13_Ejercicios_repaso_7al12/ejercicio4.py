# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
# y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista1 = [1, 2, 3]
cadena = "Hola, mundo!"
num_entero = 42
logico = True

def mostrar_datos(variable):
    if isinstance(variable, list):
        print("Es una lista.")
    elif isinstance(variable, str):
        print("Es una cadena de texto.")
    elif isinstance(variable, int):
        print("Es un número entero.")
    elif isinstance(variable, bool):
        print("Es un valor lógico.")
    else:
        print("Hola.")


mostrar_datos(lista1)
mostrar_datos(cadena)
mostrar_datos(num_entero)
mostrar_datos(logico)
