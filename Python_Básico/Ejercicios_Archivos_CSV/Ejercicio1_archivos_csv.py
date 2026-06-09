#    Jaime Vanegas Villalobos
#    14/04/2026
#    Python Archivos CSV

# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir: # Nombre # Género # Desarrollador # Clasificación ESRB

import csv

def games_information():

    game_list = [
        ["Nombre", "Género", "Desarrollador", "Clasificación ESRB"]
    ]

    print("Registro de Video Juegos")

    while True:
        nombre         = input("\nNombre: ")
        genero         = input("Género: ")
        desarrollador  = input("Desarrollador: ")
        clasificacion  = input("Clasificación: ")
        
        game_list.append([nombre,genero,desarrollador,clasificacion])

        opcion = input("Desea guardar otro juego?  s/n: ").lower()

        if opcion != 's':
            break

    try:
        with open('Games.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(game_list)
        print("Se ha creado con exito tu archivo CSV!!")    

    except Exception as e:
        print(f"Error: {e}")

games_information()             