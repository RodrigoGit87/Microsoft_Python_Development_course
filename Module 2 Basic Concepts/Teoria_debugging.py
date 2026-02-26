# El intérprete de Python lee el codigo de forma secuencial de izquierda a derecha y de arriba a abajo

#Errores mas comunes 

# 1. Errores de sangría
# Python es conocido por sus estrictas reglas de sangría. A diferencia de muchos otros lenguajes que usan llaves u otros 
# delimitadores para definir bloques de código, Python confía en la sangría para indicar la estructura de tu código
# x = 0

# if x > 5:
#     print("x is greater than 5")
#   else:  # Incorrect indentation
#     print("x is less than or equal to 5")
# En este caso, el bloque else es tratado como una sentencia separada fuera de la estructura if-else, conduciendo a una salida incorrecta.

# 2. Ámbito de las variables
# En Python, las variables tienen un ámbito, que define la región de tu código donde la variable es accesible. 
# Un error común es intentar acceder a una variable fuera de su ámbito.
flag = False
if flag:
    num = 10
    print(num) # No problem here

print(num) # No error if flag = True

# 3. Valores inmutables
# En Python, las cadenas son inmutables, lo que significa que su contenido no puede ser cambiado después de ser creadas.
# El código siguiente intenta cambiar el primer carácter de la cadena "Hola" de 'H' a 'h'. Sin embargo, esto resultará 
# en un TypeError porque las cadenas son inmutables.  
value = "Hello"
value[0] = 'h' #TypeError: 'str' object does not support item assignment
print(value)

# Solución:  Cuando crees que estás cambiando una cadena, en realidad estás creando una nueva.
# Por ejemplo, si quisieras crear una nueva cadena con la primera letra en minúscula, podrías hacer esto: 
value = "Hello"
new_value = "h" + value[1:]
print(new_value)  # Output: hello

#4. Reasignación de variables
# En Python, puedes accidentalmente usar el mismo nombre de variable de nuevo dentro de tu código.
# Esto puede llevar a resultados inesperados, ya que el uso posterior del nombre cambiará el valor de la variable. 
y = 5
if True:
   y = 10  # You've used 'y' again here!
   print(y)  # Output: 10

print(y)  # Output: 10
# Solución: Elija nombres distintos para sus variables para evitar este problema. 

# 5. Pasar por alto las excepciones
# Como intentar abrir un archivo que no existe, o referenciar una variable que no existe
x = 10
y = 0
 
result = x / y  # ZeroDivisionError
# Solución: Usar el bloque try-except 
x = 10
y = 0

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero")

#Errores avanzados y buenas prácticas
# Importaciones circulares:
# 'importar' es como obtener ayuda de otra materia. Tú 'importas' código de otro archivo para usarlo en tu propio programa
# una "importación circular", en Python, ocurre cuando dos archivos necesitan utilizar código del otro, creando un bucle

# Administración de la memoria:
# La administración de la memoria es una parte importante de la programación. 
# Incluso un programa simple puede causar problemas si no maneja la memoria de manera eficiente.  
# ASÍ COMO LOS PROGRAMAS SE HACEN MÁS COMPLEJOS Y MANEJAN MÚLTIPLES USUARIOS O PROCESOS AL MISMO TIEMPO, EL USO INEFICAZ 
# DE LA MEMORIA PUEDE PROVOCAR PROBLEMAS DE RENDIMIENTO, CAÍDAS O INESTABILIDAD DEL SISTEMA, POR LO QUE ES FUNDAMENTAL SABER 
# CÓMO ESCRIBIR CÓDIGO QUE UTILICE LOS RECURSOS DE FORMA RESPONSABLE.