def nonogramrow(array):
    solution = []
    count = 0
    i = 0
    for i in range(len(array)):
        if array[i] == 1:
            count += 1
        if array[i] == 0 and array[i-1] == 1:
            solution.append(count)
            count = 0
    solution.append(count)
    return solution

print(nonogramrow([1,1,1,1,1]))
print(nonogramrow([0,0,1,1,0,1,1,0,1]))
print(nonogramrow([0,0,0,0,0]))