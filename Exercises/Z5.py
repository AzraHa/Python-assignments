s1 = "Krasan je odmor!"
s2 = "Jadransko morez"

s1 = s1.lower()
s2 = s2.lower()

anagram = True
for z in s1:
    if z.isalpha() and s1.count(z) != s2.count(z):
        anagram = False

for z in s2:
    if z.isalpha() and s1.count(z) != s2.count(z):
        anagram = False

if anagram:
    print("Jesu anagrami")
else:
    print("Nisu anagrami")
