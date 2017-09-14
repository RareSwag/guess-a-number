import random

# config

low = 1
high = 100
tries = 5

rand = random.randrange(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1

while guess != rand and tries > 0:
    guess = input("Take a guess: ")
    guess = int(guess)
    
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
