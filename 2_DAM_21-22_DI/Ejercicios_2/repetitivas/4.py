"""Ejercicio4
Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5."""
tablas = (1, 2, 3, 4, 5)
for i in tablas:
    print("\nTabla del",i)
    for j in range(11):
        print(i,"*",j," = ",i*j)