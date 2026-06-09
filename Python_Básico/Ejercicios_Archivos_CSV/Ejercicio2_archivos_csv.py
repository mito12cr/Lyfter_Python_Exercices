#    Jaime Vanegas Villalobos
#    1/04/2026
#    Python Archivos CSV

#
import csv

def games_information_with_dictionary():

    fields = ["Nombre", "Genero", "Desarrollador","Clasificacion ESRB" ]

    game_list = []
    
    print("Registro de Video Juegos 2")

    while True:
        game = {}
        game["Nombre"] = input("\nNombre: ")
        game["Genero"] = input("Genero: ")
        game["Desarrollador"] = input("Desarrollador: ")
        game["Clasificacion ESRB"] = input("Clasificación : ")

        game_list.append(game)

        opcion = input("Desea guardar otro juego ? s/n: ").lower()
        if opcion != 's':
            break

    try:
        with open('Games.csv', 'w', newline='', encoding='utf-8') as file:
           writer = csv.DictWriter(file,fieldnames=fields, delimiter="\t") # de esta forma realizamos las tabulaciones "\t" 
           writer.writeheader()
           writer.writerows(game_list)

        print("Se ha creado con exito tu archivo CSV!!")    

        
    except Exception as e:
        print(f"Error: {e}")

games_information_with_dictionary()             