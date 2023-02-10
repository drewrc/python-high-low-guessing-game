import random

#computer chooses random number between 1-10
computer = random.randint(1,10)

guesses = 0

while guesses <= 2:
    guess = int(input("Enter your guess:"))
    guesses += 1
    if guess != computer: 
        print("Try again")
        print(guesses)
    else:
        print("You win!")
        break
    
    import random

#def play():
    #computer chooses random number between 1-10
#    computer = random.randint(1,10)
#    guesses = 0
    #run loop while guesses < 3
#    while guesses < 3:
    #convert string to int
#        guesses += 1
#        guess = int(input("Enter your guess:"))
#        if guess == computer: 
#            print("You win")
#            print("attempt", guesses)
#        elif guess < random_number:
#            print('Your guess was too low.')
#        else:
#            print("Your guess was too high")
        
#        if guesses == 3:
#            print('Sorry, you ran out of guesses.')
      
#    if __name__ == '__main__':
#        play()