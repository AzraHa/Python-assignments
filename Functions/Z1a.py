import random

def ispisiSlucajanBroj(od=1, do=100):
    print(random.randint(od, do))

def vratiSlucajanBroj(od=1, do=100):
    x = random.randint(od, do)
    return x




x = vratiSlucajanBroj(1, 10)
print(x+2)
