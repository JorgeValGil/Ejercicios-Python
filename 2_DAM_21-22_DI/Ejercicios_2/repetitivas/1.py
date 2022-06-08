"""Ejercicio1
Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el
producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de
un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)"""
import math
numero = int(input("Introduce un número: "))
#print("Factorial de",numero,"es:",math.factorial(numero))
factorial = 1
texto = ""
for i in range(1,numero+1):
    factorial*=i
    if(i==(numero)):
        texto_actual=str(i)
    else:
        texto_actual=str(i)+" * "
    texto+=texto_actual
    
print(str(numero)+"! = "+str(texto)+" = "+str(factorial))