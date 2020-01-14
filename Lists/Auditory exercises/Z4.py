n = int(input("Unesite n: "))

mat = []
for i in range(n):
    mat.append([])
    for j in range(n):
        x = int(input("Unesite broj: "))
        mat[i].append(x)

sumareda1 = 0
for j in range(n):
  sumareda1 += mat[0][j]

tmax = sumareda1

for i in range(n):
    sumared = 0
    for j in range(n):
        sumared += mat[i][j]

    if sumared > tmax:
        tmax = sumared

for i in range(n):
    sumakol = 0
    for j in range(n):
        sumakol += mat[j][i]

    if sumakol > tmax:
        tmax = sumakol

for i in range(n):
    for j in range(n):
        print(mat[i][j], end= " ")
    print()


print(tmax)
