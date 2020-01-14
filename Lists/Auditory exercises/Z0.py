def f(x):
    x = 10

def f2(lista):
    lista2 = lista.copy()
    lista2[0] = 10

x = 5
f(x)
print(x)

lista = [1, 2, 3, 4]
f2(lista)
print(lista)
