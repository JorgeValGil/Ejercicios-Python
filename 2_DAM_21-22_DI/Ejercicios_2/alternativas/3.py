"""Ejercicio3
Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
numero1 ="""
numero1 = int(input("Introduce el primer número:"))
numero2 = int(input("Introduce el segundo número:"))
numero3 = int(input("Introduce el tercer número:"))
numeros =(numero1,numero2,numero3)
print("Números ordenados de mayor a menor",sorted(numeros, reverse=True))