lista = []

while True:
    x = int(input("Unesi broj: "))

    if x == 100:
        break

    lista.append(x)

#print(lista)
for e in lista:
    print(e)

print("----")

for i in range(len(lista)):
    print(lista[len(lista)-1-i])

print("----")

for i in range(len(lista)-1, -1, -1):
    print(lista[i])

print("----")

lista.reverse()
for i in range(len(lista)):
    print(lista[i])
