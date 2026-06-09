#    Jaime Vanegas Villalobos
#    13/05/2026
#    Python Archivos Json

# Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON (ipsum:lesson/python-bsico/manejo-de-json)
# Debe leer el archivo para importar los Pokémones existentes.
# Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

# Para convertir de Json a python utilizamos el metodo 'loads()'
# Para convertir de Python a Json utilizamos el metodo dumps()
import json
FILE_PATH = 'pokemones.json'

def read_pokemon_json(file_pokemon):
    try:
        with open(file_pokemon,'r') as file: #Primeramente leemos el archivo
            return json.load(file)   

    except FileNotFoundError:
        print(f"ERROR: El Archivo: {file_pokemon} , no se ha encontrado") 
        return []   # Si el archivo no existe, retornará una lista vacía para que el programa pueda crear el archivo con un primer pokémon
    except json.JSONDecodeError:
        print(f"ERROR: El archivo {file_pokemon} está vacío o tiene un formato inválido.") 
        return []   
    except Exception as e:
        print(f"ERROR: Se ha presentado un inesperado: {e}") 
                
def add_new_pokemon(file_pokemon,new_pokemon):
    data = read_pokemon_json(file_pokemon) #leemos los datos actuales

    if data is None: 
        print("No se ha podido realizar la peticion por una inconsistencia en la lectura del archivo!!") # si el archivo esta vacio vamos a tener una lista vacia para ir llenandola de la data
        return 

    data.append(new_pokemon)    #agregamos el nuevo pokemon a esa lista vacia

    try:
        with open(file_pokemon,'w') as file:
            json.dump(data,file,indent= 4 ) # transferimos y formateamos los datos de la memoria de python a nuestro disco duro (traduce al formato JSON), luego lo transferimos a la variable 'file' de mi archivo fisico real previamente abierto.
        print(f"{new_pokemon['name']} agregado correctamente!!")
    except Exception as e:
        print(f"No se pudo guardar correctamente: {e}")

def request_pokemon_info():
    print("\n --Registro de un nuevo Pokémon--")

    name         = input("Nombre: ").strip().capitalize()
    p_type       = input("Tipo: ").strip().capitalize()
    level        = int(input("Nivel: "))
    weight       = float(input("Peso: "))      
    shiny_input  = input("Es Shiny? (s/n): ").strip().lower()
    is_shiny     = True if shiny_input == 's' else False
    item_input   = input("Objeto sostenido, Presiona Enter si éste pokemon no tiene: ").strip()
    held_item    = item_input if item_input != "" else None
    skills_input = input("Habilidades: (Escríbelas y separalas por comas(,))")
    skills       = [skill.strip().title()for skill in skills_input.split(",") if skill.strip() ]

    print("-- Estadisticas del Pokémon --")

    hp = int(input("HP: "))
    attack = int(input("Ataque: "))
    defense = int(input("Defensa: "))
    sp_attack = int(input("Ataque Especial: "))
    sp_defense = int(input("Defensa Especial: "))
    speed = int(input("Velocidad: "))

    pokemon_structure = {  # Estructura segun el JSON
        "name": name,
        "type": p_type,
        "level": level,
        "weight_kg": weight,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed
        }
    }

    return pokemon_structure

if __name__ == "__main__":
    new_pokemon = request_pokemon_info() #mostramos primeramente el solicitar la info del nuevo pokémon:

    add_new_pokemon(FILE_PATH, new_pokemon) # por ultimo guardamos nuestro registro de el nuevo pokémon



        
                
