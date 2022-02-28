def change(amount):
    i = 0
    coins = [500, 100, 25, 10, 5, 1]
    sum = 0
    next = amount
    while next > 0:
        sum += next//coins[i]
        next = next%coins[i]
        i += 1
    return sum

print(change(0))
print(change(12))
print(change(468))
print(change(123456))