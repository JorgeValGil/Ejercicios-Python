"""Ejercicio1
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""

import math
cateto1 = int(input("Introduce el valor del primer cateto:"))
cateto2 = int(input("Introduce el valor del segundo cateto:"))
hipotenusa = math.sqrt(math.pow(cateto1,2)+math.pow(cateto2,2))
print("El valor de la hipotenusa es " + str(hipotenusa))