"""Ejercicio 1
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena."""
cadena = input("Introduce una cadena de texto:")
diccionario = {}
for i in cadena:
    if(i not in diccionario):
        diccionario[i]=1
    else:
        cantidad = diccionario.get(i)
        diccionario[i]= cantidad + 1

print(diccionario)
for clave, valor in diccionario.items():
    print("CLAVE -",clave, ", VALOR -",valor)