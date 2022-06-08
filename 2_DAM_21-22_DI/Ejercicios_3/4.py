"""Ejercicio 4
Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado."""
cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")
subcadena_in = subcadena in cadena
if(subcadena_in):
    print("La subcadena",subcadena, "se encuentra dentro de la cadena",cadena)
else:
    print("La subcadena",subcadena, "no se encuentra dentro de la cadena",cadena)
    
#subcadena_find = cadena.find(subcadena)
#if(subcadena_find != -1):
# print("La subcadena",subcadena, "se encuentra dentro de la cadena",cadena)
#else:
# print("La subcadena",subcadena, "no se encuentra dentro de la cadena",cadena)