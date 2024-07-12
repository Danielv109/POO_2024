from conexionBD import *


try:
    micursor=conexion.cursor()

    sql="create table clientes(id int primary key auto_increment, nombre varchar (60), direccion varchar (120), tel varchar(10))"

    micursor.execute(sql)
except:
    print(f"se creo la tabla exitosamente")

else:
    print(f"se creó la tabla Exitosamente")