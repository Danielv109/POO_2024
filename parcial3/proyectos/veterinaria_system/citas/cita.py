from conexionbd import *

class Cita:

    def __init__(self, id_cita=None, fecha=None, hora=None, motivo=None, paciente_id=None, sucursal_id=None):
        self.id_cita = id_cita
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.paciente_id = paciente_id
        self.sucursal_id = sucursal_id

    def Insertar(self, conexion):
        cursor = conexion.cursor()
        query = "INSERT INTO citas (fecha, hora, motivo, paciente_id, sucursal_id) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.fecha, self.hora, self.motivo, self.paciente_id, self.sucursal_id)
        cursor.execute(query, valores)
        conexion.commit()
        print("Cita creada correctamente")

    @staticmethod
    def Consultar(conexion):
        cursor = conexion.cursor()
        query = "SELECT * FROM citas"
        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                print(f"id_cita: {fila[0]}, fecha: {fila[1]}, hora: {fila[2]}, motivo: {fila[3]}, paciente_id: {fila[4]}, sucursal_id: {fila[5]}")
        else:
            print("No se encontraron registros.")
        
        input("\nPresiona Enter para volver al menú principal...")

    @staticmethod
    def Actualizar(conexion, id_cita, fecha, hora, motivo, paciente_id, sucursal_id):
        cursor = conexion.cursor()
        query = "UPDATE citas SET fecha = %s, hora = %s, motivo = %s, paciente_id = %s, sucursal_id = %s WHERE id_cita = %s"
        valores = (fecha, hora, motivo, paciente_id, sucursal_id, id_cita)
        cursor.execute(query, valores)
        conexion.commit()
        print("Actualización hecha correctamente")

    @staticmethod
    def Eliminar(conexion, id_cita):
        cursor = conexion.cursor()
        query = "DELETE FROM citas WHERE id_cita = %s"
        cursor.execute(query, (id_cita,))
        conexion.commit()
        print("Cita eliminada correctamente")
