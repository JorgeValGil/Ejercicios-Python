#Número máxico:
#Debe preguntar un número ata que se acerte o correcto.
#Se o campión non acerta, o programa devolve “Hahaha, estás atrapado no meu bucle”
#Se o campión acerta, o programa devolve “Ben feito” Eres libre!”

maxico = 11
print("Introduce o número máxico:")
proba = int(input())
while proba != maxico:
    print("Hahaha, estás atrapado no meu bucle")
    print("Introduce o número máxico:")
    proba = int(input())
print("Ben feito. Eres libre!")
