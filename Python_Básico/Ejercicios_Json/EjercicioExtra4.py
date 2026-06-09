#    Jaime Vanegas Villalobos
#   27/05/2026
#    Python Archivos Json

# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON
# Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el promedio de nivel para cada tipo:

import json
FILE_PATH = 'pokemones.json'

def read_pokemon_json(file_pokemones):
    try:
        with open(file_pokemones,'r') as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"ERROR: El Archivo: {file_pokemones} , no se ha encontrado") 
        return []   # Si el archivo no existe, retornará una lista vacía para que el programa pueda crear el archivo con un primer pokémon
    except json.JSONDecodeError:
        print(f"ERROR: El archivo {file_pokemones} está vacío o tiene un formato inválido.") 
        return []   
    except Exception as e:
        print(f"ERROR: Se ha presentado un inesperado: {e}") 

def group_by_pokemon_type(pokemon_list):
    new_pokemons = {}

    for pokemon in pokemon_list:
        p_type = pokemon.get("type","Desconocido").strip().capitalize()

        if p_type not in new_pokemons: #si el tipo del pokemon no existe; creamos una lista vacia para postereormente agregar el pokemon que recorra nuestro for 
            new_pokemons[p_type]= []   # creo la lista vacia

        new_pokemons[p_type].append(pokemon) #agrego el nuevo pokemon a la lista vacia con el parametro 'pokemon'    
    return new_pokemons

def display_pokemon_list(pokemon_list):
    if not pokemon_list:
        print("No se encontraron Pokémones registrados para mostrar!!!")
        return
    
    print("\n=============================================")
    print("         REPORTE ACTUAL DE POKÉMONES POR TIPO       ")
    print("=============================================\n")

    for p_type, pokemons in pokemon_list.items():
        print(f"\n🔹 Tipo de Pokémon: {p_type} ({len(pokemons)} Registrados)")
        print("-" * 35)

        for pokemon in pokemons:
            name = pokemon.get("name", "Desconocido")
            level = pokemon.get("level", 0)
            print(f"  • {name} (Nivel: {level})")

    print("\n" + "=" * 35)

def display_average_reports(averages_dict):
    if not averages_dict:
        print(" No hay datos suficientes para calcular promedios.")
        return
        
    print("\n --- PROMEDIO DE NIVEL POR TIPO ---")
    print("=" * 40)
    
    for p_type, avg in averages_dict.items():
        print(f"* Tipo: {p_type} ➔  Promedio de nivel: {avg}")
        
    print("=" * 60)


def calculate_average_level_by_pokemon_type(grouped_pokemon):

    averages = {}

    for p_type, pokemons in grouped_pokemon.items():  
        if not pokemons:
            averages[p_type] = 0.0
            continue

        total_level_pokemon = sum(pokemon.get("level", 0) for pokemon in pokemons) 

        average = total_level_pokemon / len(pokemons)
        averages [p_type] = round(average,1)

    return averages    

if __name__ == "__main__":
    all_pokemons = read_pokemon_json(FILE_PATH)  # Leemos los datos del archivo json

    pokemons_by_type = group_by_pokemon_type(all_pokemons) # agrupamos por tipo los pokemones

    display_pokemon_list(pokemons_by_type)     

    type_averages = calculate_average_level_by_pokemon_type(pokemons_by_type)

    display_average_reports(type_averages)