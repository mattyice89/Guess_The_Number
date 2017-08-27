''' Prompt:
Using  the random module, the program will randomly guess a number
unknown to the user.  The user needs to guess what that number is
(the user needs to be able to input information).  If the User's guess
is wrong, the pgoram should return some sort of indication as to how wrong
(i.e. the number is too high or too low).  If the user guesses correctly,
a positive indication should appear.  You'll need functions to check
if the user input is an actual number, to see the difference between
the inputted number and the randomly generated numbers, and to compare
the numbers.
'''

import random
from sys import exit

# I will make my program generate a number between one and ten.
number_generator = random.randint(1,10)

def start():
    print ('Guess an integer between one and ten')
    while True:
        try:
            guess = int(input("> "))
            break
        except ValueError:
            print("That's not an integer!")
    #print(f'The actual number is {number_generator}') <--- remove this comment for testing purposes
    if guess < number_generator:
        print("Your guess is too low")
        start()
    elif guess > number_generator:
        print("Your guess is too high")
        start()
    else:
        print("Correct!")
        exit()

def int_check():
    from start import guess
    try:
        val = int(guess)
    except ValueError:
        print("That's not a number!")

start()
