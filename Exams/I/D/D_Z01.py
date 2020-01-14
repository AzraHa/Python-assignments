import math

x = int(input())
y = int(input())

r = math.sqrt(x**2 + y**2)
phi = math.degrees(math.atan2(y, x))

print(r)
print(phi)