import modules

roman_numerals = {
  1:"I", 
  4:"IV", 
  5:"V",
  9:"IX",
  10:"X",
  40:"XL",
  50:"L",
  90:"XC",
  100:"C",
  400:"CD",
  500:"D",
  900:"CM",
  1000:"M"
}

if __name__ == '__main__':
  print(modules.to_roman(1337))
