#    Jaime Vanegas Villalobos
#    20/04/2026
#    Python Archivos CSV

# Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea

import csv
FILE_PATH = 'games.csv'

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
    
def display_all_games(games_list):
    
    if not games_list:
        print("No hay juegos para mostrar!!")
        return
    
    print(f"\n--- LISTADO COMPLETO DE JUEGOS ({len(games_list)}) ---")
    print("=" * 40)

    for game in games_list:
        for column ,value in game.items():
            print(f"{column:20}: {value}")
        print("-" * 40)

def main():
    #obtenciòn de los datos:
    data = load_games_from_csv(FILE_PATH)

    #mostramos la data si hay datos:
    if data:
        display_all_games(data)

if __name__ == "__main__":
    main()        
        