#Dado o DNI do alumno e 4 notas do mesmo, imprime o DNI e o promedio das súas cualificacións
print("Introduce o DNI:")
dni=input()
print("Escribe a nota do primeiro exame:")
a = float(input())
print("Escribe a nota do segundo exame:")
b = float(input())
print("Escribe a nota do terceiro exame:")
c = float(input())
print("Escribe a nota do cuarto exame:")
d = float(input())
print("DNI:",dni)
media = (a+b+c+d)/4
print("Nota media",media)