"""Ejercicio 1
Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado."""
cadena = "hola, chámome Jorge"
cadena_teclado = input("Introduce una cadena: ")
if cadena.startswith(cadena_teclado):
    print("Acierto! La cadena",cadena,"empieza por",cadena_teclado)
else:
    print("Error! La cadena",cadena,"no empieza por",cadena_teclado)