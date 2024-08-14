import mysql.connector


try:
#Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_notas',
        port='3307'
)
    # crear un objeto de tipo cursos que tenga un parametro que permita reutilizar el objeto en cualquier conexion

    cursor=conexion.cursor(buffered=True)

except:
    print(f"Ocurrio un error con el sistema, por favor verifique más tarde.")

