"""Ejercicio4
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS
segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T
segundos. Escribir un algoritmo que determine la hora de llegada a la
ciudad B."""

horas = int(input("Introduce la hora de salida: "))
minutos = int(input("Introduce los minutos de salida: "))
segundos = int(input("Introduce los segundos de salida: "))
tiempo = int(input("\nIntroduce el tiempo total del viaje (tiempo en segundos): "))
horainicial = horas*3600 + minutos*60 + segundos
segundos_totales = horainicial + tiempo
t_horas = (segundos_totales//3600)
t_minutos =(segundos_totales%3600)//60
t_segundos = (segundos_totales%3600)%60
print("\nHora final del trayecto",t_horas,"horas,",t_minutos,"minutos y",t_segundos,"segundos.")