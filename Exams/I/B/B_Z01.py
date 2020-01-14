import math

b = int(input())
c = int(input())
alfa = int(input())

a = math.sqrt(b ** 2 + c ** 2 - 2 * b * c * math.cos(math.radians(alfa)))

print(a)