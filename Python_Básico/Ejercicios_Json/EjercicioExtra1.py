#    Jaime Vanegas Villalobos
#    19/05/2026
#    Python Archivos Json

# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1)y:
# Lea el archivo JSON de Pokémon
# Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

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

def format_pokemon_info(pokemon):
    name   = pokemon.get("name", "Desconocido")
    p_type = pokemon.get("type", "Desconocido")
    level  = pokemon.get("level", 0)
    skills = ", ".join(pokemon.get("skills", []))

    stats  = pokemon.get("stats", {})
    hp     = stats.get("hp", 0)
    attack = stats.get("attack", 0)

    info_block = (
        f"[{name.upper()}] (Tipo: {p_type} | Nivel: {level})\n"
        f" Estadísticas -> HP: {hp} | Ataque: {attack}\n"       # Estructura en consola
        f" Habilidades  -> {skills if skills else 'Ninguna'}\n" 
        f"{'-'*45}"
    )
    return info_block 

def display_pokemon_list(pokemon_list):
    if not pokemon_list:
        print("No se encontraron Pokémones registrados para mostrar!!!")
        return
    
    print("\n=============================================")
    print("         REPORTE ACTUAL DE POKÉMONES        ")
    print("=============================================\n")

    for any_pokemon in pokemon_list:
        text_to_print = format_pokemon_info(any_pokemon)
        print(text_to_print)

if __name__ == "__main__":
    pokemon_list = read_pokemon_json(FILE_PATH)

    display_pokemon_list(pokemon_list)        