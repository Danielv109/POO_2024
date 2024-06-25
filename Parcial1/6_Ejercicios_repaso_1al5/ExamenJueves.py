#Realizar un programa en python que entregue promedio o calificaciones
AlumnosT = 0
SumaCalificacionesFinales = 0

while True:
    nombre = input("Ingrese el nombre del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    parcial1 = float(input("Ingrese la calificación del parcial 1: "))
    parcial2 = float(input("Ingrese la calificación del parcial 2: "))
    parcial3 = float(input("Ingrese la calificación del parcial 3: "))
    proyectoFinal = float(input("Ingrese la calificación del proyecto final: "))
    promedioParciales = (parcial1 + parcial2 + parcial3) / 3
    calificacionFinal = (promedioParciales + proyectoFinal) / 2
    print("Alumno: ",nombre)
    print("Carrera: ",carrera)
    print("Promedio de parciales: ",promedioParciales)
    print("Calificación final: ",calificacionFinal)
    if calificacionFinal < 80 or proyectoFinal < 50:
        print("Presenta examen extraordinario")
    AlumnosT += 1
    SumaCalificacionesFinales += calificacionFinal
    continuar = input("\n¿Desea capturar los datos de otro alumno? (si/no): ")
    if continuar != "si":
        break

PromedioFinaldeAlumnos = SumaCalificacionesFinales / AlumnosT
print("\nPromedio final de todos los alumnos capturados: ",PromedioFinaldeAlumnos)
