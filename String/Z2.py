def promijeni_slova(s):
    rs = ""

    for ch in s:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            rs += chr(ord(ch)+ord('A') - ord('a'))
        elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            rs += chr(ord(ch)-(ord('A') - ord('a')))
        else:
            rs += ch
    return rs

print(promijeni_slova("Danas je PONEDJELJAK."))
