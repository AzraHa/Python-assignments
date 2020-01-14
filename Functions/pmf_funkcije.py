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

def vrati_faktorijel(n):
    rez = 1
    for i in range(1, n+1):
        rez *= i
    return rez
