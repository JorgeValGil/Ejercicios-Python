# Crea unha calculadora do mundo máxico de Harry Potter, que convirta galeóns, sickels e knuts.
# Debe ofrecer inicialmente un menú no que se indiquen as seguintes opcións:
# 1. Conversión de galeóns a sickels.
# 2. Conversión de galeóns a knuts.
# 3. Conversión de sickles a knuts.
# 4. Conversión de knuts a galeóns, sickles e knuts.
# Recorda que:
# 1 galeón = 17 sickles
# 1 sickle = 29 knuts

print("Selecciona a opción (introducir o número da opción):")
print("1. Conversión de galeóns a sickels.")
print("2. Conversión de galeóns a knuts.")
print("3. Conversión de sickels a knuts.")
print("4. Conversión de knuts a galeóns, sickles e knuts.")
opcion = int(input())
print("Introduce a cantidade:")
cantidade = int(input())
if opcion == 1:
    resultado = cantidade * 17
    print("Resultado:", resultado,"sickels")
elif opcion == 2:
    resultado = cantidade * 17 * 29
    print("Resultado:", resultado,"knuts")
elif opcion == 3:
    resultado = cantidade * 29
    print("Resultado:", resultado,"knuts")
elif opcion == 4:
    knuts = cantidade%29
    sickels = (cantidade//29)%17
    galeones = cantidade//29//17
    print("Tus knuts equivalen a",galeones,"galeones", sickels, "sickels e ", knuts,"knuts")
else:
    print("Introduce un número entre o 1 e o 4")