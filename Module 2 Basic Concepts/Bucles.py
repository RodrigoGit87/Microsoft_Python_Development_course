import random

#FOR
# Un bucle for itera sobre una secuencia, como una lista, tupla o cadena, ejecutando un bloque de código por cada 
# elemento de la secuencia. Esto resulta especialmente útil cuando se trabaja con colecciones de datos 
# o cuando se conoce de antemano el número de iteraciones.
for i in range(0,10):
    print("iteration:",i)
#ITERACIONES POSIBLES EN FOR
# range(stop): Genera una secuencia de números empezando por 0 (por defecto) hasta, pero sin incluir, el valor stop, incrementándose en 1 cada vez.
# Así, range(5) haría un bucle del 0 al 4. -- No hay homologo en Java --

# range(start, stop): Esta forma le permite especificar el valor inicial de la secuencia. Genera números desde el valor inicial hasta el valor final,
# pero sin incluirlo, aumentando en 1 cada vez. Así, range (1, 11) haría un bucle del 1 al 10. -- No hay homologo en Java --

# range(start, stop, step): Esta es la forma más flexible, ya que permite definir el incremento (o decremento) entre los números de la secuencia. 
# Genera números empezando por el inicio, continuando hasta (pero sin incluir) el final, con cada número incrementado (o decrementado si el paso es negativo) por paso.
# Así, range(1, 10, 2) genera 1, 3, 5, 7 y 9. Una versión que utiliza pasos negativos es range(10, 5, -1), que generaría 10, 9, 8, 7 y 6.
# En Java: for (int i=1; i <= 10; i++){...}

#WHILE
#Un bucle while, por el contrario, ejecuta un bloque de código mientras se cumpla una condición especificada.
#Esto resulta útil cuando se desconoce de antemano el número de iteraciones o cuando el bucle debe continuar 
#hasta que se cumpla una condición específica

valid_input = False
while not valid_input:
  user_input = int(input("Please enter a number greater than 0: "))
  if user_input > 0:
    valid_input = True
  else:
    print("Invalid input. Please try again.")

#TAREA
#Creará un juego de adivinar números en el que el ordenador intentará adivinar un número secreto que usted le indique.
#El ordenador generará conjeturas aleatorias dentro de un rango (1 a 10) y continuará adivinando hasta que encuentre el número correcto

#1.onfigure su secret_number: Elija un número entre 1 y 10 y asígnele una variable llamada secret_number
#2.Inicializa otra variable llamada guess con un valor de 0.
#3.Completa el bucle while: Añada la condición al bucle while para asegurarse de que continúa ejecutándose mientras guess no sea igual a su secret_number.


# Set the secret_number variable here (between 1 and 10)
secret_number = 3
# Initialize the guess variable here with a value of 0
guess = 0
while not guess == secret_number:
	guess = random.randint(1, 10)
	print("Guessing:",guess)

print("I guessed the right number! It was",secret_number)

#LISTAS 
#Es una estructura de datos que almacena una colección ordenada de elementos. La diferencia con el Array es que los elementos pueden ser de cualquier tipo dentro de la lista.
#Las listas son dinamicas, y lso arrays son de tamaño fijo. Lo mas parecido en Java es el ArrayList o List<>, pero Java si obliga a que se un determinado tipo de dato.
#Las listas se definen encerrando los elementos entre corchetes [], separados por comas.

lenguajes = ["Python","Java","MySQL","JavaScript"]
#Acceso por elemento
print(lenguajes[0])
#Longitud de Lista
print(len(lenguajes)) #Devuelve el total de elementos
#Añadir
lenguajes.append("Cobol")
#Acceso con 'for in'
for lenguaje in lenguajes:
  print("Hello",lenguaje)
#Acceso con 'for' con 'range'
students = ["Alice", "Bob", "Charlie"]
for i in range(0,len(students)):
    print("Hello,", students[i]) 

#TAREA
# Crear un bucle for: Utilice la función range() para generar la secuencia de números. Recuerde que range(max_value + 1) incluirá max_value en el bucle.

# Comprueba la divisibilidad: Dentro del bucle for, utilice una sentencia if para comprobar si el número actual es divisible entre 3 y 4. 
# Para ello, utilice el operador módulo (%). Para ello, utilice el operador de módulo (%) para encontrar el resto al dividir por 3, y de nuevo al dividir por 4.
#  Si ambos restos son 0, utilice print() para mostrar el número.
max_value = 50

for i in range(0, max_value+1):
    if (i % 3 == 0 and i % 4 == 0 ):
        print(i)