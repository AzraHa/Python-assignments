n = int(input())
matrica = []
for i in range(0, n):
    red = []
    for j in range(0, n):
        red.append(int(input()))
    matrica.append(red)
suma1 = 0
suma2 = 0
for i in range(0, n):
    suma1 += matrica[i][i]
    suma2 += matrica[i][n - 1 - i]
print(suma1 * suma2)