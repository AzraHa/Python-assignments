
n = float(input("Unesite broj: "))
l = []

while n != 0:
    i = len(l)

    while i > 0 and l[i-1] > n:
        i -= 1

    l.insert(i, n)
    n = float(input("Unesite broj: "))

print(l)
