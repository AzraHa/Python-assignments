import random

BROJ_SIM = 10000000
broj_ostrougli = 0

for i in range(0, BROJ_SIM):
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = random.randint(1, 1000)

    ostrougli = True
    if(a + b <= c or a + c <= b or b + c <= a):
        ostrougli = False
    if(a**2 + b**2 <= c**2 or a**2 + c**2 <= b**2 or b**2 + c**2 <= a**2):
        ostrougli = False
    if ostrougli:
        broj_ostrougli += 1

print(100.0 * broj_ostrougli / BROJ_SIM)