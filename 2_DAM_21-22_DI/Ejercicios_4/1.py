"""Ejercicio1
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo."""
import random
import math

numeros = []
for i in range(10):
    j = random.randrange(1,11)
    numeros.append(j)
print("Valores originales:",numeros)

numeros_cuadrado = []
for item in numeros:
    j = math.pow(item,2)
    numeros_cuadrado.append(j)
print("Valores al cuadrado:",numeros_cuadrado)

numeros_cubo = []
for item in numeros:
    j = math.pow(item,3)
    numeros_cubo.append(j)
print("Valores al cubo:",numeros_cubo)