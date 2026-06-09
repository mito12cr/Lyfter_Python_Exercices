#    Jaime Vanegas Villalobos
#    21/04/2026
#    Python Archivos CSV

# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación

import csv
FILE_PATH = 'games.csv'
VALID_RATINGS = {"T","B","H","M","O","V"}

def load_games_from_csv(file_path):
    try:
        games = []

        with open(file_path,mode='r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                games.append(row)
        return games

    except FileNotFoundError:
        print(f"ERROR: El Archivo: {file_path} , no se ha encontrado")
        return []
    except Exception as e:
        print(f"ERROR: Se ha presentado un inesperado: {e}") 
        return []   

def filter_games_by_ESRB(game_list,rating_to_find):
 return [
    game for game in game_list
    if game.get("Clasificación ESRB", "").strip().upper() == rating_to_find.upper()
]

def show_games_result(filtered_games,selected_rating):
    print(f"\n--- Resultados para ESRB: {selected_rating} ---")
    print("=" * 40)

    if not filtered_games:
        print("No se han encontrado juegos con esta clasificación!!")
        return
    for game in filtered_games:
        for column, value in game.items():
            print(f"{column:20}: {value}")
        print("-" * 40)
    print(f"Total Encontrados: {len(filtered_games)}")

def main():
    #cargamos la data:
    all_games = load_games_from_csv(FILE_PATH)
    if not all_games:
        return
    # Pedimos la calificacion al usuario:
    print(f"Calificaciones disponibles: {', '.join(VALID_RATINGS)}")
    esrb_option = input("Digite Únicamente una calificacion de la lista:").strip().upper()

    # Filtramos los datos:
    results = filter_games_by_ESRB(all_games,esrb_option)

    # Mostramos los datos:
    show_games_result(results,esrb_option)

if __name__ == "__main__":
    main()    








# def main():

# if __name__ == "__main__":
#    main()    