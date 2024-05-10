#Calculador de IMC

#Titulo
print("Calcule su indice de masa corporal: ")

#Variables y formula

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura**2)

#Mostrar por pantalla su IMC

print("Su indice de masa corporal es de: ", IMC)

if IMC <= 18.5 : 
    print("Se encuentra dentro del rango de peso insuficiente.")

elif 18.5 < IMC <= 24.9:
    print("Se encuentra dentro del rango de peso normal o saludable.")

elif 25.0 <= IMC <+ 29.9:
    print("se encuentra dentro del rango de sobrepeso.")

elif IMC >= 30.0:
    print("se encuentra dentro del rango de obesidad.")

else:
    print("Cargue los datos nuevamente")
