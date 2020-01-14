s1 = input().lower()
s2 = input().lower()

su_anagrami = True
for ch in s1:
    if ch.isalpha() and s1.count(ch) != s2.count(ch):
        su_anagrami = False

if su_anagrami:
    print('Anagrami')
else:
    print('Nisu anagrami')