import mysql.connector 

#conectar con la base de datos en mysql

try:
    conexion = mysql.connector.connect(
    host = '127.0.0.1', # o tambien se puede usar localhost
    user = 'root',
    password ='',
    database = 'bd_python',
    port='3307'
    )

except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de excepcion: {type.__name__}")
    print(f"Ocurrio un error con el servidor... Por favor verifique...")


else:

#verificar si la conexion fue exitosa

    if conexion.is_connected():
        print(f"se creo la conexion con la base de datos exitosamente...")
    else:
        print(f"No fue posible conectarse a la base de datos..... verifique")


