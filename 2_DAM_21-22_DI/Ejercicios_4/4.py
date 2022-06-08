"""Ejercicio4
Diseñar el algoritmo correspondiente a un programa, que:
 Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
 Carga la tabla con valores numéricos enteros.
 Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla."""
import random
x=5
y=5
lista = [[0 for i in range(x)] for j in range(y)]

for i in range(len(lista)):
    for j in range(len(lista[i])):
        number = random.randrange(0,101)
        lista[i][j] = number

for i in range(len(lista)):
    fila_texto = ""
    for j in range(len(lista[i])):
        fila_texto += str(lista[i][j])+ " "
    print(fila_texto)

for i in range(len(lista)):
    fila = 0
    columna = 0
    for j in range(len(lista[i])):
        fila += lista[i][j]
        columna += lista[j][i]
print("Fila",i,"=",fila)
print("Columna",i,"=",columna)