"""Ejercicio 3
Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene."""
cadena = input("Introduce una cadena: ")
cadena_split = cadena.split(" ")
cadena_split_len = len(cadena_split)
print("En la cadena",cadena, "hay",cadena_split_len,"palabras")