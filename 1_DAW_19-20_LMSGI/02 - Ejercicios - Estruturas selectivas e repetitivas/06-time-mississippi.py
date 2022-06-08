# Crea un programa que conte ata 5 en segundos e, cando acabe, amose a mensaxe “Vou!”. 
# O resultado será o seguinte:
# 1 Mississippi
# 2 Mississippi
# 3 Mississippi
# 4 Mississippi
# 5 Mississippi
# Vou!
# Emprega a función time.sleep() para esperar un segundo.

import time
for i in range(1,6):
    print(i,"Mississippi")
    time.sleep(1)
print("Vou!")