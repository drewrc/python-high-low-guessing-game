import random

playerinput = int(input("Enter your number 1-10:"))

low = 1
high = 10 

computer = 5

guesses = 0

while computer != playerinput:
    guesses += 1
    computer = (low + high)//2
    if computer > playerinput:
        high = computer - 1
        print("Too high")
        print(computer)
    if computer < playerinput:
        low = computer + 1
        print("Too low")
        print(computer)
    elif computer == playerinput:
        print("computer guesses number", computer, "and computer guesses", guesses, "times")
        break


#import random

#def play():
#    player_number = int(input('Pick a number beterrn 1 and 10.'))
#    min_num, max_num = 1, 10
#    guesses = 0
    #be careful using 'while True'
#    while True:
#        computer = (min_num + max_num) // 2
#        guesses +=1
        
#        if computer == player_number:
#            print(f'The computer guessed your number in {guesses} tries.')
#            break
#        elif computer < player_number:
#            print('The computer guessed too low.')
#            min_num = computer + 1
#        else:
#            print('The computer guessed too high.')
#            max_num = computer - 1
#if __name__ == "__main__":
#    play()