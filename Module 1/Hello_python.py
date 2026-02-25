print("Hello, world!")

#Variables
num1 = 10
num2 = 5
string = "string" 
boolean = True

#Basic operations

    #Addition +
addition = num1 + num2
    #Subtraction
subtraction = num1 - num2    
    #Multiplication
multiplication = num1 * num2
    #Division
division = num1 / num2
    #Module (Devuelve el resto de una división)
modulo =  num1 % num2    
    #Exponentiation
exponent = num1**num2    


print("addition:", addition, "subtraction:", subtraction, 
"multiplication:", multiplication, "division:", division,"modulo:",modulo,
"exponentiation:",exponent)

#Ejemplo matematico
discount = 0.2  # 20% discount --también .2
price = 50
final_price = price * (1 - discount) #50 * (1 - 02) == 50 * 0.8
print(final_price)

#TAREA
#Programa que calcule el precio final de un articulo después de aplicar un descuento. Calcular el descuento y restar el 
#descuento al precio original. En variables separadas
original_price = 75
discount_rate = 15

discount = (discount_rate / 100) * original_price
final_price = original_price - discount

print("The final price after discount is: $", final_price)