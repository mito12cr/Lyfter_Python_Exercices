#    Jaime Vanegas Villalobos
#    21/04/2026
#    Python Archivos CSV

# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada
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
    
def calculate_gender_statistics(games_list):
    gender_count = {}
    for row in games_list:
        gender = row.get('Género', 'Sin Género').strip().capitalize() #Usamos la funcion capitalize para no tener problemas con mayusculas y minusculas
        
        if gender in gender_count: # Si el género ya existe sumamos 1 
            gender_count[gender] += 1
        else:
            gender_count[gender] = 1 # Si no existe y es nuevo agregamos 1 al diccionario
    return gender_count    

def show_gender_report(gender_stats):

    if not gender_stats:
        print("No hay juegos para mostrar!!")
        return
    
    print("\n" + "-" * 40)
    print("  DETALLE DE VIDEOJUEGOS POR GÉNERO")
    print("-" * 40)

    for gender in sorted(gender_stats.keys()):
        total = gender_stats[gender]
        print(f" {gender:20}: {total} juegos")

    print("-" * 40)
    total_general = sum(gender_stats.values())
    print(f"Total general: {total_general} Videojuegos")
    print("-" * 40)

def main():
    #obtenemos los datos
    data = load_games_from_csv(FILE_PATH)

    if data:
        stats = calculate_gender_statistics(data)

        show_gender_report(stats)

if __name__ == "__main__":
    main()                
