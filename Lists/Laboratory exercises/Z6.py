
def da_li_postoji(l, n):
    for x in l:
        if x == n:
            return True
    return False


def vrati_jedinstvene(l):
    jedinstveni = []

    for x in l:
        if not da_li_postoji(jedinstveni, x):
            jedinstveni.append(x)

    return jedinstveni


def vrati_razliku_max_i_nti_max(l, n):
    jedinstveni = vrati_jedinstvene(l)
    jedinstveni.sort(reverse=True)
    return jedinstveni[0] - jedinstveni[n-1]


unos = input('Unesite brojeve razdvojene praznim mjestom: ')
n = int(input('Unesite n: '))
lista = unos.split()

l = []
for x in lista:
    l.append(int(x))

print(vrati_razliku_max_i_nti_max(l, n))
