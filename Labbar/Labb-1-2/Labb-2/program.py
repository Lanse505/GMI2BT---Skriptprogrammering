import os.path
import json
import util

# TODO: Code Review with Joakim
if __name__ == '__main__':  # Checks if the code is being invoked directly and not as an import
    # Main Menu as a printable multi-line string
    menu = """
#####################
# 1 - Add Person    #
# 2 - Remove Person #
# 3 - Save File     #
# 4 - View Person   #
# 5 - Exit          #
#####################
            """
    field_names = ['username', 'first_name', 'last_name', 'email']  # Default Field Names
    field_names_sv = ['användarnamn', 'förnamn', 'efternamn', 'epost']  # Default Swedish Field Names

    # Get if the user wants to load from the target CSV or the cached JSON
    get_from_csv = input("Do you want to load from a CSV or from the cached JSON? [CSV, JSON]: ")
    csv_dict = {}  # Setups an empty dict to use
    if get_from_csv.upper() == "CSV":  # Checks if the user wanted to load from the CSV
        util.populate_from_csv(csv_dict, field_names)  # Populates the csv_dict from the csv
    if get_from_csv.upper() == "JSON" and os.path.exists('./temp.json'):  # Checks if the JSON file already exists
        with open('./temp.json', "r+", encoding='utf-8-sig') as temp:  # Opens the existing temp.json
            csv_dict = json.load(temp)  # Parses the JSON into the csv_dict as a dict object
    with open('./temp.json', "w+", encoding='utf-8-sig') as temp:  # Opens a new file
        json.dump(csv_dict, temp, indent=True, ensure_ascii=False, cls=util.PersonEncoder)  # Dumps the dict to Json

    is_first_run = True  # Sets the "first run" value so it only prints the json to log once
    while True:  # Continuous Loop that's broken out of later
        option = -1  # Checks if the current target is the menu or a sub-program
        if is_first_run:  # If it is the first run
            with open('./temp.json', "r+", encoding='utf-8-sig') as temp:  # Opens up the temp.json
                print(temp.read())  # Prints the entire file contents to log
            print()  # Print empty line
            is_first_run = False  # Set that this is no longer the first run of the main menu

        while option == -1:  # If the option value is -1 then run the main menu cycle
            print(menu)  # Prints the Main Menu multi-line string
            valueIn = input("Select your preferred option: ")  # Asks for the preferred program option
            # Checks if the input is a parsable integer and is within 1-5
            while not util.is_integer(valueIn) or not util.is_within(int(valueIn), 1, 5):
                print("Error: Invalid Input, Please enter a number between 1-5")  # Prints error message if not
                valueIn = input("Select your preferred option: ")  # Asks for new input and loops
            option = int(valueIn)  # Parses the validated input to the option value

        if option == 1:  # option 1: Add Person
            option = util.addPerson(csv_dict) # Calls addPerson in util
            input("Press Any Key to Return to Menu")  # Input to not instantly clear the message line
        elif option == 2:  # option 2: Remove Person
            option = util.removePerson(False, csv_dict) # Calls removePerson with a default "False" for while-loop
            input("Press Any Key to Return to Menu")  # Input to not instantly clear the message line
        elif option == 3:  # option 3: Flush JSON to CSV
            print("Flushing JSON to CSV")  # Info Message
            option = util.flush_from_json_to_csv(field_names_sv)  # Calls flush_to_csv in util
            input("Press Any Key to Return to Menu")  # Input to not instantly clear the message line
        elif option == 4:  # option 4: runs the get_user_data function in util
            option = util.get_user_data(csv_dict)  # Calls the get_user_data function in util
            input("Press Any Key to Return to Menu")  # Input to not instantly clear the message line
        elif option == 5:  # option 5: exit
            break  # Breaks out of the while loop
        print()  # Prints an empty line
