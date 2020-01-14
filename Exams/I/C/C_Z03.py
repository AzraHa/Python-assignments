import random

n = int(input())

BROJ_SIM = 10000
broj_uspjeha = 0

for j in range(0, BROJ_SIM):
    broj_sestica = 0
    for i in range(0, 30):
        kockica = random.randint(1, 6)
        if kockica == 6:
            broj_sestica += 1
        else:
            broj_sestica = 0
        if broj_sestica >= n:
            broj_uspjeha += 1
            break

print(100 * broj_uspjeha / BROJ_SIM)