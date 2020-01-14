from random import randint


def da_li_postoji(l, n):
    for x in l:
        if x == n:
            return True
    return False


def popuni_random(a, b):
    l = []

    while len(l) < 10:
        n = randint(a, b)
        if not da_li_postoji(l, n):
            l.append(n)

    return l


print(popuni_random(1, 10))
print(popuni_random(1, 10))
print(popuni_random(1, 10))
print(popuni_random(1, 10))
