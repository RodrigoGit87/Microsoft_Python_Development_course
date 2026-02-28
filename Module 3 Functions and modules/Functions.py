#Sintaxis de una funcion
def function_name(parameters):
    """ String explicando que hace la funcion """
    #Codigo en sí
    return result

#ejemplo
def calcularAreaRect(base,altura):
    """Este metodo devuelve el area de un rectangulo"""
    areaRec = base * altura
    return areaRec
#Built-in functions
# print() input() 

# Casting
# int() str() float() bool() list()

# Funciones Matemáticas
# abs(x): Devuelve el valor absoluto de un número.
# round(x, n): Redondea un número
# sum(iterable): Suma todos los elementos de una lista o tupla
# max() / min(): Devuelven el valor máximo o mínimo de un conjunto.

#ACTIVIDAD
# Comience con la lista antarctic_temperatures, que contiene los registros diarios de temperatura.
# Aplique la función max() a la lista antarctic_temperatures para obtener la temperatura más alta registrada.
# Aplique la función min() a la lista antarctic_temperatures para determinar la temperatura más baja registrada.
# Imprima las temperaturas más alta y más baja.
# Calcule la temperatura media sumando todas las temperaturas de la lista antarctic_temperatures mediante la función sum() 
# y dividiendo por el número de temperaturas, que puede determinar mediante la función len(). 
# Redondee la temperatura media calculada a un decimal utilizando la función round().
# Imprima la temperatura media redondeada.
# Calcule el valor absoluto de la temperatura más fría utilizando la función abs().
# Imprime el valor absoluto de la temperatura más fría.
antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Find the highest and lowest temperatures
highest_temp = max(antarctic_temperatures)
lowest_temp = min(antarctic_temperatures)

print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")

# Calculate the average temperature
average_temp = round(sum(antarctic_temperatures) / len(antarctic_temperatures))
print("Average temperature:", average_temp, "°C")

# Find the absolute value of the coldest temperature
coldest_temp_abs = abs(lowest_temp)
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")

