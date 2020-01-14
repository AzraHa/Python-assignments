f = open('snijeg.in', 'r')

mat = []
while True:
    x = f.readline().rstrip('\n')
    if x == '':
        break
    m = []
    for i in range(0, len(x), 2):
        m.append(x[i])
    mat.append(m)

redova = len(mat)
kolona = len(mat[0])

for j in range(kolona):
    pahuljica = 0

    for i in range(redova):
        if mat[i][j] == '*':
            mat[i][j] = '-'
            pahuljica += 1
        if mat[i][j] == '#':
            for k in range(pahuljica):
                mat[i-k-1][j] = '*'
            break
        if i == redova-1:
            for k in range(pahuljica):
                mat[i-k][j] = '*'



for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print()
