
def je_li_rastuca2(l):
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            return False
    return True


def je_li_rastuca(l):
    i = 1
    while i < len(l) and l[i] > l[i-1]:
        i += 1
    if i == len(l):
        return True
    else:
        return False


l = [1,1, 4, 10, 12, 17]
print(je_li_rastuca(l))
print(je_li_rastuca2(l))
