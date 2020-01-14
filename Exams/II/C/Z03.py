fajl = open('test01.in', 'r')
mr = {0:'Januar', 1:'Februar', 2:'Mart', 3:'April', 4:'Maj', 5:'Juni', 6:'Juli', 7:'August', 8:'Septembar', 9:'Oktobar', 10:'Novembar', 11:'Decembar'}

godine = []
for line in fajl:
    lista = line.split()
    mjeseci = []
    for mjesec in lista:
        mjeseci.append(float(mjesec))
    godine.append(mjeseci)

prosjecne = []
for i in range(0, 12):
    suma = 0
    for j in range(0, 5):
        suma += godine[j][i]
    prosjecne.append(suma/5)
    print(suma/5, end=' ')

print()
print(mr[prosjecne.index(max(prosjecne))])
print(mr[prosjecne.index(min(prosjecne))])