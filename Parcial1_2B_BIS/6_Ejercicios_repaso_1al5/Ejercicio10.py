#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
aprobados = 0
reprobados = 0
total_alumnos = 15
calificacion_minima_aprobatoria = 60

for i in range(1, total_alumnos + 1):
        calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
        if calificacion >= calificacion_minima_aprobatoria:
            aprobados += 1
        else:
            reprobados += 1
print(f"Alumnos que aprobaron: {aprobados}")
print(f"Alumnos que no aprobaron: {reprobados}")