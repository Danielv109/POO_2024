import mysql.connector 


try:
    conexion = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password ='',
    database = 'agencia_autos',
    port='3307'
    )

except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de excepcion: {type.__name__}")
    print(f"Ocurrio un error con el servidor... Por favor verifique...")


else:

    if conexion.is_connected():
        print(f"se creo la conexion con la base de datos exitosamente...")
    else:
        print(f"No fue posible conectarse a la base de datos..... verifique")
