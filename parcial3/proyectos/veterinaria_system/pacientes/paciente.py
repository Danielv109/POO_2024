from conexionbd import *


class Paciente:

    def __init__(self, id_paciente=None, nombre=None, especie=None, raza=None, edad=None, dueño_id=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueño_id = dueño_id

    def Insertar(self, conexion):
        cursor = conexion.cursor()
        query = "INSERT INTO pacientes (nombre, especie, raza, edad, dueño_id) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.nombre, self.especie, self.raza, self.edad, self.dueño_id)
        cursor.execute(query, valores)
        conexion.commit()
        print("Paciente registrado correctamente")

    @staticmethod
    def Consultar(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM pacientes"
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                print(f"id_paciente: {fila[0]}, nombre: {fila[1]}, especie: {fila[2]}, raza: {fila[3]}, edad: {fila[4]}, dueño_id: {fila[5]}")
        else:
            print("No se encontraron registros.")
        
        input("\nPresiona Enter para volver al menú principal...")

    @staticmethod
    def Actualizar(conexion, id_paciente, nombre, especie, raza, edad, dueño_id):
        cursor = conexion.cursor()
        query = "UPDATE pacientes SET nombre = %s, especie = %s, raza = %s, edad = %s, dueño_id = %s WHERE id_paciente = %s"
        valores = (nombre, especie, raza, edad, dueño_id, id_paciente)
        cursor.execute(query, valores)
        conexion.commit()
        print("Actualización hecha correctamente")

    @staticmethod
    def Eliminar(conexion, id_paciente):
        cursor = conexion.cursor()
        query = "DELETE FROM pacientes WHERE id_paciente = %s"
        cursor.execute(query, (id_paciente,))
        conexion.commit()
        print("Paciente eliminado correctamente")
