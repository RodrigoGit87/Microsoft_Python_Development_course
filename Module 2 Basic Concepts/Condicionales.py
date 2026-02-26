#IF - ELSE
#La sentencia if-else sigue una estructura sencilla. Si una condición es verdadera, se ejecuta el bloque de código dentro de la sentencia if;
#en caso contrario, se ejecuta el bloque de código dentro de la sentencia else.
#Esto permite la ejecución selectiva de código basada en criterios específicos.

player_score = 180

if player_score > 100:
  print("Congratulations! You scored over 100 points.")
else:
  print("Keep trying to beat your high score!")

#Problemas potenciales y buenas prácticas
#Los bucles deben ser concisos:  Evite anidar los bucles demasiado profundamente
#Utilice condiciones significativas: Evite las condiciones demasiado complejas que puedan ofuscar la lógica del código
#Considera construcciones alternativas: Las construcciones alternativas como las listas de comprensión o las funciones lambda pueden proporcionar 
#formas más concisas y eficientes de lograr el mismo resultado que los bucles y las sentencias condicionales

# TIP
# La distinción clave entre los bucles for y while es que los bucles for iteran sobre una secuencia conocida, mientras que los bucles while iteran 
# hasta que una condición se convierte en falsa.

# TAREA COACH
#determinar el precio de las entradas de cine según la edad del cliente. Aquí están las reglas de precios:
#Niños (menores de 12 años): $8
#Adultos (12-64 años): $12
#Mayores (65 años o más): $10

edad = 12
precio = 0
if(edad < 12):
    precio = 8
    print("tarifa para menor de edad, $", precio,sep="")
elif(edad < 65):
    precio = 12
    print("tarifa para adulto, $",precio,sep="")
else:
    precio = 10    
    print("tarifa para mayores, $",precio,sep="")


# elif le permite encadenar varias condiciones, proporcionando respuestas más matizadas basadas en el valor de la temperatura.
temperature = 15  # Let's assume the temperature is 15 degrees Celsius

if temperature < 10:
    print("Wear a jacket! It's cold out there.")
elif 10 <= temperature < 20:
    print("A light sweater should be fine. It's a bit chilly.")
elif 20 <= temperature < 30:
    print("Enjoy the pleasant weather! No need for extra layers.")
else:
    print("It's hot! Stay hydrated and wear sunscreen.")



for i in range (10, -1, -1):
  print(i)
  if( i == 5):
    print("Punto medio alcanzado!")