def ispisi_najveci_broj(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            x = str(l[i])
            y = str(l[j])
            for k in range(max(len(x), len(y))):
                if x[k%len(x)] < y[k%len(y)]:
                    l[i], l[j] = l[j], l[i]
                    break
                if x[k%len(x)] > y[k%len(y)]:
                    break

l = [2, 21, 3, 12342, 4, 45, 41]
ispisi_najveci_broj(l)
print(l)
