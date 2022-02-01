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
    valid_numbers.remove(0)
    print(valid_numbers)


def guessing_game():
    number = randint(1, 100)
    guess = 0
    tries = 0
    while guess != number:
        guess = input('Please enter a number between 1-100: ')
        while not is_integer(guess) or not is_within(int(guess), 1, 100):
            print("Error: Invalid Input - Number needs to be between 1-100")
            guess = int(input('Please enter a number between 1-100: '))
        guess = int(guess)
        if guess < number:
            print("The entered guess was wrong! Too Low")
            tries += 1
        elif guess > number:
            print("The entered guess was wrong! Too High")
            tries += 1
    print(f"Congratulations You Won! The number was {number}, It took you {tries + 1} tries to find the correct number.")


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
    if value != "print_divisible_numbers" and value != "guessing_game":
        return False
    return True
