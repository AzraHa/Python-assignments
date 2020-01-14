n = int(input("Unesite dimenziju n: "))

mat = []
for i in range(n):
    niz = []
    for j in range(n):
        x = int(input("Unesite broj: "))
        niz.append(x)
    mat.append(niz)

tmax = mat[0][0]
for i in range(n):
    for j in range(n):
        if mat[i][j] > tmax:
            tmax = mat[i][j]

print(tmax)
