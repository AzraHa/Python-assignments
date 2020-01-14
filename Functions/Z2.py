def ispisi_faktorijel(n):
    rez = 1
    for i in range(1, n+1):
        rez *= i
    print(rez)

def vrati_faktorijel(n):
    rez = 1
    for i in range(1, n+1):
        rez *= i
    return rez
    #print("Evo me")

ispisi_faktorijel(5)
x = vrati_faktorijel(5)
print(x)
