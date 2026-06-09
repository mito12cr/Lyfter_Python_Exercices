#    Jaime Vanegas Villalobos
#    25/03/2026
#    Python Funciones

# Cree una función que reciba un string y retorne cuántas vocales contiene

def return_vocals(my_string):
    text = my_string.lower()

    return sum(text.count(vocals) for vocals in 'aeiou')
result = return_vocals("Hola mundo te estoy saludando")

# Segundo ejemplo digitando nosotros mismos las palabras o texto a calcular
def return_vocals2(my_string):
    text = my_string.lower()

    return sum(text.count(vocals) for vocals in "aeiou")
text = input("Escriba las palabras u oracion para conocer el total de vocales que contienen: ")
result = return_vocals2(text)
print(result)
