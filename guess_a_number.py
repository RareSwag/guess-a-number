import random

# config

low = 1
high = 100
tries = 5

# start game
rand = random.randrange(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1

# helper functions
def get_guess():
    while True:
        g = input("Take a guess: ")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("I don't understand medicine.")

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
    print("Ur Bad Kid")
