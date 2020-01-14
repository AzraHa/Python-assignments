tekst1 = input()
tekst2 = tekst1.replace(' i ', ' I ')
print(tekst2)
for i in range(0, len(tekst2)):
    if tekst1[i] != tekst2[i]:
        print('-', end='')
    else:
        print(' ', end='')