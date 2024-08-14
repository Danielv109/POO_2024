from conexionesBD import *
from Funciones.funciones import *

class Autos:

    def __init__(self, matricula=None, marca=None, modelo=None, año=None, color=None):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def Insertar(self, conexion):
        cursor = conexion.cursor()
        query = "INSERT INTO autos (matricula, marca, modelo, anio, color) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.matricula, self.marca, self.modelo, self.año, self.color)
        cursor.execute(query, valores)
        conexion.commit()
        print("Auto creado correctamente")

    @staticmethod
    def Consultar(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM autos"
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                print(f"Matricula: {fila[0]}, Marca: {fila[1]}, Modelo: {fila[2]}, Año: {fila[3]}, Color: {fila[4]}")
        else:
            print("No se encontraron registros.")
        
        input("\nPresiona Enter para volver al menú principal...")

    @staticmethod
    def Actualizar(conexion, matricula, marca, modelo, año, color):
        cursor = conexion.cursor()
        query = "UPDATE autos SET marca = %s, modelo = %s, anio = %s, color = %s WHERE matricula = %s"
        valores = (marca, modelo, año, color, matricula)
        cursor.execute(query, valores)
        conexion.commit()
        print("Actualización hecha correctamente")

    @staticmethod
    def Eliminar(conexion, matricula):
        cursor = conexion.cursor()
        query = "DELETE FROM autos WHERE matricula = %s"
        cursor.execute(query, (matricula,))
        conexion.commit()
        print("Auto eliminado correctamente")

