"""EJERCICIO 2
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
máximo y el mínimo, utilizando la función anterior."""
def calcularMaxMin(lista):
    print("\nEl valor máximo de la lista es:",max(lista))
    print("El valor mínimo de la lista es:",min(lista))
    print("Lista completa:",lista)

def introducirNumeros():
    lista = []
    for i in range(11):
        numero = int(input("Introduce un número:"))
        lista.append(numero)
    calcularMaxMin(lista)

introducirNumeros()