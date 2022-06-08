"""Ejercicio 2
Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena."""
cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")
count = 0
if caracter.isalpha and len(caracter) == 1:
    for i in cadena:
        if i == caracter:
            count+=1

if(count!=0):
    print("El caracter",caracter,"aparecer en la cadena",cadena,",",count,"veces.")
else:
    print("El caracter",caracter,"NO aparece en la cadena",cadena)