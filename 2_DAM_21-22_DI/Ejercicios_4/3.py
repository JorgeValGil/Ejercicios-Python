"""Ejercicio3
Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
 Todos los alumnos mayores de edad.
 Los alumnos mayores (los que tienen más edad)"""
nombres = []
edades = []

nombre = ""

while (nombre!="*"):
    print("\nCREACIÓN DE ALUMNO\n")
    nombre = input("Introduce el nombre: ")
    if(nombre!="*"):
        nombres.append(nombre)
        edad = int(input("Introduce una edad:"))
        edades.append(edad)
else:
    print("Introducido caracter especial. Final del proceso de creación de alumnos")

print("\nAlumnos mayores de edad:\n")
for nombre,edad in zip(nombres,edades):
    if(edad>=18):
        print("Nombre:",nombre,"- Edad:",edad)

for i in range(len(edades)):
    if(edades[i]==max(edades)):
        print("Alumno mayor:",nombres[i],"- Edad:",max(edades))