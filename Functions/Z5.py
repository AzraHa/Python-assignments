def fib(n):
    if n == 1 or n == 2:
        return 1

    predzadnji = 1
    zadnji = 1

    for i in range(3, n+1):
        stari_zadnji = zadnji
        zadnji = predzadnji + zadnji
        predzadnji = stari_zadnji

    return zadnji

x = int(input())
print(fib(x))
