# A partir da hora de comezo dun evento e a súa duración (3 valores: hora, minutos, duración en minutos)
# calcula a hora de finalización do evento. Non te preocupes dos erros que poida introducir o usuario (hora inválida).

print("Introduce a hora de comezo:")
hora = int(input())
print("Intoduce os minutos de comezo:")
minuto = int(input())
print("Intoduce a duración en minutos:")
duracion = int(input())
hora_suma = (minuto + duracion) // 60 
hora_final = hora + hora_suma
while hora_final >= 24:
    hora_final = hora_final - 24
minuto_suma = (minuto + duracion) % 60
print("O evento finalizará as", hora_final,":",minuto_suma)
