
import mysql.connector
from mysql.connector import Error
import os
from Revisiones.revisiones import *
from Autos.autos import *
from Clientes.clientes import *
from Usuarios.usuarios import *

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
            usuario = Usuarios(nombre, apellido, correo, contrasena)
            usuario.registrar(conexion)
        elif opcion == '2':
            correo = input("Indique su correo: ")
            contrasena = input("Indique su contraseña: ")
            if Usuarios.iniciar_sesion(conexion, correo, contrasena):
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
        print("\n--- BIENVENIDO AL MENU PRINCIPAL ---")
        print("1. Revisiones")
        print("2. Autos")
        print("3. Clientes")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            menu_revisiones(conexion)
        elif opcion == '2':
            menu_autos(conexion)
        elif opcion == '3':
            menu_clientes(conexion)
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_revisiones(conexion):
    revisiones = Revisiones()
    while True:
        os.system("cls")
        print("\n--- Menú de Revisiones ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            no_revision = input("Indique el numero de revision: ")
            cambiofiltro = input("Indique si es cambio de Filtro: ")
            cambioaceite = input("Indique si es cambio de Aceite: ") 
            cambiofrenos = input("Indique si es cambio de Frenos: ")
            otros = input("Indique si hubo alguna otra acción con su auto: ")
            matricula = input("Indique la matricula de su auto: ")
            revisiones = Revisiones(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
            revisiones.Insertar(conexion)
        elif opcion == '2':
            revisiones.Consultar(conexion)
        elif opcion == '3':
            no_revision = input("Nuevo Numero de revision: ")
            cambiofiltro = input("Se ha hecho Cambio de Filtro: ")
            cambioaceite = input("Se ha hecho Cambio de Aceite: ") 
            cambiofrenos = input("Se ha hecho Cambio de Frenos: ")
            otros = input("Se ha hecho Otra acción con su auto: ")
            matricula = input("Ingresar la Matricula de su auto: ")
            revisiones.Actualizar(conexion, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
        elif opcion == '4':
            no_revision = input("Escriba el no. de revision a eliminar: ")
            revisiones.Eliminar(conexion, no_revision)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_autos(conexion):
    autos = Autos()
    while True:
        os.system("cls")
        print("\n--- Menú de Autos ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            matricula = input("Indique la matricula del auto: ")
            marca = input("Indique la marca del auto: ")
            modelo = input("Indique el modelo del auto: ") 
            año = input("Indique el año del auto: ")
            color = input("Indique el color del auto: ")
            autos = Autos(matricula, marca, modelo, año, color)
            autos.Insertar(conexion)
        elif opcion == '2':
            autos.Consultar(conexion)
        elif opcion == '3':
            matricula = input("Indique la matricula del auto a actualizar: ")
            marca = input("Indique la nueva marca del auto: ")
            modelo = input("Indique el nuevo modelo del auto: ") 
            año = input("Indique el nuevo año del auto: ")
            color = input("Indique el nuevo color del auto: ")
            autos.Actualizar(conexion, matricula, marca, modelo, año, color)
        elif opcion == '4':
            matricula = input("Escriba la matricula del auto a eliminar: ")
            autos.Eliminar(conexion, matricula)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_clientes(conexion):
    while True:
        os.system("cls")
        print("\n--- Menú de Clientes ---")
        print("1. Insertar Cliente")
        print("2. Consultar Clientes")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Regresar al Menú Principal")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_cliente = input("Indique el ID del cliente: ")
            nombre = input("Indique el nombre del cliente: ")
            direccion = input("Indique la dirección del cliente: ")
            telefono = input("Indique el teléfono del cliente: ")
            email = input("Indique el email del cliente: ")
            cliente = Clientes(id_cliente, nombre, direccion, telefono, email)
            cliente.Insertar(conexion)
        elif opcion == '2':
            Clientes.Consultar(conexion)
        elif opcion == '3':
            id_cliente = input("Ingrese el ID del cliente que desea actualizar: ")
            nombre = input("Nuevo nombre del cliente: ")
            direccion = input("Nueva dirección del cliente: ")
            telefono = input("Nuevo teléfono del cliente: ")
            email = input("Nuevo email del cliente: ")
            Clientes.Actualizar(conexion, id_cliente, nombre, direccion, telefono, email)
        elif opcion == '4':
            id_cliente = input("Ingrese el ID del cliente que desea eliminar: ")
            Clientes.Eliminar(conexion, id_cliente)
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
