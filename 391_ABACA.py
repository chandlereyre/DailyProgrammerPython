import string
alphabet = string.ascii_lowercase

file = open('C:/Users/chaby/Code/python/DailyProgrammer/abaca_output.txt', 'w')
def ABACA(iter):
    counter = 0
    last_iteration = ''
    for i in range(iter):
        current_letter = alphabet[i]
        this_iteration = last_iteration + current_letter + last_iteration
        last_iteration = this_iteration
        counter += 1
    return this_iteration

file.write(ABACA(26))

# for loop runs for each iteration,
# counter for each letter of alphabet
# each time add one more index of alphabet
