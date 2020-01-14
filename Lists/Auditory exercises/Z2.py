lista = []

while True:
    x = int(input("Unesi broj: "))
    if x == 0:
        break

    lista.append(x)

for e in lista:
    if e < 0:
        print(e, end=" ")
for e in lista:
    if e > 0:
        print(e, end=" ")
