#Crea un programa comedor de vogais. Pide unha palabra ao usuario e a devolve sen vogais. 
# Por exemplo, para a palabra morcego, devolve:
# M
# R
# C
# G
print("Introduce unha palabra:")
palabra = input()
vocais = ['a','A','e','E','i','I','o','O','u','U']
for letra in palabra:
	if letra not in vocais:
		print(letra)