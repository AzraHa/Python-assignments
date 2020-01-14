r1 = input().lower()
r2 = input().lower()
s1 = set()
s2 = set()
for slovo in r1:
    s1.add(slovo)
for slovo in r2:
    s2.add(slovo)
razlika = s1-s2
print(len(razlika))