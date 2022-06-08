"""Ejercicio4
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta."""
def ano_bisiesto(year):
    bisiesto = False
    if year % 4 == 0 and year % 100 !=0:
        bisiesto = True
    elif year % 400 == 0:
        bisiesto = True

meses_30_dias = (4, 6, 9, 11)
meses_31_dias = (1, 3, 5, 7, 8, 10, 12)

dia = int(input("Introduce el día:"))
mes = int(input("Introduce el mes:"))
ano = int(input("Introduce el año:"))

fecha_correcta = False
if dia>0 and mes>0 and ano>0:
    if mes!=2 and mes <=12:
        for i in meses_30_dias:
            if mes == i:
                if dia <=30:
                    fecha_correcta = True
        for i in meses_31_dias:
            if mes == i:
                if dia <=31:
                    fecha_correcta = True
    else:
        bisiesto = ano_bisiesto(ano)
        if bisiesto:
            if dia <=29:
                fecha_correcta = True
            else:
                if dia <=28:
                    fecha_correcta = True
if fecha_correcta:
    print("La fecha introducida es correcta.")
else:
    print("La fecha introducida NO es correcta.")