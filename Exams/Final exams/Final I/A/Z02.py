n = int(input())
lista = [0]*n
for i in range(0, n*n):
    print(lista)
    m = int(input())
    lista[i%n] += m

#for i in range(0, n):
#    print(lista[i])
