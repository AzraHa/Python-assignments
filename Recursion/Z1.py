def hanoi(n, a, b, c):
    if n == 1:
        print("Prebacujem disk sa", a, "na", c)
        return
    #prebacujemo n-1, a, c, b
    hanoi(n-1, a, c, b)
    # prebacujemo 1, a, b, c
    hanoi(1, a, b, c)
    # prebacujem n-1, b, a, c
    hanoi(n-1, b, a, c)

hanoi(20, '1', '2', '3')
