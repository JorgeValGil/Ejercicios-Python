#Crea unha función que indique se un ano é ou non bisesto.
def bisesto(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 100:
        return True
    elif ano % 400 != 0:
        return True
    else:
        return True

ano = int(input("Escribe o ano:"))
print(bisesto(ano))