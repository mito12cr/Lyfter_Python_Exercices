#    Jaime Vanegas Villalobos
#    08/04/2026
#    Python Manejo de Archivos

# Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente


def new_line_in_current_file():
    
    new_file = 'Nuevo_archivo_texto5.txt'
    new_line = input("Digite su nuevo Texto Aquí: ")

    try:   
        with open(new_file, 'a', encoding= 'utf-8') as file1:
            file1.write(new_line + "\n" )
        print(f"Se agregó correctamente la linea nueva en el archivo: {new_file}")    

    except Exception as e:
        print(f"Ocurrió un error inesperado en el sistema!!")    

new_line_in_current_file()            