import random
import math

# config
low = 1
high = 100
limit = math.ceil(math.log(high - low + 1 , 2))

# helper functions
def show_start_screen():
    print("_/﹋\_")
    print("(҂`_´)")
    print("<,︻╦╤─ ҉ - - Guess A Name")
    print("_/﹋\_")
    
def show_credits():
    print("░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░")
    print("░░░░█░░░░░░GG░░░░░█░░░░")
    print("░░░█░░░░░░░░░░▄▄▄░░█░░░")
    print("░░░█░░▄▄▄░░▄░░███░░█░░░")
    print("░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░")
    print("░░░█░░▀█▀█▀█▀█▀█▀░░█░░░")
    print("░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░")
    print("░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + " and you will have " + str(limit) + " tries to guess it.")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print()
        print("You guessed too low.")
    elif guess > rand:
        print()
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print()
        print("You win!")
    else:
        print()
        print("You are such a loser! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.upper()
        print()

        if decision == 'Y' or decision == 'YES':
            return True
        elif decision == 'N' or decision == 'NO':
            return False
        else:
            print()
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


