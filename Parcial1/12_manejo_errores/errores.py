#Los errores de excepciones en un lenguaje de programacion no es otra cosa que los errores en tiempo de ejecucio  . Cuando se manejan los errores mediante las excepciones en realidad se dice que se evita que se presete esos errores en el programa en el tiempo de ejecucion.

#Ejemplo. Se presenta un error cuando no es generada una variable 


# try:
#     nombre = input("Dame el nombre completo de una persona: \n")

#     if len(nombre) > 0:
#         nombre_usuario = "El nombre de usuario del sistema es: \n" + nombre
#         print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre de una persona")


#Ejemplo 2: Cuando se solicita un numero y se ingresa otra cosa

try:
    numero = int(input("Ingresa un numero: \n"))
    if numero > 0:
        print("Soy un numero entero positivo")
    else:
        print("Soy un numero entero negativo")
except ValueError:
    print("No es posible convertir una letra a un numero, favor de verificar....")


#Ejemplo 3: Cuando se generan multpiles excepciones 

try:
    numero = int(input("Ingresa un numero. \n"))
    print("El cuadrado del numero es: " + str(numero*numero))
except TypeError:
    print("Es necesario convertir el numero a entero")
except ValueError:
    print("No es posible convertir una letra a un numero, verifica por favor...")
else:
    print("Todo se ejecuto sin errores..")

finally:
    print("Ya termino, gracias")


