#SINTAXSIS DE UNA FUNCION
#La nomenclatura para nombrar funciones es con 'snake_case' y dar un nombre que indique bien lo que hace. Se suele empezar con un verbo y evitar generalizaciones.
def function_name(parameters):
    """ String explicando que hace la funcion """
    #Codigo en sí
    return result

#ejemplo
def calcular_area_rect(base,altura):
    """Este metodo devuelve el area de un rectangulo"""
    areaRec = base * altura
    return areaRec

#BUILT-IN FUNCTIONS
# print() input() 

# Casting
# int() str() float() bool() list()

# Funciones Matemáticas
# abs(x): Devuelve el valor absoluto de un número.
# round(x, n): Redondea un número
# sum(iterable): Suma todos los elementos de una lista o tupla
# max() / min(): Devuelven el valor máximo o mínimo de un conjunto.

# ACTIVIDAD
# Comience con la lista antarctic_temperatures, que contiene los registros diarios de temperatura.
antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Aplique la función max() a la lista antarctic_temperatures para obtener la temperatura más alta registrada.
# Aplique la función min() a la lista antarctic_temperatures para determinar la temperatura más baja registrada.
highest_temp = max(antarctic_temperatures)
lowest_temp = min(antarctic_temperatures)
print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")

# Calcule la temperatura media sumando todas las temperaturas de la lista antarctic_temperatures mediante la función sum() 
# y dividiendo por el número de temperaturas, que puede determinar mediante la función len(). 
# Redondee la temperatura media calculada a un decimal utilizando la función round().
average_temp = round(sum(antarctic_temperatures) / len(antarctic_temperatures), 1)
print("Average temperature:", average_temp, "°C")

# Calcule el valor absoluto de la temperatura más fría utilizando la función abs().
coldest_temp_abs = abs(lowest_temp)
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")

# --- CONSIDERACIONES AVANZADAS --
#Si una función está destinada a un uso interno dentro de un módulo y no debe accederse a ella directamente desde el exterior, anteponga a su nombre un guión bajo (_). 
# Por ejemplo, _calculate_internal_metrics. En el caso de las funciones que devuelven un valor booleano (Verdadero/Falso), se recomienda utilizar prefijos como is_, has_ o can_ para indicar su naturaleza

# PRACTICA
def calculate_diameter_circle(radius: float) -> float:
    """Calculate the diameter of a circle
        Args
            the radius of the circle in float type
        Returns
            the diameter based on the radius given
        Raises
            Math error if negative radius"""
    diameter= float(radius * 2)
    if float(radius) < 0:
        diameter=-1 
    return diameter

# ---- TECNICAS AVANZADAS -----
# Puede utilizar *args para recopilar argumentos posicionales en una tupla y **kwargs para recopilar argumentos de palabras clave en un diccionario
#Ejemplo:
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)

# Parametros obligatorios y opcionales:
def create_user_profile(name, age, occupation="Student", interests=None):
    #name y age son parámetros obligatorios porque un perfil de usuario no estaría completo sin ellos.
    #occupation y interests son opcionales. occupation es por defecto "Estudiante", garantiza que la función pueda crear un perfil básico aunque no se proporcionen.
    #interests es por defecto None, lo que permite a los usuarios omitir esta información si así lo desean.
    if interests is None:  # Initialize if None
        interests = [] 

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "interests": interests
    }
    return profile

user = create_user_profile("Bob", 18)  # Se puede hacer la llamada a la funcion aunque no se hallan especificado los parametros opcionales.
print(user)