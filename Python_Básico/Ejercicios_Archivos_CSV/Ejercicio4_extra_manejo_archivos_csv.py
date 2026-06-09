#    Jaime Vanegas Villalobos
#    21/04/2026
#    Python Archivos CSV

# Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible:

import csv

def get_games_by_company(file_path,company_name):

        games_found = []
        company_name = company_name.strip().lower()

        with open(file_path,mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("Desarrollador", "").strip().lower() == company_name:
                    games_found.append({
                        "name": row.get("Nombre", "N/A").strip(),
                        "rating": row.get("Clasificación ESRB", "N/A").strip(),
                        "genre": row.get("Género", "N/A").strip()
                    })
                    
        return games_found
    

def show_games_interface(file_path):
        
    print(" ")
    print("---- Programa para mostrar todos los videojuegos desarrollados por la misma empresa ----")
    print(" ")   

    company = input("Digite el nombre de la empresa de desarrollo de videojuegos (Ejemplo: Ubisoft)").strip().lower()

    try:
        results = get_games_by_company(file_path,company)

        if not results:
            print(f"No se encontraron juegos para: {company.title()}. ")    
            return
        
        print(f"\nVideojuegos desarrollados por: {company} ---")
        print("-" * 30) 

        for game in results:
            print(f" {game['name']} (Clasificación: {game['rating']}, Género: {game['genre']})")

    except FileNotFoundError:
        print("Error: El archivo no se encuentra o no existe!!")
    except Exception as e:
        print(f"Ha ocurrido un error de ejecución!! {e}")         


if __name__ == "__main__":
    show_games_interface('games.csv')          