l = []
while True:
    s = input()
    if s == '':
        break
    l.append(s)

for e in l:
    if e[0] != 'b':
        print(e, end=" ")
