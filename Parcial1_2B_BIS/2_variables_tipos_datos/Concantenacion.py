#Fromas de concatenacion en python

Nombre = "Alejandro Villarreal"
Especialidad = "Area de SW multiplataforma"
Carrera = "Ingenieria en Gestion y Desarrollode Software"

#1er forma de concatenar

print("Mi nombre es:\n", Nombre , "Estoy en la especialidad de: \n", Especialidad , "\nEn la carrera de: \n", Carrera)

#2da forma de concatenar

print("Mi nombre es:\n", Nombre , "Estoy en la especialidad de: \n", Especialidad , "\nEn la carrera de: \n", Carrera)

#3er forma de concatenar, FORMA MAS COMUN EN PYTHON

print(f"Mi nombre es:\n, {Nombre} , Estoy en la especialidad de: \n, {Especialidad} , \nEn la carrera de: \n, {Carrera}")

#4ta forma de concatenar

print("Mi nombre es:\n, {} , Estoy en la especialidad de: \n, {} , \nEn la carrera de: \n, {}".format(Nombre, Especialidad, Carrera))

#5ta forma de concatenar

print('Mi nombre es:\n', Nombre , 'Estoy en la especialidad de: \n', Especialidad , '\nEn la carrera de: \n', Carrera)


