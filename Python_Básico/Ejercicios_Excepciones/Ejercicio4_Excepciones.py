#    Jaime Vanegas Villalobos
#    03/04/2026
#    Python Excepciones

# Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total

def sumar_valores(lista):
    total = 0.0


    for i in lista:
        try:
            item = float(i)
            total += item
            print(f"{item} sumado correctamente")

        except ValueError as ex:
            print(f"Elemento inválido: {i}")    

    print(f"Total de la suma: {total}")


    return lista

my_list = ['10', 'manzana', '5.5', '3', 'n/a']
sumar_valores(my_list)
