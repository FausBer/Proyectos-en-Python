print("--------------------------------------")
print("Administre su lista de compras:")
respuesta = input("Quieres ingresar?: ")

ListaCompras = ["Lista: ",]  # Movido fuera del bucle while

while respuesta.lower() == "si":
    print("--------------------------------------")
    print("1 - Agregar Producto. \n2 - Eliminar producto de la lista. \n3 - Mostrar lista de compras. \n4 - Salir")
    Acciones = input("Seleccione alguna accion: ")
    print("--------------------------------------")

    # Agregar
    if Acciones == "1":
        ListaCompras.append(input("Agregue un elemento a la lista: "))
    
    # Eliminar
    elif Acciones == "2":
        elemento_eliminar = input("Elimine el elemento: ")
        if elemento_eliminar in ListaCompras:
            ListaCompras.remove(elemento_eliminar)
        else:
            print("El elemento no está en la lista.")
    
    # Mostrar
    elif Acciones == "3":
        print("Lista de compras:")
        for item in ListaCompras:
            print(item)
            
    # Salir
    elif Acciones == "4":
        print("Hasta Luego!")
        break

    respuesta = input("Quieres continuar?: ")  # Preguntar al final de cada iteración si el usuario desea continuar
else:
    print("Hasta Luego!")
