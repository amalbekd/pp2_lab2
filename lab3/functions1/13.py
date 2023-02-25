<<<<<<< HEAD
import random

print("Hello! What is your name?")
name = input()

x = random.randrange(1, 20)
i = 0

print("Well,", name + ',', "I am thinking of a number between 1 and 20.")

while 1:
    print("Take a guess.")
    i += 1
    n = int(input())
    print()
    
    if n == x:
        print("Good job,", name + '!', "You guessed my number in", i, "guesses!")
        break
    elif x > n:
        print("Your guess is too low.")
    else:
=======
import random

print("Hello! What is your name?")
name = input()

x = random.randrange(1, 20)
i = 0

print("Well,", name + ',', "I am thinking of a number between 1 and 20.")

while 1:
    print("Take a guess.")
    i += 1
    n = int(input())
    print()
    
    if n == x:
        print("Good job,", name + '!', "You guessed my number in", i, "guesses!")
        break
    elif x > n:
        print("Your guess is too low.")
    else:
>>>>>>> 2a979e4717352ef20e11fce5aa6c52f3c54e7091
        print("Your guess is too high.")