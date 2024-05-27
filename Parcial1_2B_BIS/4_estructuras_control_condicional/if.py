"""
... Existeuna estructurade condicion llamada 'if' 
la cual evalua una condicion para encontrar el valor 'true' o se comple la condicion
se ejecuta la linea o lineas de codigo 

tienes 4 variantes de if

1.-if simple
2.-if compuesto
3.- if anidado
4.-if y elif
"""
#Ejemplo 1 if simple

color = "rojo"
if color =="rojo":
    print("soy el color rojo")

#Ejemplo 2 if compuesto

color = "rojo"
if color =="rojo":
    print("soy el color rojo")
else:
    print("no soy el color rojo")

#Ejemplo 3 if anidado

color = "rojo"
if color =="rojo":
    print("soy el color rojo")
    if color != "rojo":
        print("soy otro color")
else:
    print("no soy el color rojo")
    if color != "rojo":
        print("soy otro color")

#Ejemplo 4 elif 

color = "rojo"
if color =="rojo":
    print("soy el color rojo")
elif color == "negro":
    print("soy el color negro")
elif color == "verde":
    print("soy elcolor verde")
else:
    print("No soy rojo, verde o negro")