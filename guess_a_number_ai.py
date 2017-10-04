"""
Jaden H.
RareSwag
Guess A Number AI
9-28-17
"""
import random
import math

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


def get_name():
    name = input("What's your name fam")
    return name

def get_guess(current_low, current_high):
    guess = (current_high + current_low) // 2
    return guess

def get_low(name):
    low = input("What would you like the low number to be " + name + "?")
    return int(low)

def get_high(low, name):
    high = input("What would you like the high number to be " + name + "?")
    if low >= int(high):
        print("High needs to be bigger then low  " + name + ".")
        get_low()
    
    return int(high)

def pick_number(low, high, name):
    guess = input("Ey fam, Pick a number between " + str(low) + " and " + str(high) + ", " + name + ", and i'm gunna guess it.")
    print()
    if int(guess) >= high + 1:
        print("Between " + str(low) + " and " + str(high) + " you dum dum")
        pick_number()
    elif int(guess) <= low - 1:
        print("Between " + str(low) + " and " + str(high) + " you dum dum")
        pick_number()
    else:
        return guess

def check_guess(guess, aiguess, limit, name):
    print()
    print("Was your guess " + str(guess) + " " + name + ".")
    playinpu = input("Guess " + str(aiguess) + " out of " + str(limit) + ", was my guess to high or low or was I right " + name + ". (Low/High/Correct)")
    playinpu = playinpu.lower()
    print()
    if playinpu == "l" or playinpu == "low":
        check =  -1
        return check
    elif playinpu == "h" or playinpu == "high":
        check = 1
        return check
    elif playinpu == "correct" or playinpu == "right" or playinpu == "yes" or playinpu == "c":
        check = 0
        return check
    else:
        print("Type High Or Low " + name + ".")
        

def show_result(guess, aiguess, limit, name):
    if aiguess != limit + 1:
        print("I know good and well your number was " + str(guess) + " " + name + ".")
        print("I got it in " + str(aiguess) + " guesses.")
    else:
        print("I suck and should be terminated. Ur to clean " + name + ".")
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
    input("Press Enter to continue...")
    name = get_name()
    low = get_low(name)
    high = get_high(low, name)
    current_low = low
    current_high = high
    check = -1
    aiguess = 1
    limit = math.ceil(math.log(high - low + 1 , 2))

    pick_number(low, high, name)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess, aiguess , limit, name)
        aiguess = aiguess + 1

        if aiguess != limit + 1:
            if check == -1:
                current_low = guess
            elif check == 1:
                current_high = guess
            elif check == 0:
                pass
        else:
            print("I ran out of guesses...rip")
            check = 0

    show_result(guess, aiguess, limit, name)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
