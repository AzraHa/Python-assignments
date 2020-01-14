def S(n):
    if n == 1:
        return 1
    return n**2 + S(n-1)

print(S(4))
