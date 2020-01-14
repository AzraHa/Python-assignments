import pmf_funkcije as pmf

def f(x, y):
    if x < -5:
        return x+y

    if x < 0:
        return pmf.vrati_stepen(x, y)

    if x < 10:
        return pmf.vrati_stepen(x, pmf.vrati_stepen(y, x))

    if x < 15:
        return pmf.vrati_faktorijel(x)

    return 0

print(f(2,5))
