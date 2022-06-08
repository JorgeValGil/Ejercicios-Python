"""Ejercicio1
Algoritmo que pida un número y diga si es positivo, negativo o 0"""
numero = float(input("Introduce un número:"))
if numero<0:
    print('El número introducido es negativo')
elif numero>0:
    print('El número introducido es positivo')
else:
    print('El número introducido es 0')