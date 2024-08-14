import mysql.connector
from mysql.connector import Error

class Usuarios:
    def __init__(self, nombre=None, apellido=None, correo=None, contrasena=None):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena

    def registrar(self, conexion):
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO usuarios (nombre, apellido, correo, contrasena) VALUES (%s, %s, %s, %s)"
            values = (self.nombre, self.apellido, self.correo, self.contrasena)
            cursor.execute(query, values)
            conexion.commit()
            print("Usuario registrado exitosamente.")
        except Error as e:
            print(f"Error al registrar el usuario: {e}")

    @staticmethod
    def iniciar_sesion(conexion, correo, contrasena):
        try:
            cursor = conexion.cursor()
            query = "SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s"
            cursor.execute(query, (correo, contrasena))
            usuario = cursor.fetchone()
            if usuario:
                print(f"Bienvenido, {usuario[1]} {usuario[2]}!")
                return True
            else:
                print("Correo o contraseña incorrectos.")
                return False
        except Error as e:
            print(f"Error al iniciar sesión: {e}")
            return False

def conexion_BD():
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            database='agencia_autos',
            user='root',
            password='',
            port='3307'
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return None