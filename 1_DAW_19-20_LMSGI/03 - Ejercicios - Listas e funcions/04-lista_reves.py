#Crea unha función que tome unha lista e a devolva do revés.
def lista_inversa(lista):
    lista_reves = []
    for i in lista:
        lista_reves.insert(0, i)
        print("i:", i)
        print("Lista reves:", lista_reves)
    return lista_reves

lista = [1,2,3,4]
print(lista_inversa(lista))