"""Ejercicio2
Un alumno desea saber cual será su calificación final en la materia de
Matemáticas. Dicha calificación se compone de los siguientes
porcentajes:
• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final."""

parcial1 = float(input("Introduce la nota del primer parcial:"))
parcial2 = float(input("Introduce la nota del segundo parcial:"))
parcial3 = float(input("Introduce la nota del tercer parcial:"))
nota_final = float(input("Introduce la nota del examen final:"))
trabajo_final = float(input("Introduce la nota del trabajo final:"))
nota = (((parcial1+parcial2+parcial3)/3) * 0.55) + (nota_final * 0.3) + (nota_final * 0.15)
print("La nota final es de",round(nota,2))