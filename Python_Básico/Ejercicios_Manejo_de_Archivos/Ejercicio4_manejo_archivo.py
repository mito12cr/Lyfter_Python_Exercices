#    Jaime Vanegas Villalobos
#    08/04/2026
#    Python Manejo de Archivos

# Cree un programa que:
# Lea un archivo línea por línea
# Convierta cada línea a mayúsculas
# Escriba el contenido en un nuevo archivo

def convert_to_upper_any_word(origin_file,destiny_file):
    try:
        with open(origin_file, 'r', encoding= 'utf-8') as file1:
           lines = file1.read()
           text_upper = lines.upper()

        with open(destiny_file, 'w', encoding= 'utf-8') as file2:
           result = file2.write(text_upper)  
        print("Archivo creado Exitosamente!!")    

    except FileNotFoundError:
     print(f"ERROR, El archivo '{origin_file}' no existe en el contexto actual!!")

convert_to_upper_any_word('Archivo_texto_ejercicio4.txt','Archivo_convertido_upper.txt' )