import csv
import json
import re
from json import JSONEncoder


class Person:
    def __init__(self, info: dict):
        self.info = info

    def get_value(self, identifier: str):
        return self.info[identifier]

    def get_info(self):
        return self.info

    def __getitem__(self, item):
        return self.info


class PersonEncoder(JSONEncoder):
    def default(self, person):
        return person.info


# Opens up the csv as a file and returns both the file itself and the csv-reader for the file
def open_csv(path: str, mode: str):
    file = open(path, mode, encoding='utf-8-sig')  # Opens up the file using utf-8-sig encoding to support all chars
    reader = csv.reader(file, delimiter=';')  # Opens up the CSV using a csv reader using ';' as a delimiter
    return reader, file  # Returns a tuple of the csv reader and the original file


# TODO: Code Review with Joakim
# TODO: Rewrite to support any input location
# Populates the csv_dict object using the clean csv file
def populate_from_csv(csv_dict, field_names):
    csv_file, file = open_csv("./clean.csv", "r+")  # Opens the csv
    for i, row in enumerate(csv_file):  # Iterate over the rows in the csv
        if i == 0:  # If the row is the header row then continue
            continue  # Skip if it's the head column
        person_dict: dict = {}  # Create an empty dictionary for the user
        for j, name in enumerate(field_names):  # Loops over the field_names
            row_value = row[j]  # Get the value from the CSV
            if row_value is not None:  # If the value isn't empty then add it and its value to the new dict
                person_dict[name] = row[j]  # Set the fields of the "person_dict"
                continue  # Continue as to not add double values to the dict
            person_dict[name] = None  # If the value was empty then add an empty field value to the dict
        person: Person = Person(person_dict)  # Creates a new Person object holding the person_dict as information
        csv_dict[row[0]] = person  # Set the "person" to the "csv_dict" with the username as key.
    file.close()  # Closes the file reference


# TODO: Code Review with Joakim
# Flushes the code from the stored object map to JSON and the csv
def flush_from_json_to_csv(field_names_sv):
    with open('./temp.json', "r+", encoding='utf-8-sig') as saved:  # Opens the file again in read/write mode
        json_dict = json.load(saved)  # Loads the Json into csv_dict overriding it with the contents of the JSON
        with open('./labb2_personer_vt22.csv', 'w', newline='') as file:  # Opens the csv file itself
            writer = csv.writer(file, delimiter=';')  # Grabs the writer for the file
            writer.writerow(field_names_sv)  # Writes the header using swedish names
            for (key, value) in enumerate(json_dict.items()):  # Loops over the top-level keys and values
                nk, nv = value  # Grabs the value which is a key/value store
                # Writes a row consisting of the internal values of 'username', 'first_name', 'last_name' and 'email'
                writer.writerow([nv['username'], nv['first_name'],
                                 nv['last_name'], nv['email']])
    return -1  # Returns -1 to reset the menu to the Main Menu


# TODO: Code Review with Joakim
# Flushes the csv_dict contents to JSON
def flush_to_json(csv_dict):
    with open('./temp.json', "w", encoding='utf-8-sig') as flush:  # Clear the json file
        # Dumps the csv_dict contents to the json
        json.dump(csv_dict, flush, indent=True, ensure_ascii=False, cls=PersonEncoder)


# TODO: Code Review with Joakim
# Adds a new person to the csv dictionary, also applies regex input validation.
def addPerson(csv_dict):
    username = input("Please enter a username for the person you want to add: ")  # Grab the username input
    # Match it against our regex and check so it doesn't exist already
    while not is_regex_compliant(username, r"[hv]\d{2}[a-z]{5}") or username in csv_dict:
        print("Invalid input: Please provide a valid username matching the following regex format:")  # Print Error
        print(r"[[hv]\d{2}[a-z]{5}] - [Example: h00andan]")  # Print Example
        username = input("Please enter a username for the person you want to add: ")  # Ask for new Input
    first_name = input("Please enter the first name of the user you want to add: ")  # Ask for First Name
    while first_name is None or first_name == "":  # Validate that there was a valid input and the input wasn't empty
        print("Error: Invalid Input - 'First Name' was either of type None or Empty")  # Print Error
        first_name = input("Please enter the first name of the user you want to add: ")  # Ask for new input
    last_name = input("Please enter the last name of the user you want to add: ")  # Ask for Last Name
    while last_name is None or last_name == "":  # Validate that there was a valid input and the input wasn't empty
        print("Error: Invalid Input - 'First Name' was either of type None or Empty")  # Print Error
        last_name = input("Please enter the last name of the user you want to add: ")  # Ask for new
    # Generate the user-dict based on the input information
    user_dict = {'username': username, 'first_name': first_name,
                 'last_name': last_name, 'email': username + "@du.se"
                 }
    csv_dict[username] = user_dict  # Add the user-dict to the internal csv-dict
    flush_to_json(csv_dict)  # Flush the newly added content to JSON
    return -1  # Return -1 to return to main menu


# TODO: Code Review with Joakim
# Removes a person from the list, validates the input username by checking if the dict contains the name.
def removePerson(removed, csv_dict):
    while not removed:  # Check so an removal hasn't been done
        # Get the input username
        username = input("Please enter the username of the User you want to delete [exit = return to main menu]: ")
        if username == "exit":  # Check if it's 'exit' in which case return to main menu
            return -1  # Return to main menu
        if username in csv_dict:  # Check so the username key exists in the internal csv_dict
            csv_dict.pop(username)  # Remove the user from the internal dict
            flush_to_json(csv_dict)  # Flush the updated dict to JSON
            print(f"Removed user: {username}")  # Print a message stating they got removed
            removed = True  # Set removed to True
        else:
            print(f"Error: User with Username: {username} , Didn't exist!")  # If the user didn't exist, print error


# TODO: Code Review with Joakim
# Gets the userdata for the provided username, uses both regex validation and existence validation to validate the input
def get_user_data(csv_data):
    username = input("Please enter the username of the user you want to view: ")  # Gather username input
    # Check so the input exists and is regex compliant
    while not is_regex_compliant(username, r"[hv]\d{2}[a-z]{5}") or username not in csv_data:
        print(r"Invalid Error: Please input a regex compliant username [[hv]\d{2}[a-z]{5}]: ")  # Print Error
        username = input("Please enter the username of the user you want to view: ")  # Ask for new input
    data = csv_data[username]  # Get the user-data dict from the internal csv-dict by key
    first_name = data['first_name']  # Get the first_name
    last_name = data['last_name']  # Get the last_name
    email = data['email']  # Get the Email
    print(f"Printing data for user: {username}")  # Information Print
    print(f"Username: {username}")  # Print Username
    print(f"First Name: {first_name}")  # Print First Name
    print(f"Last Name: {last_name}")  # print Last Name
    print(f"Email: {email}")  # print Email
    return -1  # Return -1 to return to main menu


# Checks if the provided input can be converted to an integer
def is_integer(num):
    try:  # Attempt to execute
        int(num)  # Attempt parse to int
        return True  # If success True
    except ValueError:
        return False  # If failure False


# Checks if the provided string is valid against the provided regex pattern
def is_regex_compliant(testable: str, pattern: str):
    if re.match(pattern, testable):  # Attempt to match string against provide regex pattern
        return True  # If it passes Regex then return True
    return False  # If it doesn't pass Regex then return False


# Checks if the provided value is less than the maximum specified value but greater than the minimum specified value.
def is_within(value, minimum_inclusive, maximum_inclusive):
    # Check so that the value is:
    # Larger than minimum_inclusive
    # Smaller than maximum_inclusive
    if minimum_inclusive <= value <= maximum_inclusive:
        return True  # Returns true if it's between min_inclusive and max_inclusive
    return False  # Returns false if it's outside the bounds of min_inclusive and max_inclusive
