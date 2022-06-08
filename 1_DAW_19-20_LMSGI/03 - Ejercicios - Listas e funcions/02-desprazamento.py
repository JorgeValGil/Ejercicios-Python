# Mova as palabras da lista anterior unha posición cara a adiante (emprega a mesma variable). 
# Por exemplo, a lista [2, 4, 6, 8, 10] pasa a ser [10, 2, 4, 6, 8]
def despraza(lista):
    nova = []
    for i in range(0, len(lista)):
        nova.append(lista[(i-1)%len(lista)])
    return nova

def despraza_v2(lista):
    lista.insert(0,lista[-1])
    del(lista[-1])
    return lista

l = [1,2,3,4]
print(despraza(l))
print(despraza_v2(l))
