"""
Nota: Cuando se imprime en pantalla una cadena de caracteres se trabaja por default
con 'cadenas'es decir, python no puede concatenar otra cosa que no sea un string (Str)
"""

texto = "Soy una cadena de caracteres"
numero = 23

#concatenar cadena str con str
print("Soy otra cadena y "+texto)
#concatenar un str con int
numero_str = str(numero)
print("El numero es:"+numero_str)

print("El numero es:"+str(numero))

#concatenar int con str
#ejercicio erroneo
n1 = "23"
n2 = 33
suma = n1+n2
print("La suma es:" + suma)
#ejercicio incorrecto
n1 = '23'
n2 = '33'
suma = int(n1+n2)
print("La suma es: "+str(suma))
#ejercicio correcto
n1 = int('23')
n2 = '33'
suma = int(n1+n2)
print("La suma es: "+str(suma))

print(f"La suma es: {suma}")

#concatenar float y int con str
n1 = 23
n2 = 33.0
suma = float(n1)+n2
print(f"La suma es: "+{suma})