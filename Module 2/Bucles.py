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


