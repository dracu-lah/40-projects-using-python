def maximum(x):
    max_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] > x[max_index]:
            max_index = current_index
        current_index += 1
    return max_index

a = [23, 76, 45, 20, 70, 65, 15, 54]

print(f"Maximum:  {maximum(a)}")