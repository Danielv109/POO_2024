import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    port='3307'
)

except:
    print(f"Ocurrio un error con el sistema, por favor verifique más tarde.")

else:
#Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    micursor=conexion.cursor()
#ejecutar la consulta

    sql="CREATE DATABASE bd_python"
    micursor.execute(sql)


    if micursor:
        print(f"se creo bd exitosamente")

#Mostrar bases de datos que existen en el SGBD Mysql
    micursor.execute("SHOW DATABASES")

    for x in micursor:
        print(x)


