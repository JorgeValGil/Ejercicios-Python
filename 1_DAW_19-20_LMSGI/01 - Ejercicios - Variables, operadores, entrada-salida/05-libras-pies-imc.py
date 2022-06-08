# Dado o nome dunha persoa e o seu peso e altura en kg e cm, 
# imprime o seu peso en libras, a súa altura en pés e o seu IMC (peso/altura²)
print("Introduce o nome:")
nome = input()
print("Introduce os apelidos:")
apelidos = input()
print("Introduce o peso(kg):")
peso = float(input())
print("Escribe a altura(cm):")
altura = int(input())
pesolibras = peso * 2.205
alturam= altura / 100
alturapes = ( alturam ) * 3.281
imc = peso / ( alturam ** 2)
print(nome, apelidos,"pesa",round(pesolibras,2),"libras, mide",round(alturapes,2),"pes e ten",round(imc,2),"de IMC.")