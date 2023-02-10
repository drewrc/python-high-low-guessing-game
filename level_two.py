import random

guess = int(input("Enter your number 1-10:"))

guesses = 0

while guesses <= 2:
    computer = random.randint(1,10)
    guesses += 1
    if computer != guess: 
        print(computer)
        print("Computer guessed wrong!")
    else:
        print("Computer wins! Computer guessed", guess)
        break

#import random

#guess = int(input("Enter your number 1-10:"))
#guesses = 0

#while guesses < 3:
#    computer = random.randint(1,10)
#    guesses += 1
#    if computer != guess: 
#        print('The computer guessed', computer)
#        print("Computer guessed wrong!")
#    else:
#        print("Computer wins! Computer guessed", guess)
#        break
#    if guesses == 3:
#        print("You win! The computer did not guess your number.")