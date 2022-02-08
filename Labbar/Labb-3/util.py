import json
import os
import re
import sys
import urllib.parse
import requests
import search


menu = """
############################################
# Welcome to the Main Menu                 #
# Please enter your choice of action below #
############################################
# 1) Search for Movie                      #
# 2) View Previous Searches                #
# 3) Rate a Movie                          #
# 4) Exit                                  #
############################################
"""


# Gets the Searchable ID for API Queries
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


# Handles getting and validating the api-key system
def handleAPIKey():
    if not os.path.exists("./api-key.txt"):  # Checks if the api-key file exists
        # If not then generate the file and inform the user
        print("A file has been generated in your run-dir named 'api-key.txt' please enter your api-key for omdb there")
        with open("./api-key.txt", 'w', encoding='utf-8'):  # Generates the empty file
            pass  # Pass
        sys.exit()  # Shutdown script
    with open("./api-key.txt", 'r') as file:  # If the api-key file exists
        api_key = file.read(8)  # Read the first 8 length of the file which should be the 8 characters of the api-key
    response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}")  # Queries the api to check key validity
    inputJson = response.json()  # Grab the response as JSON
    while 'Error' in inputJson and inputJson['Error'] == 'Invalid API key!':  # If it contains Error and the error is invalid key
        print("Error: Invalid API Key")  # Error
        api_key = input("Please enter your api key: ")  # Ask for new key manually
        response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}")  # Validate input key
        inputJson = response.json()  # Set the json to the new response json
    return api_key  # Return the Key


# Runs the main logic loop for the program
def runMainLoop(api_key: str):
    option_id = -1
    while option_id == -1:
        print(menu)
        option_id = input("Which program would you like to run: ")
        while not is_integer(option_id) or not is_within(int(option_id), 1, 4):
            print("Error: Invalid Program ID")
            option_id = input("Which program would you like to run: ")
        option_id = int(option_id)
    if option_id == 1:
        search.menu.runSearchMenuLogic(api_key)
    elif option_id == 2:
        getHistoricSearches(api_key)
    else:
        sys.exit()


def getRequest(api_key: str, typeTarget: str, movie_id: str):
    if typeTarget.lower() == 'id':
        return requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={movie_id}")
    else:
        return requests.get(f"http://www.omdbapi.com/?apikey={api_key}&s={movie_id}")


def handleSearchError(r: requests.Response):
    print()
    print("Error: The requested ID was either found no results or returned a status-code other than 200")
    print(f"Status Code: {r.status_code}")
    print(f"Error: {r.json()['Error']}")
    print(f"Reason: {r.reason}")
    print()
    input("Press any key to continue back to MainMenu")


def getHistoricSearches(api_key: str):
    if not os.path.exists("./searches.json"):
        print("Error: No Historic Search Results to Show")
        input("Press any key to continue back to MainMenu")
    else:
        with open("./searches.json", 'r+', encoding='utf-8') as file:
            searches = json.load(file)
            for i, result in enumerate(searches):
                print(f"{i}: \tTitle: {result['Title']}, imdbId: {result['imdbID']}")
            use_search = input("Would you like to search by any of these results? [Yes/No]")
            while use_search.lower() != "yes" and use_search.lower() != "no":
                print("Error: Invalid Input, Use either 'Yes' or 'No' ")
                use_search = input("Would you like to search by any of these results? [Yes/No]")
            if use_search.lower() == "yes":
                target = input("Which movie would you like to search for? [Use index number]: ")
                while not is_integer(target) or not is_within(int(target), 0, 4):
                    print("Error: Invalid ID")
                    target = input("Which movie would you like to search for? [Use index number]: ")
                searchTarget = searches[int(target)]
                r = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={searchTarget['imdbID']}")
                handler = search.searchHandler.SearchHandler(False, r.json())
                print(handler)
                input("Press any key to continue back to MainMenu")
            elif use_search.lower() == 'no':
                pass


def handleSearchSave(title: str, imdb_id: str):
    searches = []
    if not os.path.exists("./searches.json"):
        with open("./searches.json", 'w'):
            pass
    else:
        with open("./searches.json", 'r+', encoding='utf-8') as file:
            searches = json.load(file)
    if len(searches) >= 4:
        clean = []
        for i, memory in enumerate(searches):
            if i == 0:
                pass
            else:
                clean.append(memory)
        searches = clean
    if len(searches) == 0:
        searches.append({'Title': title, 'imdbId': imdb_id})
    else:
        index = len(searches)
        searches.insert(index, {'Title': title, 'imdbID': imdb_id})
    with open("./searches.json", 'r+') as file:
        json.dump(searches, file, indent=True, ensure_ascii=False)


# Checks if the provided input can be converted to an integer
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
