#Las LISTAS son estructuras de datos fundamentales en Python, que sirven como contenedores versátiles para almacenar 
#colecciones de elementos.A diferencia de las matrices de otros lenguajes de programación, que pueden restringir el tipo de elementos, 
# las listas de Python ofrecen la flexibilidad de contener diversos tipos de datos, incluyendo números, cadenas, 
# booleanos e incluso otras listas. Esta naturaleza dinámica hace de las listas una herramienta indispensable para diversas 
# tareas de programación, desde la simple organización de datos hasta la compleja implementación de algoritmos.

#Declaracion
# Lista vacía: Su programa necesita tener una lista que se cargará durante la ejecución del programa. Puede obtener valores del usuario 
# o de un archivo y almacenarlos durante la ejecución del programa. La lista debe ser inicializada primero.
new_list = []
    #enteros
enteros = [1,2,3,4,5,6,7,8,9,10]
    #caracteres
chars = ["a","b","c","d","e"]
    #booleans
coin_flip = [True, False, True, True, False]
    # Valores mixtos: Su programa necesita almacenar la información de los estudiantes en una lista. Quieres almacenar el nombre 
    # de un estudiante (una cadena), su edad (un número), su especialidad (una cadena), su GPA (un número en coma flotante), 
    # y si es un estudiante a tiempo completo (un valor booleano). 
    # Ten en cuenta que verás otras formas más eficientes de hacer esto en lecturas posteriores, cuando te encuentres con diccionarios.
student_record = ["Rodrigo", 38, "Multiplatform Development Application", 8.8, True]

#Impresión
grocery_list = ["milk", "hummus", "bread", "cheese", "apples"]
print(grocery_list)
    
    #impresion por indice
print(grocery_list[3])
    
    #imprimir longitud de la lista
print(len(grocery_list)) #5 (recordar q lso indices empiezan en 0. 5 elementos == 0 a 4 posiciones)
    
    #imprimir el ultimo elemento (sin saber la posición)
print(grocery_list[len(grocery_list) - 1])
    #o guardar en una variable el retorno del len() y usarla en el print (Más legible)
last_index = len(grocery_list) -1 
print(grocery_list[last_index])   

#Rebanar: Acceso a una parte de la lista
# A veces, sólo necesita una parte de la lista. 
# Python te permite extraer una "porción" de tu lista, como ésta:
print(grocery_list[0:2]) # desde el 0 hasta el 2 pero sin incluirlo (coge la 0 y la 1)

#Metodos mas comunes para trabajar listas
# Comando                             Qué hace

# len(lista)                          Te dice cuántas cosas hay en la lista.

# list.append(x)                      Añade x al final de la lista.

# list.insert(i, x)                   Añade x en la posición i de la lista.

# list.remove(x)                      Elimina la primera x de la lista.

# lista.sort()                        Ordena la lista.

# list.reverse()                      Invierte el orden de los elementos de la lista.

# list.count(x)                       Retorna cuántas veces aparece x en la lista.

# list.index(x)                       Indica la posición de la primera x en la lista.

# list.pop()                          Elimina y retorna el ultimo elemento de una lista o del indice especificado


#Compresión de listas
# [expression for item in iterable]

# [ ... ]: Los corchetes significan que el resultado será una nueva lista.

# expression: Esta es la operación o transformación que se aplica a cada elemento del iterable.
#  El resultado de esta expresión para cada elemento se convertirá en un elemento de la nueva lista.

# for item in iterable: Esta parte especifica el iterable con el que se está trabajando y asigna cada elemento del iterable 
# a la variable item durante cada iteración. Es similar al comienzo de un bucle for.  
#Ejemplo:

exam_scores = [55, 70, 78, 52, 68]
curve_amount = 10
# Use a list comprehension to create a new list of curved grades
curved_grades = [score + curve_amount for score in exam_scores]
print("Original scores:", exam_scores)
print("Curved scores:", curved_grades)

#Listas bidimensionales: Listas dentro de listas
grid = [ 
      [1, 2, 3],

	  [4, 5, 6],

	  [7, 8, 9]
    ]
# Para acceder a un número individual de la cuadrícula, utilizarías dos índices.
# Por ejemplo, para imprimir el número 6 (segunda fila, tercera columna)    
print(grid[1][2])