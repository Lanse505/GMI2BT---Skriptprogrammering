from MyDictionary import roman_numerals

def to_roman(number:int):
  floored = floor_key(roman_numerals, number)
  if number is floored:
    return roman_numerals.get(number)
  
  return roman_numerals.get(floored) + to_roman(number - floored)


def floor_key(d, key):
    if key in d:
        return key
    return max(k for k in d if k < key)