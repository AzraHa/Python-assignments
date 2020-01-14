for i in range(10, 100):
    if i**2 < 1000 and i == i**2 % 100:
        print(i, i**2, sep='\n')