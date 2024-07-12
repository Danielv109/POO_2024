from conexionBD import *


try:
    micursor=conexion.cursor()

    sql="Update clientes set direccion='Col. Nueva Vizcaya' where id=1"
    micursor.execute(sql)

    conexion.commit()

except:
    print(f"Ocurrio un error con el sistema, por favor verifique más tarde.")

else:
    print(f"Registro eliminado exitosamente")