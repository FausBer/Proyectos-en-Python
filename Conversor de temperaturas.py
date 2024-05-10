#Conversor de temperaturas

#Menu

print("Conversor de temperaturas")
CelFah = print("1 - De Celsius a Fahrenheit")
FahCel = print("2 - De Fahrenheit a Celsius")
pregunta = input("Marque 1 o 2: ")

#Condicional para verificar el tipo de operacion

if pregunta == "1":
   
    #Casilla para que el usuario ingrese el dato

    Celsius = int(input("Pon la temperatura en Grados Celsius: "))
   
    #Calculo

    CalculoCelFah = (Celsius * 9/5) + 32
   
    #Salida

    print("La temperatura de ", Celsius ,"Grados Celsius a Grados Fahrenheit es: ", CalculoCelFah)
    print("Hasta Luego!")
    
elif pregunta == "2":
   
    #Casilla para que el usuario ingrese el dato
    Fahrenheit = int(input("Pon la temperatura en Grados Fahrenheit: "))
   
    #Calculo

    CalculoFahCel = (Fahrenheit - 32) * 5/9

    #Salida

    print("La temperatura de ", Fahrenheit ,"Grados Fahrenheit a Grados Celsius es: ", CalculoFahCel)
    print("Hasta Luego!")

else:
    print("No se encontro el tipo de dato a convertir")
    print("Hasta Luego!")