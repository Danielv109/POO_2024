from conexionesBD import *

class Clientes:

    def __init__(self, id_cliente=None, nombre=None, direccion=None, telefono=None, email=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def Insertar(self, conexion):
        cursor = conexion.cursor()
        query = "INSERT INTO clientes (id_cliente, nombre, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.id_cliente, self.nombre, self.direccion, self.telefono, self.email)
        cursor.execute(query, valores)
        conexion.commit()
        print("Cliente creado correctamente")

    @staticmethod
    def Consultar(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM clientes"
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                print(f"id_cliente: {fila[0]}, nombre: {fila[1]}, direccion: {fila[2]}, telefono: {fila[3]}, email: {fila[4]}")
        else:
            print("No se encontraron registros.")
        
        input("\nPresiona Enter para volver al menú principal...")

    @staticmethod
    def Actualizar(conexion, id_cliente, nombre, direccion, telefono, email):
        cursor = conexion.cursor()
        query = "UPDATE clientes SET nombre = %s, direccion = %s, telefono = %s, email = %s WHERE id_cliente = %s"
        valores = (nombre, direccion, telefono, email, id_cliente)
        cursor.execute(query, valores)
        conexion.commit()
        print("Cliente actualizado correctamente")

    @staticmethod
    def Eliminar(conexion, id_cliente):
        cursor = conexion.cursor()
        query = "DELETE FROM clientes WHERE id_cliente = %s"
        cursor.execute(query, (id_cliente,))
        conexion.commit()
        print("Cliente eliminado correctamente")
