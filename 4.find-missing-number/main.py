def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output


listOfNumbers = [1, 2, 3, 5, 7, 10]
print(f"Missing numbers are : {findMissingNumbers(listOfNumbers)}")
