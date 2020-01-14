n = int(input("Dim: "))
suma = 1

for i in range(3, n+1, 2):
    suma += i ** 2
    suma += i ** 2 - (i-1)
    suma += i ** 2 - 2*(i-1)
    suma += i ** 2 - 3*(i-1)

print(suma)
