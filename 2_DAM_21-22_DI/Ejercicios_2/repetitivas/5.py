"""Ejercicio5
Escribe un programa que diga si un número introducido por teclado es o no primo. Un número
primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la
raíz cuadrada del número para ver si es divisible por algún otro número"""
numero = int(input("Introduce un número:"))
count = 0
primo_dos = False
if numero > 1:
    if numero == 2:
        primo_dos = True
    else:
        for i in range(2,numero):
            if numero % i == 0:
                count +=1
else:
    print("El número no puede ser menor que 1")

if(primo_dos):
    print("El número es primo")
else:
    if(count > 0):
        print("El número no es primo")
    else:
        print("El número es primo")