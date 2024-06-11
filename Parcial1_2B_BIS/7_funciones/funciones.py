"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
   1.- Funcion que no recibe parametros y no regresa valor
   2.- Funcion que no recibe parametros y regresa valor
   3.- Funcion que recibe parametros y no regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#Ejemplo 1 Crear una funcion para imprimir nombres de personas
#    1.- Funcion que no recibe parametros y no regresa valor 
def solicitarNombres():
   nombre=input("Ingresa el nombre completo: ")

solicitarNombres()  

#Ejemplo 2 sumar dos numeros
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()    

#Ejemplo 3 sumar dos numeros 
#2.- Funcion que no recibe parametros y regresa valor
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejemplo 4 sumar dos numeros 
# 3.- Funcion que recibe parametros y no regresa valor
def suma(num1,num2):
    suma=num1+num2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejemplo 5 sumar dos numeros 
# 4.- Funcion que recibe parametros y regresa valor
def suma(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")

#Ejemplo 6 Crear un programa que solicite a traves de una funcion la siguiente informacion: Nombre del Paciente, Edad, Estatura, Tipo de Sangre. Utilizar los 4 tipos de funciones


def solicitar_informacion():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    estatura = input("Ingrese la estatura del paciente (en metros): ")
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")

    mostrar_informacion(nombre, edad, estatura, tipo_sangre)

solicitar_informacion()


def calcular_promedio_edad():
    cantidad_pacientes = int(input("Ingrese la cantidad de pacientes: "))
    suma_edades = 0

    for _ in range(cantidad_pacientes):
        edad = int(input("Ingrese la edad del paciente: "))
        suma_edades += edad

    promedio = suma_edades / cantidad_pacientes
    return promedio

# Función que recibe parámetros y no regresa valor
def mostrar_informacion(nombre, edad, estatura, tipo_sangre):
    print("\nInformación del paciente:")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Estatura:", estatura)
    print("Tipo de Sangre:", tipo_sangre)

# Función que recibe parámetros y regresa valor
def verificar_tipo_sangre(tipo_sangre):
    tipos_validos = ["A", "B", "AB", "O"]
    if tipo_sangre in tipos_validos:
        return True
    else:
        return False

tipo_sangre = input("Ingrese el tipo de sangre a verificar: ")
if verificar_tipo_sangre(tipo_sangre):
    print("El tipo de sangre ingresado es válido.")
else:
    print("El tipo de sangre ingresado no es válido.")



