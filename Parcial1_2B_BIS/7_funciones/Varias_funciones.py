def solicitarDatos():
    print("\n")
    n1 = int(input("Ingrese el Numero '1': "))
    n2 = int(input("Ingrese el Numero '2': "))

def getCalculadora(num1, num2, operacion):
    if operacion == "1" or operacion == "+" or operacion == "SUMA":
        resultado = f"{num1}+{num2}={int(num1) + int(num2)}"
    elif operacion == "2" or operacion == "-" or operacion =="RESTA":
        resultado = f"{num1}-{num2}={int(num1) - int(num2)}"
    elif operacion == "3" or operacion == "*" or operacion == "MULTIPLICACION":
        resultado = f"{num1}*{num2}={int(num1) * int(num2)}"
    elif operacion == "4" or operacion == "/" or operacion == "DIVISION":
        resultado = f"{num1}/{num2}={int(num1) / int(num2)}"
    return resultado

def esperaTecla():
    print("Presiona cualquier tecla para continuar...")
    input()
