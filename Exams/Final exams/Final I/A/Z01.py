for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            broj = a * 100 + b * 10 + c
            if broj == (a ** 3 + b ** 3 + c ** 3):
                print(broj, end=' ' )