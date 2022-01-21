from random import randint


# Programs
def print_divisible_numbers():
    div1 = input('Please enter denominator 1: ')
    while not is_integer(div1):
        print("Error: Invalid Input for Denominator")
        div1 = input('Please enter denominator 1: ')
    div2 = input('Please enter denominator 2: ')
    while not is_integer(div2):
        print("Error: Invalid Input for Denominator")
        div2 = input('Please enter denominator 2: ')
    valid_numbers = []
    for number in range(0, 1001, 1):
        if number % int(div1) == 0 and number % int(div2) == 0:
            valid_numbers.append(number)
    print(valid_numbers)


def guessing_game():
    number = randint(1, 1000)
    guess = 0
    while guess != number:
        guess = input('Please enter a number between 1-1000: ')
        while not is_integer(guess) or not is_within(int(guess), 1, 1000):
            print("Error: Invalid Input - Number needs to be between 1-1000")
            guess = int(input('Please enter a number between 1-1000: '))
        if guess < number:
            print("The entered guess was wrong! Too Low")
        elif guess > number:
            print("The entered guess was wrong! Too High")
    print(f"Congratulations You Won! The number was {number}")


# Checker Methods
def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def is_within(value, minimum_inclusive, maximum_inclusive):
    if minimum_inclusive <= value <= maximum_inclusive:
        return True
    return False


def is_valid_program(value):
    if value != "print_divisible_numbers" or value != "guessing_game":
        return False
    return True
