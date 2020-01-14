rijec = input().lower()
samoglasnici = "aeiou"
pozicija = 0
for i in range(1, len(rijec)):
    if rijec[i] in samoglasnici and pozicija == 0:
        pozicija = i
print(rijec[pozicija+1:] + rijec[:pozicija+1])
