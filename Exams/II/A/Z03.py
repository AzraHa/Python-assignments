fajl = open('test01.in', 'r')
sekvenca = fajl.read()
najduza = ""
duzina = 0
indeks1 = sekvenca.find('AGGT')
while indeks1 != -1:
    sekvenca = sekvenca[indeks1+4:]
    indeks2 = sekvenca.find('AGGT')
    if indeks2 != -1:
        podsekvenca = sekvenca[:indeks2]
        if len(podsekvenca) > duzina:
            duzina = len(podsekvenca)
            najduza = podsekvenca
    indeks1 = indeks2
print(najduza)