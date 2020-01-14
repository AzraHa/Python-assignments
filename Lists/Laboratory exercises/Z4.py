from math import inf

def vrati_maksimum(l):
    trenutni_maksimum = -inf
    for x in l:
        if x > trenutni_maksimum:
            trenutni_maksimum = x
    return trenutni_maksimum


def vrati_broj_pojavljivanja(l, n):
    brojac = 0
    for x in l:
        if x == n:
            brojac += 1
    return brojac


l = [1, -2, -6, 1, 8, 8,0]
m = vrati_maksimum(l)
print(vrati_broj_pojavljivanja(l, m))
