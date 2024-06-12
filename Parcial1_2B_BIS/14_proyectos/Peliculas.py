import Archivo_peliculas_calculadora

def menu_peliculas():
    print("\t...::BIENVENIDO!::...\n")
    peliculas = [
        "El Padrino",
        "Matrix",
        "Crepúsculo",
        "Piratas del Caribe",
        "Harry Potter",
    ]

    while True:
        print("\nMenu de Opciones: ")
        print("1.- Agregar peliculas\n2.- Remover peliculas\n3.- Consultar peliculas\n4.- Buscar pelicula\n5.- Vaciar lista\n6.- Actualizar pelicula\n7.- Salir")
        opcion = input("¿Qué deseas hacer? \n")

        if opcion == "1":
            Archivo_peliculas_calculadora.agregar_pelicula(peliculas)
        elif opcion == "2":
            Archivo_peliculas_calculadora.remover_pelicula(peliculas)
        elif opcion == "3":
            Archivo_peliculas_calculadora.consultar_pelicula(peliculas)
        elif opcion == "4":
            Archivo_peliculas_calculadora.buscar_pelicula(peliculas)
        elif opcion == "5":
            Archivo_peliculas_calculadora.vaciar_lista(peliculas)
        elif opcion == "6":
            Archivo_peliculas_calculadora.actualizar_pelicula(peliculas)
        elif opcion == "7":
            print("Gracias por usar el gestor de películas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

        input("Presiona Enter para continuar...")

menu_peliculas()


