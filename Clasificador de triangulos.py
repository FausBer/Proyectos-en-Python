#Clasificador de triangulos

print("Ingrese las longitudes de los tres lados de un triangulo: ")

#Declaro las variables que quiero que el usuario ingrese

LadoA = input("Ingrese el primer lado: ")
LadoB = input("Ingrese el segundo lado: ")
LadoC = input("Ingrese el tercer lado: ")

#Realizo el calculo para saber que triangulo es y le devuelvo al usuario el resultado

if LadoA == LadoB == LadoC:
    print("Este triangulo es equilatero")
elif (LadoA != LadoB != LadoC) and (LadoA != LadoC != LadoB):
    print("Este triangulo es escaleno")
else:
    print("Este triangulo es isosceles")