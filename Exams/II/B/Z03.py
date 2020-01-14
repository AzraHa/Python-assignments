fajl = open('test01.in', 'r')
linija = fajl.readline()
lista = linija.split()
r = int(lista[0])
c = int(lista[1])
matrica = []
for i in range(0, r):
    red = []
    for j in range(0, c):
        red.append(' ')
    matrica.append(red)

linija = fajl.readline()
while linija != '':
    (red, kolona, znak) = linija.split()
    red = int(red.strip('(,'))
    kolona = int(kolona.strip(')'))
    matrica[red][kolona] = znak
    linija = fajl.readline()

for i in range(0, r):
    for j in range(0, c):
        print(matrica[i][j], end='')
    print()