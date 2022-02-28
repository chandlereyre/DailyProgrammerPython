alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate_sums(items):
    listsum = {}
    i = 1
    for item in items:
        listsum[item] = i
        i += 1
    return listsum

def lettersum(word, values):
    lettersum = 0
    for letter in word:
        lettersum += values.get(letter, 0)
    return lettersum
        
lettervalues = generate_sums(alphabet)
print(lettersum('microspectrophotometries', lettervalues))