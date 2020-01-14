unos = input().lower()
rijeci = unos.split()

for rijec in rijeci:
    s = ""
    for slovo in rijec:
        if slovo != 'a' and slovo != 'e' \
            and slovo != 'i' and slovo != 'o' \
            and slovo != 'u':
            s += slovo
    print(s)
