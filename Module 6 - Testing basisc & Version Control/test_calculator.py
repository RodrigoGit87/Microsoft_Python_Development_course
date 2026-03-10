from calculator import add
import pytest
"""Tenemos un archivo básico de Python llamado calculator.py con una función simple. 
A continuación, vamos a crear un archivo de pruebas llamado test_calculator.py. 
pytest descubre automáticamente los archivos de prueba y las funciones basándose en sus convenciones de nomenclatura."""



def test_add():
    """La función de prueba comprueba si la función add suma correctamente 2 y 3.
La declaración assert es clave aquí. Verifica que el resultado de sumar 2 y 3 sea 5.
Si no lo es, la prueba fallará."""
    assert add(2,3) == 5

def test_bug():
    """Aqui forzamos el fallo, diciendo q el resultado es una cadena vacia
    Evidentemente,pytest lanzará un 'failure' diciendo el metodo donde ha detectado el fallo, el codigo q falló e incluso lo que
    debería haber dado (5)"""
    assert add(2,3) == ""

# >       assert add(2,3) == ""
# E       AssertionError: assert 5 == ''
# E        +  where 5 = add(2, 3)

# Module 6 - Testing basisc & Version Control\test_calculator.py:19: AssertionError


""" FIXTURES """
"""Se crea una funcion y se 'anota' con el @pytest.fixture
    Un fixture tiene un scope predeterminado a la funcion anotada"""
#Definir un fixture
@pytest.fixture
def sample_data():
    #Crear una list con datos de ejemplo
    data = [1,2,3,4,5]
    return data

#Usar el fixture en un test
def test_sum(sample_data):
    #Test code
    assert sum(sample_data) == 15     

#Otro test usando el mismo fixture
def test_max(sample_data):
    #Test code: check maximo valor en una lista
    assert max(sample_data) == 5

#Definir un fixture con funcionalidades
@pytest.fixture
def enhanced_data():
    print("Ajustando el fixture enhanced_data")
    
    #Crear list de enteros
    data = [10,20,30,40,50]

    #Codigo: 'mejorar' la list data
    enhanced_data = [x * 2 for x in data]

    #Retornar la list mejorada
    return enhanced_data

#TEST que usa el enhanced_data
def test_sum_enhanced(enhanced_data):
    #Comprueba q la suma de elementos en enhanced_data es correcta
    assert sum(enhanced_data) == 300 #10*2 + 20*2 + 30*2 + 40*2 + 50 *2     

#Otro test q usa el enhanced_data fixture
def test_max_enhanced(enhanced_data):
    #Comprueba el valor maximo en enhanced_data list
    assert max(enhanced_data) == 100 #50 * 2    