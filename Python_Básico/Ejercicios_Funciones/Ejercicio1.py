#    Jaime Vanegas Villalobos
#    20/03/2026
#    Python Funciones

# Creacion de una Funcion llamando a otra.
# Ejercicio 1 

def count_number() :
    my_list = [4, 2, 7, 2, 8, 2, 1]
    number_to_search = 2

    repeated_times = my_list.count(number_to_search)

    print(f"\nThe Number to find is: {number_to_search} and appears: {repeated_times} times!!")


def call_function():
    print("this is the second function who calls the firstone =D !!")
    count_number()

call_function()    


