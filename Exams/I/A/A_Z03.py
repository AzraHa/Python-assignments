import random

BROJ_SIM = 10000

ulog = int(input())
opklada = int(input())
cilj = int(input())

broj_pobjeda = 0
for s in range(BROJ_SIM):
    novac = ulog
    while novac > 0 and novac < cilj:
        if random.randrange(0, 100) < 49:
            novac += opklada
        else:
            novac -= opklada
    if novac >= cilj:
        broj_pobjeda += 1

print(broj_pobjeda/BROJ_SIM)