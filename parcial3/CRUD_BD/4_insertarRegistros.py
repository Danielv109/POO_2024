from conexionBD import *


try:
    micursor=conexion.cursor()
    nombre=input("¿Cual es el nombre?:\n")
    direccion=input("¿Cual es tu direccion?:\n")
    tel=input("¿Cual es tu telefono?:\n")

    # sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. Centro', '6181563424')"

    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, '%s', '%s', '%s')"
    valores=(nombre,direccion,tel)

    micursor.execute(sql,valores)

    # Sirve para finalizar de manera exitosa la ejecicion del SQL
    conexion.commit()

except:
    print(f"Ocurrio un error con el sistema, por favor verifique más tarde.")

else:
    print(f"Registro insertado Exitosamente")