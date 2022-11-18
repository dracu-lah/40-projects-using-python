# To create a guessing game, we need to write a program to select a random number between 1 and 10. To give hints to the user, we can use conditional statements to tell the user if the guessed number is smaller, greater than or equal to the randomly selected number.

import random
n = random.randrange(1, 10)
guess = int(input("Enter any number: "))
while n != guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again:"))
    else:
        break
print("you guessed it right")
