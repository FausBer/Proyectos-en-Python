#Calculadora de tarifas de envio
#Menu
print("Calcule la tarifa de envio de la encomienda \n ¿Cómo se calcula el envio? \n Para establecer el Rango de Peso de las encomiendas y paquetes se debe comparar el Peso volumétrico y el Peso real y tomar el mayor de los dos para determinar el Rango Tarifario al que pertenece el paquete. \n")
PesoReal = int(input("ingrese el peso del paquete en kilogramos: "))
print("Seleccione la forma geometrica del paquete que desea enviar: \n") 
print("1 - Rectangular/Cuadrada \n","2 - Triangular  \n", "3 - Cilindrica \n")
pregunta = input("Marque 1, 2 o 3: ")

#Se verifica la condicion, si el usuario quiere calcular el peso volumetrico ya sea de un rectangulo/cuadrado, triangulo o cilindrico, luego se verifica cual es mayor si el peso volumetrico o el peso real y a partir de eso se calcula el valor del envio

#Calculo RECTANGULAR/CUADRADO

if pregunta == "1":

    dimensionRCT = int(input("Ingrese el primer lado: ")), int(input("Ingrese el segundo lado: ")), int(input("Ingrese el tercer lado: "))
    calculoRC = (dimensionRCT[0] * dimensionRCT[1] * dimensionRCT[2]) /6000

    if PesoReal > calculoRC :
        print("Se tomara en cuenta el Peso real")

        if PesoReal <= 5:
            print("El precio del envio es de $8.500,00")
        elif 5 < PesoReal <= 15:
            print("El precio del envio es de $15.000,00")
        elif 15 < PesoReal <= 25:
            print("El precio del envio es de $21.450,00")
        else:
            print("La empresa no soporta los paquetes excedidos a los 25 kilogramos.")

    elif PesoReal < calculoRC :
        print("Se tomara en cuenta el Peso Volumetrico")
        if calculoRC <= 5:
            print("El precio del envio es de $8.500,00")
        elif 5 < calculoRC <= 15:
            print("El precio del envio es de $15.000,00")
        elif 15 < calculoRC <= 25:
            print("El precio del envio es de $21.450,00")
        else:
            print("La empresa no soporta los paquetes excedidos a los 25 kilogramos.")

#Calculo TRIANGULAR

elif pregunta == "2":
    dimensionRCT = int(input("Ingrese el primer lado: ")), int(input("Ingrese el segundo lado: ")), int(input("Ingrese el tercer lado: "))
    calculoT = (dimensionRCT[0] * dimensionRCT[1] * dimensionRCT[2] /2 ) /6000

    if PesoReal > calculoT :
        print("Se tomara en cuenta el Peso real")

        if PesoReal <= 5:
            print("El precio del envio es de $8.500,00")
        elif 5 < PesoReal <= 15:
            print("El precio del envio es de $15.000,00")
        elif 15 < PesoReal <= 25:
            print("El precio del envio es de $21.450,00")
        else:
            print("La empresa no soporta los paquetes excedidos a los 25 kilogramos.")

    elif PesoReal < calculoT :
        print("Se tomara en cuenta el Peso Volumetrico")
        if calculoT <= 5:
            print("El precio del envio es de $8.500,00")
        elif 5 < calculoT <= 15:
            print("El precio del envio es de $15.000,00")
        elif 15 < calculoT <= 25:
            print("El precio del envio es de $21.450,00")
        else:
            print("La empresa no soporta los paquetes excedidos a los 25 kilogramos.")

#CALCULO CILINDRICO

elif pregunta == "3":
    DimensionCil = int(input("Ingrese el primer diametro: ")), int(input("Ingrese el segundo diametro: ")), int(input("Ingrese el largo: "))
    calculoCil = (DimensionCil[0] * DimensionCil[1] * DimensionCil[2]) /6000

    if PesoReal > calculoCil :
        print("Se tomara en cuenta el Peso real")


        if PesoReal <= 5:
            print("El precio del envio es de $8.500,00")
        elif 5 < PesoReal <= 15:
            print("El precio del envio es de $15.000,00")
        elif 15 < PesoReal <= 25:
            print("El precio del envio es de $21.450,00")
        else:
            print("La empresa no soporta los paquetes excedidos a los 25 kilogramos.")

    elif PesoReal < calculoCil :
        print("Se tomara en cuenta el Peso Volumetrico")
        if calculoCil <= 5:
            print("El precio del envio es de $8.500,00")
        elif 5 < calculoCil <= 15:
            print("El precio del envio es de $15.000,00")
        elif 15 < calculoCil <= 25:
            print("El precio del envio es de $21.450,00")
        else:
            print("La empresa no soporta los paquetes excedidos a los 25 kilogramos.")

else:
    print("Vuelve a ingresar los datos: ")
    

