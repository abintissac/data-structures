def replace_alphabet(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    result = ''
    for c in s:
        if c.isalpha():
            index = alphabet.index(c)
            result += alphabet[(index+n)%26]
        else:
            result += c
    return result
s = 'Hello, world!'
n = 3
print(replace_alphabet(s, n))
