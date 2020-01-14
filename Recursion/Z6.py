def najveci(lista):
    if len(lista) == 1:
        return lista[0]

    zadnji = lista[len(lista)-1]
    novaLista = lista[0:len(lista)-1]
    odostalihnajveci = najveci(novaLista)
    if zadnji > odostalihnajveci:
        return zadnji
    else:
        return odostalihnajveci

print(najveci([8, 123, 6,9,55,3,16,4,27,17,2228]))

#l = [8, 6,9,55,3,16,4,27,17,-8]
#print(l[0: len(l)-2])
