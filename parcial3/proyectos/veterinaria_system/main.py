import mysql.connector
from mysql.connector import Error
import os
from pacientes.paciente import *
from citas.cita import *
from sucursales.sucursal import *
from usuarios.usuario import *

def conexion_BD():
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            database='veterinaria',
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

def menu_usuarios(conexion):
    while True:
        os.system("cls")
        print("\n--- Menú de Usuarios ---")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")
            usuario = usuario(nombre, apellido, correo, contrasena)
            usuario.registrar(conexion)
        elif opcion == '2':
            correo = input("Indique su correo: ")
            contrasena = input("Indique su contraseña: ")
            if usuario.iniciar_sesion(conexion, correo, contrasena):
                print("Inicio de sesión exitoso.")
                menu_principal(conexion)
                break
            else:
                print("Error en el inicio de sesión. Verifique sus datos.")
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_principal(conexion):
    while True:
        os.system("cls")
        print("\n--- BIENVENIDO AL MENÚ PRINCIPAL ---")
        print("1. Pacientes")
        print("2. Citas")
        print("3. Sucursales")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            menu_pacientes(conexion)
        elif opcion == '2':
            menu_citas(conexion)
        elif opcion == '3':
            menu_sucursales(conexion)
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_pacientes(conexion):
    pacientes = Paciente()
    while True:
        os.system("cls")
        print("\n--- Menú de Pacientes ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_paciente = input("Indique el ID del paciente: ")
            nombre = input("Nombre del paciente: ")
            especie = input("Especie: ")
            raza = input("Raza: ")
            edad = input("Edad: ")
            pacientes = Paciente(id_paciente, nombre, especie, raza, edad)
            pacientes.Insertar(conexion)
        elif opcion == '2':
            pacientes.Consultar(conexion)
        elif opcion == '3':
            id_paciente = input("Indique el ID del paciente: ")
            nombre = input("Nuevo nombre: ")
            especie = input("Nueva especie: ")
            raza = input("Nueva raza: ")
            edad = input("Nueva edad: ")
            pacientes.Actualizar(conexion, id_paciente, nombre, especie, raza, edad)
        elif opcion == '4':
            id_paciente = input("Indique el ID del paciente a eliminar: ")
            pacientes.Eliminar(conexion, id_paciente)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_citas(conexion):
    citas = Cita()
    while True:
        os.system("cls")
        print("\n--- Menú de Citas ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_cita = input("Indique el ID de la cita: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            hora = input("Hora (HH:MM): ")
            paciente_id = input("ID del paciente: ")
            sucursal_id = input("ID de la sucursal: ")
            citas = Cita(id_cita, fecha, hora, paciente_id, sucursal_id)
            citas.Insertar(conexion)
        elif opcion == '2':
            citas.Consultar(conexion)
        elif opcion == '3':
            id_cita = input("Indique el ID de la cita: ")
            fecha = input("Nueva fecha (YYYY-MM-DD): ")
            hora = input("Nueva hora (HH:MM): ")
            paciente_id = input("Nuevo ID del paciente: ")
            sucursal_id = input("Nuevo ID de la sucursal: ")
            citas.Actualizar(conexion, id_cita, fecha, hora, paciente_id, sucursal_id)
        elif opcion == '4':
            id_cita = input("Indique el ID de la cita a eliminar: ")
            citas.Eliminar(conexion, id_cita)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_sucursales(conexion):
    sucursales = Sucursal()
    while True:
        os.system("cls")
        print("\n--- Menú de Sucursales ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_sucursal = input("Indique el ID de la sucursal: ")
            nombre = input("Nombre de la sucursal: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            sucursales = Sucursal(id_sucursal, nombre, direccion, telefono)
            sucursales.Insertar(conexion)
        elif opcion == '2':
            sucursales.Consultar(conexion)
        elif opcion == '3':
            id_sucursal = input("Indique el ID de la sucursal: ")
            nombre = input("Nuevo nombre: ")
            direccion = input("Nueva dirección: ")
            telefono = input("Nuevo teléfono: ")
            sucursales.Actualizar(conexion, id_sucursal, nombre, direccion, telefono)
        elif opcion == '4':
            id_sucursal = input("Indique el ID de la sucursal a eliminar: ")
            sucursales.Eliminar(conexion, id_sucursal)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    conexion = conexion_BD()
    if conexion:
        menu_usuarios(conexion)
    else:
        print("No se pudo establecer la conexión a la base de datos.")
