import mysql.connector


try:
#Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
)
    
except:
    print(f"Ocurrio un error con el sistema, por favor verifique más tarde.")

#es lo mismos que lo de arriba
# conexion=mysql.connector.conect('localhost','root','','bd_python')

#verificar si la conexion fue exitosa
# if conexion.is_connected():
#     print(f"Se creo la conexion con la bd exitosamente...")

# else:
#     print(f"No fre posible conectar con la BD...verifique...")

    