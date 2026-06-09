#    Jaime Vanegas Villalobos
#    31/03/2026
#    Python Excepciones

# Pida al usuario su nombre:   Si el nombre es numérico (isdigit()), haga:
#  raise ValueError("El nombre no puede ser un número")

def print_names():

    name = input("Escriba su nombre aquí: ")
     
    try:
          if name.isdigit():
               raise ValueError("Error, El nombre no puede ser un número!! ")         

    except ValueError as e:
        print(e)
        return
    
    age_input = input("Digite su edad: ")
    try:        
        age = int(age_input)
        print(f"Hola {name}, su edad es {age}!!")  

    except ValueError:     
        print("ERROR: El número no es válido")

print_names()        