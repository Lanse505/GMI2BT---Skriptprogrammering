from modules import print_divisible_numbers, guessing_game, is_valid_program

if __name__ == '__main__':
  print("Programs: ")
  print("\t- print_divisible_numbers")
  print("\t- guessing_game")
  value = input('Please enter the program you want to run: ')
  while is_valid_program(value):
    print("Error: Invalid input program")
    value = input('Please enter the program you want to run: ')

  if value == "print_divisible_numbers":
    print_divisible_numbers()
  elif value == "guessing_game":
    guessing_game()
