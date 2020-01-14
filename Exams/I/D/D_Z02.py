n = int(input())

for i in range(0, n):
    for j in range(0, n):
        print((i + j) % n + 1, end=' ')
    print()