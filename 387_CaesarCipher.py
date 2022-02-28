import string
alphabet = string.ascii_lowercase

def warmup(letter, shift):
    value = (ord(letter)-97)+shift
    if value > 25:
        value -= 26
    output = alphabet[value]
    return output

def caesar(string, shift):
    shifted = ''
    for letter in string:
        value = (ord(letter)-97)+shift
        if value > 25:
            value -= 26
        output = alphabet[value]
        shifted += output
    return shifted

print(caesar('a', 1))
print(caesar('abcz', 1))
print(caesar('irk', 13))
print(caesar('fusion', 6))
print(caesar('dailyprogrammer', 6))
print(caesar('jgorevxumxgsskx', 20))

