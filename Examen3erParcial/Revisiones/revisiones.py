from conexionesBD import *
from Funciones.funciones import *

class Revisiones:

    def __init__(self, no_revision=None, cambiofiltro=None, cambioaceite=None, cambiofrenos=None, otros=None, matricula=None):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula

    def Insertar(self, conexion):
        cursor = conexion.cursor()
        query = "INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula)
        cursor.execute(query, valores)
        conexion.commit()
        print("Revisión creada correctamente")

    @staticmethod
    def Consultar(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM revisiones"
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                print(f"no_revision: {fila[0]}, cambiofiltro: {fila[1]}, cambioaceite: {fila[2]}, cambiofrenos: {fila[3]}, otros: {fila[4]}, matricula: {fila[5]}")
        else:
            print("No se encontraron registros.")
        
        input("\nPresiona Enter para volver al menú principal...")

    @staticmethod
    def Actualizar(conexion, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        cursor = conexion.cursor()
        query = "UPDATE revisiones SET cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s, matricula = %s WHERE no_revision = %s"
        valores = (cambiofiltro, cambioaceite, cambiofrenos, otros, matricula, no_revision)
        cursor.execute(query, valores)
        conexion.commit()
        print("Actualización hecha correctamente")

    @staticmethod
    def Eliminar(conexion, no_revision):
        cursor = conexion.cursor()
        query = "DELETE FROM revisiones WHERE no_revision = %s"
        cursor.execute(query, (no_revision,))
        conexion.commit()
        print("Revisión eliminada correctamente")




    # def Consultar(self, conexion):
    #     cursor = conexion.cursor()
    #     query = "SELECT * FROM revisiones"
    #     cursor.execute(query)
    #     resultados = cursor.fetchall()
    #     for fila in resultados:
    #         print(f"no_revision: {fila[0]}, cambiofiltro: {fila[1]}, cambioaceite: {fila[2]}, cambiofrenos: {fila[3]}, otros: {fila[4]}, matricula: {fila[5]}")


    # def Insertar(self, conexion, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
    #     cursor = conexion.cursor()
    #     query = "INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) VALUES (%s, %s, %s, %s, %s, %s)"
    #     valores = (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
    #     cursor.execute(query, valores)
    #     conexion.commit()
    #     print(f"Revision creada correctamente")