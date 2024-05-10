#Calculadora de impuesto

print("Calculadora de impuestos: ")

SalarioAnual = int(input("Ingrese su salario anual: "))


if  SalarioAnual < 400000:
    ImpuestoBajo = SalarioAnual*0/100
    print("El impuesto a pagar es: ", ImpuestoBajo)
elif 400000 <= SalarioAnual <+ 700000:
    ImpuestoMedio = SalarioAnual*10/100
    print("El impuesto a pagar es: ", ImpuestoMedio)
elif 700000 < SalarioAnual:
    ImpuestoAlto = SalarioAnual*20/100
    print("El impuesto a pagar es: ", ImpuestoAlto)
    