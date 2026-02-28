# GLOBAL SCOPE -> Las variables definidas fuera de cualquier función tienen alcance global.
# Son accesibles desde cualquier parte del módulo (incluidas las funciones).
saludo = "   Hello world   "  # Variable global

def print_upper():
    print(saludo.upper().strip()) 

print_upper()  # La función ACCEDE a la variable global, pero NO la modifica.
               # .upper() y .strip() devuelven una copia transformada, el original no cambia.
print(saludo)  # Comprobamos que 'saludo' conserva su valor original con los espacios.

# LOCAL SCOPE -> Las variables creadas dentro de una función solo existen dentro de ella.
# No se pueden acceder desde fuera; se crean al llamar la función y se destruyen al terminar.
def calculate_average(numbers):
    total = 0  # Local variable
    count = len(numbers)  # Local variable
    for num in numbers:
        total += num
    average = total / count
    return average

print(calculate_average([2, 5, 4, 1]))

# VENTAJAS DEL LOCAL SCOPE:
# 1. Encapsulación: Los detalles internos de la función quedan ocultos al resto del programa.
# 2. Evitar colisiones de nombres: Puedes reutilizar nombres como 'total' o 'count'
#    en distintas funciones sin conflicto, ya que cada una tiene su propio ámbito.
# 3. Gestión de memoria: Las variables locales se crean al llamar la función
#    y se liberan automáticamente cuando esta termina.

#VENTAJAS DEL AMBITO GLOBAL
# Ideal para constantes, valores q no estan destinados a cambiar (rutas de archivos, constantes matematicas, ...)
# Cuando se neceseite compartir la variable entre varias funciones dentro de un mismo modulo


# Ámbitos anidados y el ámbito envolvente
# En programas Python más complejos, puedes tener funciones dentro de funciones (funciones anidadas). 
# En este caso, una variable en la función externa (ámbito envolvente) es visible para la función interna, incluso si no es global.