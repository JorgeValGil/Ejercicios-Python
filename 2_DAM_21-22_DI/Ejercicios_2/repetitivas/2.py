"""Ejercicio2
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de
todos los números introducidos."""
count = 0
total = 0
numero = 1
while (numero!=0):
    numero = int(input("Introduce un número:"))
    if(numero!=0):
        count+=1
        total+=numero
print("Numero de números introducidos antes que 0:",count)
print("Suma total:",total)
print("Media total:",total/count)