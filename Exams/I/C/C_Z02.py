n = int(input())

while n > 9:
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    n = result

print(result)