#    Jaime Vanegas Villalobos
#    08/04/2026
#    Python Excepciones

# Cree un programa que lea un archivo con texto línea por línea,
#  quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

def read_text_in_line(origin_file,destiny_file):
    try:
        with open(origin_file,'r',encoding= 'utf-8') as entrance:
         lines = [letter.strip() for letter in entrance if letter.strip()]
         new_sentences= " ".join(lines)       

        with open(destiny_file,'w',encoding= 'utf-8') as exit1:           
           result = exit1.write(new_sentences)      
        print("Archivo creado Exitosamente!!")


    except FileNotFoundError:
     print("ERROR: no se ha podido encotrar el archivo de origen, verifique que exista!!")    

read_text_in_line('texto en python.txt','New Texto.txt')     