s = 'a'

rez = ''
rezp = ''

if s == 'i':
    print("I")
    print("-")
else:
    for i in range(len(s)):
        if i == 0 and s[0] == 'i' and s[1] == ' ':
            rez += 'I'
            rezp += '-'
        elif i > 0 and i < len(s)-1 and \
            s[i] == 'i' and s[i-1] == ' ' \
                and s[i+1] == ' ':
            rez += 'I'
            rezp += '-'
        elif i == len(s)-1 and s[i] == 'i' and s[i-1] == ' ':
            rez += 'I'
            rezp += '-'
        else:
            rez += s[i]
            rezp += ' '


    print(rez)
    print(rezp)
