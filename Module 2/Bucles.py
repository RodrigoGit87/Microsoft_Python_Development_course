import random

#FOR
# Un bucle for itera sobre una secuencia, como una lista, tupla o cadena, ejecutando un bloque de código por cada 
# elemento de la secuencia. Esto resulta especialmente útil cuando se trabaja con colecciones de datos 
# o cuando se conoce de antemano el número de iteraciones.
for i in range(0,10):
    print("iteration:",i)


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

