def stepen(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    if b % 2 == 0:
        x = stepen(a, b/2)
        return  x * x

    if b % 2 == 1:
        x = stepen(a, b//2)
        return a * x * x

print(stepen(2, 200))
