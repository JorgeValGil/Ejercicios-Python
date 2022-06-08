# Pida palabras ao usuario ata que este escriba 0 e meta esas palabras nunha lista
lista = []
palabra = input("Escribe unha palabra, 0 para rematar:")
while palabra != "0":
    lista.append(palabra)
    palabra = input("Escribe unha palabra, 0 para rematar:")
print(lista)