def least_common_multiple(a, b):
    if a > b:
        greater = a
    elif b > a:
        greater = b
    else:
        print("should not be same values")
    while (True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


a, b = [int(i) for i in input("Enter two numbers : ").split()]
print(least_common_multiple(a, b))
