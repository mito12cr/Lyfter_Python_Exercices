#    Jaime Vanegas Villalobos
#    26/05/2026
#    Python Archivos Json

# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)


import json
FILE_PATH = 'pokemones.json'

def read_pokemon_json(file_pokemon): # Con esta funcion al igual que en el ejercicio pasado leemos los datos de nuestro JSON
    try:
        with open(file_pokemon,'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        print(f"ERROR: El Archivo: {file_pokemon} , no se ha encontrado") 
        return []   # Si el archivo no existe, retornará una lista vacía para que el programa pueda crear el archivo con un primer pokémon
    except json.JSONDecodeError:
        print(f"ERROR: El archivo {file_pokemon} está vacío o tiene un formato inválido.") 
        return []   
    except Exception as e:
        print(f"ERROR: Se ha presentado un inesperado: {e}") 

def format_pokemon_stats(pokemon):    
    stats = pokemon.get("stats", {})

    name        = pokemon.get("name", "Desconocido")
    hp          = stats.get("hp", 0)
    attack      = stats.get("attack", 0)
    defense     = stats.get("defense", 0)
    sp_attack   = stats.get("sp_attack", 0)
    sp_defense  = stats.get("sp_defense", 0)
    speed       = stats.get("speed", 0)

    stats_block = (
        f"Nombre:           {name} \n"
        f"HP:               {hp} \n"
        f"Ataque:           {attack} \n"
        f"Defensa:          {defense} \n"
        f"Ataque Especial:  {sp_attack} \n"
        f"Defensa Especial: {sp_defense} \n"
        f"Velocidad:        {speed} \n"
    )    
    return stats_block

def display_stats(pokemon_list):
    if not pokemon_list:
        print(f"No se encontraron Pokémones en la base de datos para mostrar estadisticas!!")
        return
    print("\n=============================================")
    print("         REPORTE DE LAS ESTADÍSTICAS DEL POKÉMON       ")
    print("=============================================\n")

    for pokemon in pokemon_list:
        text_print = format_pokemon_stats(pokemon)
        print(text_print)

if __name__ =="__main__":
    all_pokemons = read_pokemon_json(FILE_PATH)       

    display_stats(all_pokemons) 