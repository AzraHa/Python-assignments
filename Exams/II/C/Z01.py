n = int(input())
lista = []
for i in range(0, n):
    lista.append(int(input()))
m = int(input())
lista.sort()
lista2 = lista[m:len(lista)-m]
for e in lista2:
    print(e, end=" ")