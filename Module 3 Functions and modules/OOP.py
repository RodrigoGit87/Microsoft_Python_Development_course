#Programacion Orientada a Objetos (JAVA es mejor para esto :P)
#Python solo se puede tener un constructor por clase
class Car: #Creacion de clase, palabra clave 'class'
    #Variable de clase:compartida por todas las instancias (variable static en Java)
    max_fuel = 100
    instantiated_cars = 0

    #-- Constructor con parametros
    def __init__(self, modelo, año, color):
                    #atributos
        self.modelo = modelo
        self.año = año
        self.color = color
        self.fuel_level = 50
        Car.instantiated_cars += 1 #como el variable de clase se usa el nobmre de la Clase. En este caso es un contador de instancias.
    
    #Constructor SIN parametros
    # def __init__(self):
    #     self.modelo="unknown"
    #     self.color= "blanco"

    #Constructor CON parámetros por defecto (lo mejor de ambos mundos)
    #    def __init__(self, modelo="Desconocido", color="Blanco"):
    #     self.modelo = modelo
    #     self.color = color
    #El parámetro self es crucial - se refiere al objeto específico sobre el que se llama al método
    
    #-- Métodos
    #Los métodos son funciones definidas dentro de la clase que operan sobre los datos del objeto. 
    #Representan las acciones que puede realizar un objeto.
    #Para un Car, los métodos podrían incluir start_engine(), accelerate(), brake(), y refuel()
    def start_engine(self):
        print(f"The {self.modelo} {self.color} is ON")
    def accelerate(self):
        print(print(f"The {self.modelo} {self.color} is picking up speed"))
    
    @classmethod #metodo estatico de clase
    def get_total_cars(cls): #Recibe 'cls' en vez de 'self'. Accede a la CLASE (no al objeto)
        return cls.instantiated_cars  # Accede a la variable de clase

print(f"Instancias de coche creadas: {Car.get_total_cars}")            





#------- CONCEPTOS AVANZADOS ----------
#-Variables de clase
# Es como las variables static en Java. 
# Son compartidas por todos los objetos de esa clase
# En Python simplemente se colocan en el cuerpo de la clase sin self

#-Métodos estáticos
# Existen dos tipos de métodos "estáticos" en Python:
#
# 1. @staticmethod -> No recibe ni 'self' ni 'cls'. Es una función utilitaria
#    que vive dentro de la clase pero no accede a nada de ella. Equivalente a 'static' en Java.
# 
#  Ejemplo: validaciones, conversiones, funciones auxiliares.
#        @staticmethod
#        def is_valid_year(año):
#          return 1886 <= año <= 2026  # No usa self ni cls
# Se llama sin crear un objeto:
# print(Car.is_valid_year(2020))  # True
#
# 2. @classmethod -> Recibe 'cls' en vez de 'self'. Accede a la CLASE (no al objeto),
#    por lo que puede leer/modificar variables de clase. No tiene equivalente directo en Java.
#    Ejemplo: constructores alternativos (factory methods), acceder a variables de clase.
#

# Resumen:
#   (ninguno)      -> recibe self  -> accede al objeto + clase  -> método normal
#   @classmethod   -> recibe cls   -> accede solo a la clase    -> sin equivalente Java directo
#   @staticmethod  -> no recibe    -> no accede a nada          -> static en Java

#-Reutilización:
# Digamos que tienes una clase BankAccount. Puede crear objetos para diferentes cuentas (my_account, your_account, etc.), cada una con 
# su propio saldo e historial de transacciones. La lógica subyacente para depositar y retirar dinero está encapsulada dentro de la clase,
#  por lo que no tienes que repetirla para cada cuenta

#-Encapsulación:
#La encapsulación en Python se logra principalmente a través de una convención entre desarrolladores.
#Gira en torno al uso de un único guión bajo (_) prefijo para los nombres de atributos para señalar que están destinados para uso interno 
#dentro de la clase.
#Python no impide el acceso directo de los atributos de la clase desde fuera de la clase, de ahí esta convención para trata los atributos
#como privados. (Aqui es la diferencia principal con Java, donde si se puede definir el acceso como private,protected...)

#Ejemplo:
class BankAccount:
    #Constructor
    def __init__(self, balance):
        self._balance = balance  # Private attribute
    #Setter
    def deposit(self, amount):
        self._balance += amount
    #Getter
    def get_balance(self):
        return self._balance
#En este ejemplo, el atributo _balance está marcado como privado. Aunque técnicamente se podría acceder a él y modificarlo directamente 
#desde fuera de la clase (por ejemplo, my_account._balance = 1000), hacerlo violaría el principio de encapsulación. 
#La clase proporciona los métodos deposit() y get_balance() como interfaz adecuada para interactuar con el saldo de la cuenta.


#-Abstracción
#El módulo abc de Python (Abstract Base Classes) permite definir clases abstractas.
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):  # Concrete subclass
    def make_sound(self):
        return "Bark!"

#En este ejemplo, Animal es una clase base abstracta. Declara un método abstracto make_sound(), que no tiene una implementación concreta.
#Cualquier clase que herede de Animal (como Dog) debe proporcionar su propia implementación de make_sound()