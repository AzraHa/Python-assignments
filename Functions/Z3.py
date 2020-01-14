def vrati_stepen(a, b):
    if b >= 1:
        rez = 1
        for i in range(1, b+1):
            rez *= a
        return rez
    elif b == 0:
        return 1
    else:
        b = -b
        rez = 1
        for i in range(1, b+1):
            rez *= a
        return 1.0/rez

print(vrati_stepen(2,4))
print(vrati_stepen(2,-2))
