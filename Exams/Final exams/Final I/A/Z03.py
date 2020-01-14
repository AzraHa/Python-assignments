tekst = input()

najduzi = 0
for i in range(0, len(tekst)):
    duzina = 0
    j = i
    while(j < len(tekst) and tekst[j] == tekst[i]):
        duzina += 1
        j += 1
    if duzina > najduzi:
        najduzi = duzina

print(najduzi)      