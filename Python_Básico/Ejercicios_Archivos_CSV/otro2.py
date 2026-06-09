    #    Jaime Vanegas Villalobos
#    21/04/2026
#    Python Archivos CSV

# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación

import csv

def filter_games_by_ESRB(games):

    print("--- FILTRO DE CLASIFICACIÓN ESRB ---")
    print("--- Opciones Disponibles: T, B, M, O, V ---")
    
    esrb_option = input("Digite Únicamente una calificacion de la lista:").strip().upper() #Importante quitar los espacios en blanco y convertir la letra selecciona siempre a Mayuscula

    try:
            read_and_return_rows(games)
            find_it = False
            print(f"\nResultados para la clasificación: {esrb_option}")
            print("=" * 30)

            for row in reader :
                rating = row.get("Clasificación ESRB", '').strip() #Quitamos espacios en blanco con .strip()                
                match rating:
                    case _ if rating == esrb_option and rating in ["T", "B", "M", "O", "V"]:        
                        for column,value in row.items(): #Mostramos los datos recorriendo los juegos existentes
                            print(f"{column}: {value}")     
                        print("=" * 30)
                        find_it = True    
            if not find_it:
                print("No se han encontrado juegos con la clasificación seleccionada!!")
    except FileNotFoundError:
        print("Error, El archivo no existe en el contexto actual!!")            
    except Exception as e:
        print(f"Error,Ha ocurrido un error de ejecución!! {e}")    

filter_games_by_ESRB('games.csv')     

def read_and_return_rows(games):
    with open(games, mode='r',encoding='utf-8') as file:
     reader = csv.DictReader(file)


#----------------------------------------------------------------------------------------------------------------------------------------#
# 
# import csv

# Configuration
FILE_PATH = 'games.csv'
VALID_RATINGS = {"T", "B", "M", "O", "V"}

def load_games_from_csv(file_path):
    """Responsibility: Read the file and return a list of dictionaries."""
    games = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                games.append(row)
        return games
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Unexpected error loading file: {e}")
        return []

def filter_by_esrb(games_list, rating_to_find):
    """Responsibility: Pure logic. Filters the list based on a criteria."""
    # We clean the input once here
    target = rating_to_find.strip().upper()
    
    return [
        game for game in games_list 
        if game.get("Clasificación ESRB", "").strip().upper() == target
    ]

def display_game_results(filtered_games, selected_rating):
    """Responsibility: User Interface. Formats and prints the data."""
    print(f"\n--- Results for ESRB: {selected_rating} ---")
    print("=" * 40)
    
    if not filtered_games:
        print("No games found for this classification.")
        return

    for game in filtered_games:
        for key, value in game.items():
            print(f"{key:20}: {value}")
        print("-" * 40)
    
    print(f"Total found: {len(filtered_games)}")

def main():
    """Responsibility: Coordination of the workflow."""
    # 1. Load data
    all_games = load_games_from_csv(FILE_PATH)
    if not all_games:
        return

    # 2. Get User Input
    print(f"Available Ratings: {', '.join(VALID_RATINGS)}")
    choice = input("Select a rating: ").strip().upper()

    # 3. Filter data
    results = filter_by_esrb(all_games, choice)

    # 4. Display data
    display_game_results(results, choice)

if __name__ == "__main__":
    main()