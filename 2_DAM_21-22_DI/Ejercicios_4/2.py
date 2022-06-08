"""Ejercicio2
Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación, debe mostrar: todas las notas, la nota media, la nota más alta que ha sacado y la menor."""
notas = []
intentos = 0
while (intentos<5):
    nota = float(input("Introduce una nota: (Entre 0 y 10)"))
    if nota>=0 and nota <=10:
        notas.append(nota)
        intentos+=1

sumatotal = 0
for i in notas:
    sumatotal+=i

print("\nNotas:",notas)
print("Media:",sumatotal/len(notas))
print("Nota más baja:",min(notas))
print("Nota más alta:",max(notas))