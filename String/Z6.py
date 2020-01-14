x = input().lower()
while x.count(x[0]) < len(x):
    x = x.replace(x[0], '')
print(x)
