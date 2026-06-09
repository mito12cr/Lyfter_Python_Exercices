#    Jaime Vanegas Villalobos
#    19/05/2026
#    Python Archivos Json

# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
# Lea el archivo JSON de Pokémon
# Pida al usuario un tipo de Pokémon
# Muestre todos los Pokémon que sean de ese tipo


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

def show_filtered_results(filtered_pokemons, pokemon_type):
    print(f"Estos son los Pokémones disponibles con respecto a su tipo '{pokemon_type.capitalize()}' son los siguientes:  ")
    print("-" * 40)

    if not filtered_pokemons:
        print(f"No se encontraron Pokémones en la base de datos de el tipo: '{pokemon_type}'")
        return
    
    for pokemon in filtered_pokemons:
        name  = pokemon.get("name", "Desconocido")
        level = pokemon.get("level", 0)
        print(f" {name} (Nivel {level})")
    print("-" * 40)  

def filtered_pokemon_by_type(pokemon_list, pokemon_type):
    target_type_clean = pokemon_type.strip().lower()  #guardamos en esta variable lo que el usuario escriba cuando le pidamos el tipo de pokemon, formateando para no tener errores

    filtered_list = [
        pokemon for pokemon in pokemon_list  # Recorremos la lista de pokemones 
        if pokemon.get("type", "").strip().lower() == target_type_clean  # comparamos cada pokemon que encuentre en la lista con el digitado por el usuario mediante su "type"
    ]                                                                    # y lo guardará en la variable filtered_list si es "true"
    return filtered_list

def request_type():
    print("----- Búsqueda de Pokémon por tipo: -----")
    type_result = input("Ingrese el tipo de Pokémon que desea buscar (Electric, Fire, Grass, etc.): ")
    
    return type_result

if __name__ == "__main__":
    pokemons = read_pokemon_json(FILE_PATH)

    if pokemons:
        selected_type = request_type()  # guardamos el resultado de lo que escriba el usuario en la variable selected_type para utilizarla  en las proximas funciones

        matches = filtered_pokemon_by_type(pokemons,selected_type) 

        show_filtered_results(matches,selected_type)

        