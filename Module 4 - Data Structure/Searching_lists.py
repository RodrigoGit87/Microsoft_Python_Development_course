### TIPOS DE BUSQUEDA EN LISTAS ###

# LINEAR SEARCH (BUSQUEDA LINEAL)
# La búsqueda lineal recorre la lista elemento por elemento,
# comparando cada uno con el valor buscado hasta encontrarlo
# o llegar al final de la lista.
# Complejidad: O(n) - en el peor caso recorre todos los elementos.

def linear_search(list, target):
    """
    Busca un elemento en una lista de forma secuencial.

    Args:
        list: La lista donde buscar.
        target: El elemento que se quiere encontrar.

    Returns:
        El índice del elemento si se encuentra, -1 si no está en la lista.
    """
    for i in range(len(list)):
        if list[i] == target:
            return i  # Devuelve el índice donde se encontró
    return -1  # return por defecto: No se encontró el elemento


# --- Ejemplo práctico ---
shopping_list = ["manzanas", "leche", "pan", "huevos", "arroz", "pasta"]

product = "huevos"
result = linear_search(shopping_list, product)

if result != -1:
    print(f"'{product}' encontrado en la posición {result}")
else:
    print(f"'{product}' no está en la lista")

# Buscar un producto que NO existe
product_2 = "chocolate"
result_2 = linear_search(shopping_list, product_2)

if result_2 != -1:
    print(f"'{product_2}' encontrado en la posición {result_2}")
else:
    print(f"'{product_2}' no está en la lista")


# ============================================================
# BINARY SEARCH (BUSQUEDA BINARIA)
# REQUISITO: La lista DEBE estar ordenada previamente.
# La búsqueda binaria divide la lista ordenada por la mitad en cada paso,
# descartando la mitad donde NO puede estar el elemento.
# Complejidad: O(log n) - mucho más rápida que la lineal en listas grandes.

def binary_search(sorted_list, target):
    """
    Busca un elemento en una lista ORDENADA dividiendo el rango de búsqueda a la mitad.

    Args:
        sorted_list: La lista ordenada donde buscar.
        target: El elemento que se quiere encontrar.

    Returns:
        El índice del elemento si se encuentra, -1 si no está en la lista.
    """
    low = 0                      # Índice inferior del rango de búsqueda
    high = len(sorted_list) - 1  # Índice superior del rango de búsqueda

    while low <= high:
        mid = (low + high) // 2  # Usar división de enteros (//) para obtener un int como punto medio
        if sorted_list[mid] == target:
            return mid           # Encontrado en el punto medio
        elif sorted_list[mid] < target:
            low = mid + 1        # El target está en la mitad derecha (+1 para excluir el punto medio ya encontrado y no entre en bucle infinito)
        else:
            high = mid - 1       # El target está en la mitad izquierda (-1 idem)

    return -1  # return por defecto: No se encontró el elemento


# --- Ejemplo práctico ---
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 67, 91,110,180, 202,303,404,505, 670, 1000]
print("\n--- BINARY SEARCH ---")
print(f"Lista ordenada: {numbers}")

target = 23
result = binary_search(numbers, target)

if result != -1:
    print(f"El número {target} encontrado en la posición {result}")
else:
    print(f"El número {target} no está en la lista")

# Buscar un número que NO existe
target_2 = 50
result_2 = binary_search(numbers, target_2)

if result_2 != -1:
    print(f"El número {target_2} encontrado en la posición {result_2}")
else:
    print(f"El número {target_2} no está en la lista")


# ============================================================
# OPERADOR "in" (BUSQUEDA CON OPERADOR NATIVO)
# Python tiene el operador "in" que permite comprobar si un elemento
# existe en una lista de forma sencilla y legible.
# Internamente hace una búsqueda lineal O(n), pero es la forma
# más "pythónica" de buscar.
# No devuelve el índice, solo True o False.

print("\n--- OPERADOR 'in' ---")

colors = ["rojo", "azul", "verde", "amarillo", "naranja"]
print(f"Lista: {colors}")

# Comprobar si un elemento EXISTE
search = "verde"
if search in colors:
    print(f"'{search}' está en la lista ")
else:
    print(f"'{search}' NO está en la lista ")

# Comprobar si un elemento NO EXISTE (con "not in")
search_2 = "morado"
if search_2 not in colors:
    print(f"'{search_2}' NO está en la lista ")
else:
    print(f"'{search_2}' está en la lista ")

# Si necesitas el índice, puedes combinar "in" con .index()
search_3 = "azul"
if search_3 in colors:
    index = colors.index(search_3)
    print(f"'{search_3}' encontrado en la posición {index}")


# ============================================================
# LIST COMPREHENSION (COMPRENSIÓN DE LISTAS)
# Permite crear una nueva lista a partir de otra, aplicando
# una condición o transformación en una sola línea.
# Sintaxis: [expresión for elemento in lista if condición]

print("\n--- LIST COMPREHENSION ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f"Lista original: {numbers}")

# Crear una lista con solo los números pares
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"Números pares:  {even_numbers}")


# ============================================================
# BISECT (BUSQUEDA MÓDULO bisect)
# El módulo bisect de Python implementa búsqueda binaria optimizada.
# Permite buscar la posición donde insertar un elemento en una lista ordenada,
# y también insertar elementos manteniendo el orden.
# REQUISITO: La lista DEBE estar ordenada.
# Complejidad: O(log n) para buscar.

import bisect

print("\n--- BISECT ---")

# Tenemos una lista DESORDENADA
scores = [88, 45, 92, 31, 67, 73, 55, 100, 12, 79]

# Ordenamos la lista (bisect requiere lista ordenada)
scores.sort()
print(f"Lista ordenada:    {scores}")

# Insertar un numero numero mientras se mantiene el orden
new_number = 10
bisect.insort(scores, new_number)

print(f"Lista actualizada: {scores}")