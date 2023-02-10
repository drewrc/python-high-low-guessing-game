import level_three
import level_one
print("Would you like computer to guess? y/n?")

input = input("")

if input == "y":
    print("computer guesses")
    level_three
if input == "n":
    print("player guesses")
    level_one

    