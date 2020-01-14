import string
znakovi = string.punctuation
s = input().lower()

for z in znakovi:
    s = s.replace(z, '')

l = s.split()
for e in l:
    if e[0] == e[len(e)-1]:
        print(e)
