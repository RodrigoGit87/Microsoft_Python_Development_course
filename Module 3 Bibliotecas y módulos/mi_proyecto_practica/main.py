# File: main.py (located in the 'my_project' directory)
import string_utils # <-- Imported custom package
import geometry_calculations # <-- Imported custom package

radius = 5
area = geometry_calculations.calculate_area_circle(radius)

print(f"Area of circle: {area}")


text = "cuantas vocales hay en esta frase?"
vocales = string_utils.count_vowels(text)
print(f"{text} vocales: {vocales}")