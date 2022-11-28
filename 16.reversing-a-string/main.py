# The first character in the string has index 0, and the last character has index n-1, where n is the length of the string. The string slicing operator “::” reads all the characters of the string, and -1, in the end, reverses the order of the characters. This is how we can reverse a string

def reverse_string(string):
    return string[::-1]

a = input("Enter a string :")
print(reverse_string(a))