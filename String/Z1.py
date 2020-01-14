def analiza_stringa(s):
    br_malih_slova = 0
    br_velikih_slova = 0
    br_cifara = 0
    br_space = 0

    for ch in s:
        if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            br_velikih_slova += 1
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            br_malih_slova += 1
        if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
            br_cifara += 1
        if ch == ' ':
            br_space += 1

        print("Broj velikih slova", br_velikih_slova)
        print("Broj malih slova", br_malih_slova)
        print("Broj cifara", br_cifara)
        print("Broj space-ova", br_space)


analiza_stringa("StrinGovi 1")
