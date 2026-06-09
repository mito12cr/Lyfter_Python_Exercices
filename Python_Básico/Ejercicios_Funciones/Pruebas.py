#    Jaime Vanegas Villalobos
#    20/03/2026
#    Python Funciones

# Pruebas de funciones.
# Ejercicio 

def print_parameters(parameter_1,parameter_2,parameter_3):
    print(f"This is the parameter 1: {parameter_1}")
    print(f"This is the parameter 2: {parameter_2}")
    print(f"This is the parameter 3: {parameter_3}")

print_parameters("Jaime Felipe", 12, "Vanegas Villalobos")


def get_max_of_the_numbers(number1,number2,number3,number4,number5):
    if number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5:
        print((f"\nEl numero 1  {number1} Es el número Mayor "))
    elif number2 > number1 and number2 > number3 and number2 > number4 and number2 > number5:
        print((f"\nEl numero 2  {number2} Es el número Mayor "))    
    elif number3 > number1 and number3 > number2 and number3 > number4 and number3 > number5:
        print((f"\nEl numero 3 {number3} Es el número Mayor "))    
    elif number4 > number1 and number4 > number2 and number4 > number3 and number4 > number5:
        print((f"\nEl numero 4  {number4} Es el número Mayor "))    
    elif number5 > number1 and number5 > number2 and number5 > number3 and number5 > number4:
        print((f"\nEl numero 5  {number5} Es el número Mayor "))    


get_max_of_the_numbers(5000,4000,1000,8000,10000)        

print("  ")

#--------------------------------------------------------------------------------------------------------------------------------------
def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
juan_scores = {
  "spanish_score": 75,
	"science_score": 95,
  "history_score": 54,
}
sofia_scores = {
  "spanish_score": 64,
	"science_score": 56,
  "history_score": 98,
}
paul_scores = {
  "spanish_score": 72,
	"science_score": 75,
  "history_score": 79,
}

# Averages
juan_scores["average_score"] = get_average_score(juan_scores)
sofia_scores["average_score"] = get_average_score(sofia_scores)
paul_scores["average_score"] = get_average_score(paul_scores)

juan_scores["is_exempted"] = is_student_exempted(juan_scores)
sofia_scores["is_exempted"] = is_student_exempted(sofia_scores)
paul_scores["is_exempted"] = is_student_exempted(paul_scores)

get_average_score(juan_scores)
get_average_score(sofia_scores)
get_average_score(paul_scores)

#-----------------------------------------------------------------------------------------------------------------------------------------


def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
students = [
  {
    "name": "Juan",
		"spanish_score": 75,
		"science_score": 95,
		"history_score": 54,
	},
  {
    "name": "Sofia",
		"spanish_score": 64,
		"science_score": 56,
		"history_score": 98,
	},
  {
    "name": "Paul",
		"spanish_score": 72,
		"science_score": 75,
		"history_score": 79,
	}
]

# Averages
for student in students:
  student["average_score"] = get_average_score(student)
  student["is_exempted"] = is_student_exempted(student)
  print(student["name"], " is_exempted is ", student["is_exempted"])



def contar_mayusculas_minusculas(texto):
    mayusculas = 0
    minusculas = 0
    
    for caracter in texto:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1
            
    print(f"There’s {mayusculas} upper cases and {minusculas} lower cases")

# Ejemplo:
contar_mayusculas_minusculas("I love Nación Sushi")

print(" ")

def numeros_primos(num):
   if num < 2:
      return False
   for i in range(2,int(num**0.5) + 1):
      if num % i == 0:
         return False
   return True


def retorno_lista_numeros_primos(my_list):
   nueva_lista = []

   for primo in my_list:
      if numeros_primos(primo):
         nueva_lista.append(primo)
   return nueva_lista

lista_de_numeros =  [1, 4, 6, 7, 13, 9, 67]      

resultado = retorno_lista_numeros_primos(lista_de_numeros)

print(resultado)

print(" ")
print(" ")


def contar_caracter(texto, caracter):
    # El método .count() hace todo el trabajo por nosotros
    cantidad = texto.count(caracter)
    return cantidad

# --- Ejemplo de uso e interacción ---
texto_usuario = "programacion"
busqueda = input("Ingrese el carácter que desea buscar: ")

resultado = contar_caracter(texto_usuario, busqueda)

print(f"Se ha encontrado {resultado} veces el carácter")


print(" ")
print(" ")


def filtrar_por_largo(lista_palabras, n):
    resultado = []
    for palabra in lista_palabras:
        # Verificamos si el largo de la palabra es mayor a n
        if len(palabra) > n:
            resultado.append(palabra)
    return resultado

# --- Ejemplo de uso e interacción ---
palabras = ["cielo", "sol", "maravilloso", "día"]

# Pedimos al usuario el número mínimo de letras
entrada_n = int(input("Ingrese el número de letras mínimas en la palabra: "))

# Llamamos a la función y mostramos el resultado
salida = filtrar_por_largo(palabras, entrada_n)
print(f"Salida: {salida}")
