"""Ejercicio3
Dadas dos variables numéricas A y B, que el usuario debe teclear, se
pide realizar un algoritmo que intercambie los valores de ambas
variables y muestre cuanto valen al final las dos variables."""

a = int(input("Introduce el valor de A: "))
b = int(input("Introduce el valor de B: "))
#c = a
#a = b
#b = c
a,b=b,a
print("El valor final de A es",a)
print("El valor final de B es",b)