"""Ejercicio 2
Vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta."""
diccionario = {}

option = 0

while (option!=3):
    option = int(input("\n1.- Guardar datos fruta\n2.- Mostrar datos fruta\n3.-Salir\n"))
    if option == 1:
        nombre_fruta = input("Introduce el nombre de la fruta:")
        precio_fruta = float(input("Introduce el precio de la fruta:"))
        diccionario[nombre_fruta]=precio_fruta
        print("FRUTA GUARDADA")
    elif option ==2:
        mostrar = "Y"
        while (mostrar=="Y"):
            nombre_fruta_buscar = input("Introduce el nombre de la fruta:")
            if nombre_fruta_buscar not in diccionario:
                print("ERROR, la fruta no existe")
            else:
                valor_fruta_buscar = diccionario.get(nombre_fruta_buscar)
                print(nombre_fruta_buscar,"->",valor_fruta_buscar,"€")
            mostrar = input("¿Desea consultar más datos? (Y/N)")