import random

# config

low = 1
high = 100
limit = 8

# helper functions
def get_guess():
    while True:
        g = input("Take a guess: ")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("I don't understand medicine.")

def play_again():
    while True:
        decision = input("You wanna play again? (y/n)")

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            return False

        print("Type y or n dummy.")

again = True

while again:
    # start game
    tries = limit
    rand = random.randrange(low, high)
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

    guess = -1

    # play game
    while guess != rand and tries > 0:
        guess = get_guess()
        
        if guess < rand:
            print("You guessed too low.")
            tries -= 1
            print("You have " + str(tries) + " tries left.")
        elif guess > rand:
            print("You guessed too high.")
            tries -= 1
            print("You have " + str(tries) + " tries left.")
        else:
            print("You got it fam!")


    if guess == rand:
        print("Good Job Fam")
    else:
        print("Ur Bad Kid. The number was " + str(rand) + ".")

    again = play_again()

print("Bye bye my dude.")

    


