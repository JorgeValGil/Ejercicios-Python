"""EJERCICIO 3
El día juliano correspondiente a una fecha es un número entero que indica los días que han
transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que
al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las
siguientes subrutinas:
 LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
 DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
 EsBisiesto: Recibe un año y nos dice si es bisiesto.
 Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano."""

import datetime

meses_30_dias = (4, 6, 9, 11)
meses_31_dias = (1, 3, 5, 7, 8, 10, 12)

def EsBisiesto(year):
    bisiesto = False
    if year % 4 == 0 and year % 100 !=0:
        bisiesto = True
    elif year % 400 == 0:
        bisiesto = True
    return bisiesto

def LeerFecha():
    dia = int(input("Introduce el día:"))
    mes = int(input("Introduce el mes:"))
    ano = int(input("Introduce el año:"))
    fecha = datetime.datetime(ano, mes, dia)
    return fecha

def DiasDelMes(mes,ano):
    dias = 0
    if mes in meses_30_dias:
        dias = 30
    elif mes in meses_31_dias:
        dias = 31
    else:
        bisiesto = EsBisiesto(ano)
    if bisiesto:
        dias = 29
    else:
        dias = 28    
    print("Mes",mes,"Año",ano,"tiene",dias,"dias")
    return dias

def Calcular_Dia_Juliano():
    fecha = LeerFecha()
    fecha_now = datetime.datetime.now()
    dias_totales=0
    for i in range(fecha.year, fecha_now.year+1):
        if i == fecha_now.year:
            for j in range(1,fecha_now.month+1):
                if j == fecha_now.month:
                    dias_totales += fecha_now.day
                    print("Mes",j,"Año",i,"tiene",fecha_now.day,"dias")
                else:
                    dias_totales += DiasDelMes(j,i)
        else:
            for j in range(1,13):
                dias_totales += DiasDelMes(j,i)
    print("Días totales:",dias_totales)
    
Calcular_Dia_Juliano()