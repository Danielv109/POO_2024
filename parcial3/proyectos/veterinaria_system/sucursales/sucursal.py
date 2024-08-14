from conexionbd import *


class Sucursal:

    def __init__(self, id_sucursal=None, nombre=None, direccion=None, telefono=None):
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def Insertar(self, conexion):
        cursor = conexion.cursor()
        query = "INSERT INTO sucursales (nombre, direccion, telefono) VALUES (%s, %s, %s)"
        valores = (self.nombre, self.direccion, self.telefono)
        cursor.execute(query, valores)
        conexion.commit()
        print("Sucursal creada correctamente")

    @staticmethod
    def Consultar(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM sucursales"
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                print(f"id_sucursal: {fila[0]}, nombre: {fila[1]}, direccion: {fila[2]}, telefono: {fila[3]}")
        else:
            print("No se encontraron registros.")
        
        input("\nPresiona Enter para volver al menú principal...")

    @staticmethod
    def Actualizar(conexion, id_sucursal, nombre, direccion, telefono):
        cursor = conexion.cursor()
        query = "UPDATE sucursales SET nombre = %s, direccion = %s, telefono = %s WHERE id_sucursal = %s"
        valores = (nombre, direccion, telefono, id_sucursal)
        cursor.execute(query, valores)
        conexion.commit()
        print("Actualización hecha correctamente")

    @staticmethod
    def Eliminar(conexion, id_sucursal):
        cursor = conexion.cursor()
        query = "DELETE FROM sucursales WHERE id_sucursal = %s"
        cursor.execute(query, (id_sucursal,))
        conexion.commit()
        print("Sucursal eliminada correctamente")
