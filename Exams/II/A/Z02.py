n = int(input())
lista = list()
for i in range(0, n):
    lista.append(int(input()))

lista2 = list(lista)
lista2.sort()
lista.remove(lista2[n//2])

for element in lista:
    print(element, end=' ')