"""Ejercicio2
Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe”
y “asdasd” se indica “Has entrado al sistema”, sino se da un error"""
nombre = input("Introduce el nombre de usuario: ")
contrasena = input("Introduce la contraseña: ")
if nombre=="pepe" and contrasena=="asdasd":
    print("Has entrado al sistema")
else:
    print("Error, datos incorrectos")