def vrati_srednji_element(lista):
    if len(lista) % 2 == 0:
        return "NOPE"

    lista.sort()
    return lista[len(lista)//2]

lista = [4, 3, 1, 2, 5]
print(lista)
#lista.sort()
#print(lista)
print(vrati_srednji_element(lista))
