from conexionbd import *

class Usuario:

    def __init__(self, id_usuario=None, nombre=None, apellido=None, correo=None, contrasena=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena

    def Insertar(self, conexion):
        cursor = conexion.cursor()
        query = "INSERT INTO usuarios (nombre, apellido, correo, contrasena) VALUES (%s, %s, %s, %s)"
        valores = (self.nombre, self.apellido, self.correo, self.contrasena)
        cursor.execute(query, valores)
        conexion.commit()
        print("Usuario creado correctamente")

    @staticmethod
    def Consultar(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM usuarios"
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                print(f"id_usuario: {fila[0]}, nombre: {fila[1]}, apellido: {fila[2]}, correo: {fila[3]}")
        else:
            print("No se encontraron registros.")
        
        input("\nPresiona Enter para volver al menú principal...")

    @staticmethod
    def Actualizar(conexion, id_usuario, nombre, apellido, correo, contrasena):
        cursor = conexion.cursor()
        query = "UPDATE usuarios SET nombre = %s, apellido = %s, correo = %s, contrasena = %s WHERE id_usuario = %s"
        valores = (nombre, apellido, correo, contrasena, id_usuario)
        cursor.execute(query, valores)
        conexion.commit()
        print("Actualización hecha correctamente")

    @staticmethod
    def Eliminar(conexion, id_usuario):
        cursor = conexion.cursor()
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        cursor.execute(query, (id_usuario,))
        conexion.commit()
        print("Usuario eliminado correctamente")
