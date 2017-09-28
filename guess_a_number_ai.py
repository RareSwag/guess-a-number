"""
Jaden H.
RareSwag
Guess A Number AI
9-28-17
"""
import random


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

def set_var():
    low = input("Set the low number.")
    print()
    high = input("set the high number.")
    print()
    if low > high or high == int or low == int:
        print("Make the low less then high and that you typed numbers")
        set_var()

    return low, high


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

def check_guess(guess):
    print("Was your guess " + str(guess) + ".")
    playinpu = input("Was my assesment to high or low or was I right (Low/High/Correct)")
    playinpu = playinpu.lower()
    if playinpu == "l" or playinpu == "low":
        check =  -1
        return check
    elif playinpu == "h" or playinpu == "high":
        check = 1
        return check
    elif playinpu == "correct" or playinpu == "right":
        check = 0
        return check
    else:
        print("Type High Or Low")
        

def show_result(guess):
    print("I know good and well your number was " + str(guess) + ".")
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
    low, high = set_var()
    
    current_low = low
    current_high = high
    check = -1

    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_low = guess
        elif check == 1:
            current_high = guess
        elif check == 0:
            pass

    show_result(guess)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
