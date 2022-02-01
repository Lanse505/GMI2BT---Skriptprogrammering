import re


# Checks if the provided input can be converted to an integer
import urllib.parse


def is_integer(num):
    try:  # Attempt to execute
        int(num)  # Attempt parse to int
        return True  # If success True
    except ValueError:
        return False  # If failure False


# Checks if the provided value is less than the maximum specified value but greater than the minimum specified value.
def is_within(value, minimum_inclusive, maximum_inclusive):
    # Check so that the value is:
    # Larger than minimum_inclusive
    # Smaller than maximum_inclusive
    if minimum_inclusive <= value <= maximum_inclusive:
        return True  # Returns true if it's between min_inclusive and max_inclusive
    return False  # Returns false if it's outside the bounds of min_inclusive and max_inclusive


def getSearchID():
    typeTarget = input("Please input the ID Type [Example: ID, Name]: ")
    while typeTarget.lower() != 'id' and typeTarget.lower() != 'name':
        print("Error: Invalid Input")
        typeTarget = input("Please input the ID Type [Example: ID, Name]: ")
    movieId = input("Please input the ID [Example: tt3896198 or Guardians of the Galaxy]: ")
    if typeTarget.lower() == 'id':
        while not re.match(r"[t]{2}\d{7}", movieId) and typeTarget.lower() != 'name':
            print("Error: input did not match valid regex for an IMDB Id")
            movieId = input("Please input the ID [Example: tt3896198 or Guardians of the Galaxy]: ")
    else:
        movieId = urllib.parse.quote(movieId)
    return typeTarget, movieId
