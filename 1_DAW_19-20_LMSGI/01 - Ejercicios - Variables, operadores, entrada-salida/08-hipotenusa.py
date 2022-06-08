#Calcule a hipotenusa dun triángulo rectángulo a partir do seus catetos
import math

print("Introduce o valor de A:")
a = int(input())
print("Introduce o valor de B:")
b = int(input())
hipotenusa=math.sqrt(a**2+b**2)
hipo2=(a**2+b**2)**0.5
print("Hipotenusa:",hipotenusa,hipo2)