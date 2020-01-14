f = open('sifre.in', 'r')

while True:
    x = f.readline()
    if x == '':
        break

    lista = x.split()
    username = lista[0]
    pwd = lista[1]

    if username == pwd:
        print(username, pwd)
    elif len(pwd) < 5:
        print(username, pwd)
    elif "1234" in pwd:
        print(username, pwd)
