# S(n)= 1**2 + 2**2 + 3**2 + ... + n**2
# S(1) = 1
# S(n) =  S(n-1) + n**2

def S(n):
    if n == 1:
        return 1
    return n**2 + S(n-1)

print(S(4))
