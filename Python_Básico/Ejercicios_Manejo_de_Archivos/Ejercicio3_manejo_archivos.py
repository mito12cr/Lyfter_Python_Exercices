#    Jaime Vanegas Villalobos
#    08/04/2026
#    Python Manejo de Archivos

# Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
# (Considere que las palabras están separadas por espacios y/o saltos de línea)

def count_words(origin_file):
    try:
         with open(origin_file,'r',encoding= 'utf-8') as file:
            text = file.read() #leemos el archivo
            words = text.split() #se dividirá en una lista de palabras

            result = len(words) #aca vamos a contar los elementos de esa lista de palabras.
            print(f"Este archivo contiene: {result} palabras")


    except FileNotFoundError:
        print(f"ERROR, El archivo '{origin_file}' no existe en el contexto actual!!")

    except Exception as e:
        print(f"Ocurrió un error inesperado en el sistema!!")    

count_words('Archivo_texto_ejercicio3.txt')