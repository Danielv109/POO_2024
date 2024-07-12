from conexionBD import *


try:
    micursor=conexion.cursor()

    sql="DELETE FROM clientes WHERE id=1"
    micursor.execute(sql)

    conexion.commit()

except:
    print(f"Ocurrio un error con el sistema, por favor verifique más tarde.")

else:
    print(f"Registro eliminado exitosamente")