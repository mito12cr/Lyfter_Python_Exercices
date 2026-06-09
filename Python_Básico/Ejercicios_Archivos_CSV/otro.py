import csv

def show_games_information(games):
    try:
        with open(games, mode='r', encoding='utf-8') as file:
            # El secreto está en delimiter='\t'
            reader = csv.DictReader(file, delimiter='\t')

            for row in reader:
                # Verificamos que la fila no esté vacía
                if any(row.values()):
                    for column, value in row.items():
                        # .strip() limpia espacios o saltos de línea sobrantes
                        print(f"{column.strip()}: {value.strip()}")
                    print("-" * 20)

    except FileNotFoundError:
        print("Error: El archivo no se encuentra!!")
    except Exception as e:
        print(f"Error de ejecución: {e}")

show_games_information('games.csv')

import csv

def filter_games_by_ESRB(games):
    print("--- FILTRO DE CLASIFICACIÓN ESRB ---")
    print("--- Opciones Disponibles: T, B, M, O, V ---")

    esrb_option = input("Digite únicamente una calificación de la lista: ").strip().upper()

    try:
        with open(games, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            find_it = False
            print(f"\nResultados para la clasificación: {esrb_option}")
            print("=" * 30)

            for row in reader:
                # Obtenemos el rating y lo limpiamos
                rating = row.get("Clasificación ESRB", '').strip().upper()
                
                # Comparamos el rating del archivo con la opción del usuario
                match rating:
                    case _ if rating == esrb_option and rating in ["T", "B", "M", "O", "V"]:
                        for column, value in row.items():
                            print(f"{column}: {value}")
                        # El separador va AQUÍ (fuera del for de columnas)
                        print("=" * 30) 
                        find_it = True    
            
            if not find_it:
                print("No se han encontrado juegos con la clasificación seleccionada!!")

    except FileNotFoundError:
        print("Error: El archivo no existe en el contexto actual!!")            
    except Exception as e:
        # Añadí una 'f' antes de las comillas para que el error {e} sea visible
        print(f"Error: Ha ocurrido un error de ejecución!! {e}")    

# IMPORTANTE: El nombre del archivo debe ir entre comillas
filter_games_by_ESRB('games.csv')
