# Crea un programa que pregunte ao usuario cal é a súa serie favorita e responda o seguinte, segundo a contestación do usuario:
# Se o usuario contesta “Game of Thrones” o ordenador responderá: “Por suposto, Game of Thrones é a mellor serie da historia!”
# Se o usuario responde “Xogo de Tronos” ou “Juego de Tronos” o ordenador responderá: “Non se di <entrada>, dise Game of Thrones”
# En caso contrario, responderá: “Non, a mellor é Game of Thrones!”
print("Escribe o nome da túa serie favorita:")
serie = input()
minusculas = serie.lower()
if minusculas == "game of thrones":
    print("Por suposto, Game of Thrones é a mellor serie da historia!")
elif minusculas == "xogo de tronos" or minusculas == "juego de tronos":
    print("Non se di ", serie,", dise Game of Thrones", sep="")
else:
    print("Non, a mellor é Game of Thrones!")
    