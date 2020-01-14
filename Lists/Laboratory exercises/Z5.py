
def vrati_broj_pojavljivanja(l, n):
    brojac = 0
    for x in l:
        if x == n:
            brojac += 1
    return brojac


def vrati_maksimum_po_broju_pojavljivanja(l):
    trenutni_maksimum = None
    trenutni_maks_br_p = 0

    for x in l:
        broj_pojavljivanja_x = vrati_broj_pojavljivanja(l, x)

        if broj_pojavljivanja_x > trenutni_maks_br_p:
            trenutni_maksimum = x
            trenutni_maks_br_p = broj_pojavljivanja_x

    return trenutni_maksimum


l = [1, 9, -2, 1, 9]
print(vrati_maksimum_po_broju_pojavljivanja(l))
