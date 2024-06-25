#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

for num1 in range(1, 11):
    print("Tabla de multiplicar del: ", num1)
    for num2 in range(1, 11):
        print(f"{num1} x {num2} = {num1 * num2}")
    print()  

