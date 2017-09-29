"""
Jaden H.
RareSwag
Guess A Number AI
9-28-17
"""
import random
import math

#config
low = 1
high = 100

# helper functions
def show_start_screen():
    print("´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶……..")
    print("´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´¶¶……")
    print("´´´´´´¶¶¶¶¶´´´´´´´¶¶´´´´´´´´´´´´´´¶¶……….")
    print("´´´´´¶´´´´´¶´´´´¶¶´´´´´¶¶´´´´¶¶´´´´´¶¶…………..")
    print("´´´´´¶´´´´´¶´´´¶¶´´´´´´¶¶´´´´¶¶´´´´´´´¶¶…..")
    print("´´´´´¶´´´´¶´´¶¶´´´´´´´´¶¶´´´´¶¶´´´´´´´´¶¶…..")
    print("´´´´´´¶´´´¶´´´¶´´´´´´´´´Guess a Number´´¶¶….")
    print("´´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´Game´´´´´´´¶¶….")
    print("´´´¶´´´´´´´´´´´´¶´¶¶´´´´´´´´´´´´´¶¶´´´´´¶¶….")
    print("´´¶¶´´´´´´´´´´´´¶´´¶¶´´´´´´´´´´´´¶¶´´´´´¶¶….")
    print("´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶´´´´´´´´¶¶´´´´´´´¶¶…")
    print("´¶´´´´´´´´´´´´´´´¶´´´´´¶¶¶¶¶¶¶´´´´´´´´´¶¶….")
    print("´¶¶´´´´´´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´¶¶…..")
    print("´´¶´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´¶¶….")
    print("´´¶¶´´´´´´´´´´´¶´´¶¶´´´´´´´´´´´´´´´´¶¶….")
    print("´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´¶¶…..")
    print("´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶…….")


def show_credits():
    print("░░▄░░░▄░▄▄▄▄░░░░░░░░░░░░░░░")
    print("░░█▀▄▀█░█▄▄░░░░░░░░░░░░░░░░")
    print("░░█░░░█░█▄▄▄░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░▄▄▄░▄░░░▄░░▄▄▄░▄▄▄▄▄░░▄▄▄░")
    print("█░░░░█░░░█░█░░░░░░█░░░█░░░█")
    print("█░▀█░█░░░█░░▀▀▄░░░█░░░█▀▀▀█")
    print("░▀▀▀░░▀▀▀░░▄▄▄▀░░░▀░░░▀░░░▀")

def get_guess(current_low, current_high):
    guess = (current_high + current_low) // 2
    
    return guess

def pick_number():
    print("Ey fam, Pick a number between " + str(low) + " and " + str(high) + " and i'm gunna guess it.")
    print()
    guess = input("Press Enter to continue...")
    if int(guess) >= high + 1:
        print("Between " + str(low) + " and " + str(high) + " you dum dum")
        pick_number()
    elif int(guess) <= low - 1:
        print("Between " + str(low) + " and " + str(high) + " you dum dum")
        pick_number()
    else:
        return guess

def check_guess(guess, aiguess, limit):
    print("Was your guess " + str(guess) + ".")
    print()
    playinpu = input("Guess " + str(aiguess) + " out of " + str(limit) + ", was my guess to high or low or was I right (Low/High/Correct)")
    playinpu = playinpu.lower()
    print()
    if playinpu == "l" or playinpu == "low":
        check =  -1
        return check, aiguess
    elif playinpu == "h" or playinpu == "high":
        check = 1
        return check, aiguess
    elif playinpu == "correct" or playinpu == "right" or playinpu == "yes":
        check = 0
        return check, aiguess
    else:
        print("Type High Or Low")
        

def show_result(guess, aiguess):
    print("I know good and well your number was " + str(guess) + ".")
    print()
    print()

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            

def play():
    limit = math.ceil(math.log(high - low + 1 , 2))
    aiguess = 1
    current_low = low
    current_high = high
    check = -1

    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check, ainumber = check_guess(guess, aiguess , limit)
        ainumber = ainumber + 1
        
        if check == -1:
            current_low = guess
        elif check == 1:
            current_high = guess
        elif check == 0:
            pass

    show_result(guess, aiguess, limit)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
