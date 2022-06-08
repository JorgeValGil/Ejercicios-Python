"""EJERCICIO 1
Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es
múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el
primero es múltiplo del segundo."""
def esMultiplo(numero1, numero2):
    if(numero1%numero2==0):
        print("El número",numero1,"es múltiplo del número",numero2)
    else:
        print("El número",numero1,"NO es múltiplo del ",numero2)

def pideNumeros():
    numero1 = int(input("Introduce un número:"))
    numero2 = int(input("Introduce otro número:"))
    esMultiplo(numero1, numero2)
    
pideNumeros()