l1 = []
l2 = []
l3 = []
for i in range(0, 10):
    n = int(input())
    if n < 0:
        l1.append(n)
    elif n == 0:
        l2.append(n)
    else:
        l3.append(n)
for e in l1:
    print(e, end=' ')
for e in l2:
    print(e, end=' ')
for e in l3:
    print(e, end=' ')