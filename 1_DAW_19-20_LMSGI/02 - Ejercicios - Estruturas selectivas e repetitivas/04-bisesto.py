#Fai unha calculadora de anos bisestos. 
# Para saber se un ano é bisesto, aplícanse as seguintes regras:
# Se o ano non é divisible entre catro, non é bisesto.
# En caso contrario, se o ano non é divisible entre 100, é bisesto.
# En caso contrario, se o ano non é divisible entre 400, non é bisesto.
# En caso contrario, é bisesto.

print("Introduce a ano:")
ano = int(input())
if ano % 4 != 0:
    print("Non é bisiesto")
elif ano % 100 != 0:
    print("É bisiesto")
elif ano % 400 != 0:
    print("Non é bisiesto")
else:
    print("É bisiesto")