def agregar_pelicula(peliculas):
    nueva_pelicula = input("Introduce el nombre de la nueva película: ")
    peliculas.append(nueva_pelicula)
    print("La pelicula ", nueva_pelicula, "ha sido agregada.")

def remover_pelicula(peliculas):
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}.-{pelicula}")
    num_pelicula = int(input("Introduce el número de la película que deseas remover: ")) - 1
    if 0 <= num_pelicula < len(peliculas):
        removida = peliculas.pop(num_pelicula)
        print(f"La película '{removida}' ha sido removida.")
    else:
        print("Número inválido.")

def consultar_pelicula(peliculas):
    print("Películas disponibles:")
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}.-{pelicula}")
    