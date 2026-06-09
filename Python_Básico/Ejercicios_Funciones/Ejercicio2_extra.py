#    Jaime Vanegas Villalobos
#    25/03/2026
#    Python Funciones

# Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
# Ejercicio 2

def return_new_list(my_list,my_number):
    my_new_list = []  
    for my_word in my_list:        
        if len(my_word) > my_number:             
            my_new_list.append(my_word)
    return my_new_list    

words = ["cielo", "sol", "maravilloso", "día"]

number_of_letters = int(input(f"Ingrese el numero de letras minimas en la palabra: ")) 

result = return_new_list(words, number_of_letters)

print(f"salida: {result}" )

