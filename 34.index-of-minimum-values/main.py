def minimum(x):
    minimum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] < x[minimum_index]:
            minimum_index = current_index
        current_index = current_index+1
    return minimum_index


a = [23, 76, 45, 20, 70, 65, 15, 54]

print(minimum(a))