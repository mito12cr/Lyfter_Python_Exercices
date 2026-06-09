#    Jaime Vanegas Villalobos
#    06/04/2026
#    Python Excepciones

# Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_songs_and_write_in_new_file(origen_file, destiny_file):
    try:
      with open(origen_file,'r', encoding = 'utf-8') as file: #Leemos el archivo con el modo 'r' de "read" donde se encuentran las canciones con el formato utf-8
         songs = [line.strip() for line in file if line.strip()]
      songs.sort() # metodo sort() para ordenar alfabeticamente

      with open(destiny_file, 'w', encoding='utf-8') as file: # Escribimos en el archivo que será nuestro destino con el modo 'w' de write con el formato utf-8 nuevamente
        for song in songs : #Recorremos la lista con las canciones
           file.write(f"{song}\n") #Escribimos linea por linea las canciones en el nuevo archivo
      print(f"Se han guardado una cantidad de: {len(songs)} canciones en '{destiny_file}'.")

       
    except FileNotFoundError: 
       print("ERROR, no se logró encontrar el archivo de destino") #En caso de no encotrar el archivo de destino desplegamos la excepcion FileNotFoundError


read_songs_and_write_in_new_file('canciones.txt', 'canciones_ordenadas.txt') #pasamos el nombre del archivo origen y el nombre del nuevo archivo donde se guardaran nuestras canciones.     
