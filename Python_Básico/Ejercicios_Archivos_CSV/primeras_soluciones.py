#    Jaime Vanegas Villalobos
#    04/05/2026
#    Python Archivos CSV

# Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea
import csv

def show_games_information(games):
    try:
        with open(games, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader :
                for column, value in row.items(): #con el metodo 'items()' python me entrega la clave y el valor 
                    print(f"{column}: {value}") # De esta manera se mostrará la informacion: la colunma o key (column) y su valor (value)
                print("-" * 30)     #Con esta linea de codigo separo cada bloque de cada juego del archivo

    except FileNotFoundError:
        print("Error: El archivo no se encuentra o no existe!!")
    except Exception as e:
        print("Ha ocurrido un error de ejecución!!")

show_games_information('games.csv')            

#---------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 3

# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada


def count_total_games_per_gender(games):
    print(" ")
    print("---- Programa para contar el total de videojuegos por cada Género ----")
    print(" ")

    gender_count = {} # en este diccionario vacío guardaremos los datos

    try:
        with open(games, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                gender = row.get('Género', 'Sin Género').strip().capitalize() #Usamos la funcion capitalize para no tener problemas con mayusculas y minusculas
                if gender in gender_count: # Si el género ya existe sumamos 1 
                    gender_count[gender] += 1
                else:
                    gender_count[gender] = 1 # Si no existe y es nuevo agregamos 1 al diccionario

        print("---- Detalle de cada Género ---- ")
        for gender, total in gender_count.items():  # Recorremos el nuevo diccionario 'gender_count'
            print(f" {gender} : {total}")        # Y damos el formato que deseamos en este caso Género y el Total

        print("---- Total por Género ----")
        print(f"Total General: {sum(gender_count.values())} Videojuegos")     # con la funcion 'sum()' sumamos el total de todos los juegos que se agregaron al diccionario nuevo       

    except FileNotFoundError:
        print("Error: El archivo no se encuentra o no existe!!")
    except Exception as e:
        print("Ha ocurrido un error de ejecución!!")

count_total_games_per_gender('games.csv')        

#-----------------------------------------------------------------------------------------------------------------------------
# EJERCICIO 4

# Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible:


def show_games_developed_bythe_company(games):

    print(" ")
    print("---- Programa para mostrar todos los videojuegos desarrollados por la misma empresa ----")
    print(" ")

    company = input("Digite el nombre de la empresa de desarrollo de videojuegos (Ejemplo: Ubisoft)").strip().lower()

    try:
        with open(games, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)           
            print(f"\nVideojuegos desarrollados por: {company} ---")
            print("-" * 30) 
            found_it = False
        
            for row in reader:
                current_company = row.get("Desarrollador", "").strip().lower()

                if current_company == company:
                    name   = row.get("Nombre", "N/A").strip()
                    rating = row.get("Clasificación ESRB", "N/A").strip()
                    genre  = row.get("Género", "N/A").strip()
                    print(f" {name} (Clasificación: {rating}, Género: {genre})")
                    found_it = True 

            if not found_it:
                print(f"No se encontraron juegos para: {company.title()}. ")                      


    except FileNotFoundError:
        print("Error: El archivo no se encuentra o no existe!!")
    except Exception as e:
        print(f"Ha ocurrido un error de ejecución!! {e}")

show_games_developed_bythe_company('games.csv')      