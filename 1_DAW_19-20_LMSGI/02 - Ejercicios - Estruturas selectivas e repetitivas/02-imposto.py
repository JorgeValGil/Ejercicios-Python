# Criterios dos impostos:
# Se a persoa non cobraba máis de 85528 thalers, o imposto era o 18% das ganancias menos 556,02 thalers.
# Se as ganancias eran maiores, o imposto era 14839,02 thalers sumados a un 32% do exceso das ganancias por riba dos 85528 thalers.
# Debe aceptar un valor real e amosar o cálculo do imposto sen decimais. 
# O goberno deste país nunca devolve cartos aos seus habitantes, polo que se o valor do imposto é negativo, deberá indicar 0
print("Introduce as ganancias:")
ganancias = float(input())
impostos = 0
LIMITE = 85528
if ganancias > 0:
    if ganancias < LIMITE:
        impostos = (ganancias * 0.18) - 556.02
    else:
        exceso = (ganancias - LIMITE) * 0.32
        impostos = exceso + 14839.02
if impostos < 0:
    impostos = 0
print("Impostos:", round(impostos))
