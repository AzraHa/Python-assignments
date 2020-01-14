zbir = 0
while True:
    x = input()
    if len(x) != 1:
        break
    if x.isdigit():
        broj = int(x)
        if broj % 2 == 0:
            zbir += broj
print(zbir)
