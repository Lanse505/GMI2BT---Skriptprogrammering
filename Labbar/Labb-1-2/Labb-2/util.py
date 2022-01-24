import csv
import json
import re


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
        person_dict = {}  # Create an empty dictionary for the user
        for j, name in enumerate(field_names):  # Loops over the field_names
            row_value = row[j]  # Get the value from the CSV
            if row_value is not None:  # If the value isn't empty then add it and its value to the new dict
                person_dict[name] = row[j]  # Set the fields of the "person_dict"
                continue  # Continue as to not add double values to the dict
            person_dict[name] = None  # If the value was empty then add an empty field value to the dict
        csv_dict[row[0]] = person_dict  # Set the "person_dict" to the "csv_dict" with the username as key.
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
                writer.writerow([nv['username'], nv['first_name'], nv['last_name'], nv['email']])
    return -1  # Returns -1 to reset the menu to the Main Menu


# TODO: Code Review with Joakim
# Flushes the csv_dict contents to JSON
def flush_to_json(csv_dict):
    with open('./temp.json', "w", encoding='utf-8-sig'):  # Clear the json file
        pass  # Just close the file, so that we clear it and then close it
    with open('./temp.json', "w", encoding='utf-8-sig') as flush:  # Opens the file again but in read/write mode
        json.dump(csv_dict, flush, indent=True, ensure_ascii=False)  # Dumps the csv_dict contents to the json


# TODO: Code Review with Joakim
# Adds a new person to the csv dictionary, also applies regex input validation.
def addPerson(csv_dict):
    username = input("Please enter a username for the person you want to add: ")
    while not is_regex_compliant(username, r"[hv]\d{2}[a-z]{5}") and username not in csv_dict:
        print("Invalid input: Please provide a valid username matching the following regex format:")
        print(r"[[hv]\d{2}[a-z]{5}] - [Example: h00andan]")
        username = input("Please enter a username for the person you want to add: ")
    first_name = input("Please enter the first name of the user you want to add: ")
    while first_name is None or first_name == "":
        print("Error: Invalid Input - 'First Name' was either of type None or Empty")
        first_name = input("Please enter the first name of the user you want to add: ")
    last_name = input("Please enter the last name of the user you want to add: ")
    while last_name is None or last_name == "":
        print("Error: Invalid Input - 'First Name' was either of type None or Empty")
        last_name = input("Please enter the last name of the user you want to add: ")
    user_dict = {'username': username, 'first_name': first_name,
                 'last_name': last_name, 'email': username + "@du.se"
                 }
    csv_dict[username] = user_dict
    flush_to_json(csv_dict)
    return -1


# TODO: Code Review with Joakim
# Removes a person from the list, validates the input username by checking if the dict contains the name.
def removePerson(removed, csv_dict):
    while not removed:
        username = input("Please enter the username of the User you want to delete: ")
        if username == "exit":
            return -1
        if username in csv_dict:
            csv_dict.pop(username)
            flush_to_json(csv_dict)
            print(f"Removed user: {username}")
            removed = True
        else:
            print(f"Error: User with Username: {username} , Didn't exist!")


# TODO: Code Review with Joakim
# Gets the userdata for the provided username, uses both regex validation and existence validation to validate the input
def get_user_data(csv_data):
    username = input("Please enter the username of the user you want to view: ")
    while not is_regex_compliant(username, r"[hv]\d{2}[a-z]{5}") or username not in csv_data:
        print(r"Invalid Error: Please input a regex compliant username [[hv]\d{2}[a-z]{5}]: ")
        username = input("Please enter the username of the user you want to view: ")
    data = csv_data[username]
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    print(f"Printing data for user: {username}")
    print(f"Username: {username}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Email: {email}")
    return -1


# Checks if the provided input can be converted to an integer
def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


# Checks if the provided string is valid against the provided regex pattern
def is_regex_compliant(testable: str, pattern: str):
    if re.match(pattern, testable):
        return True
    return False


# Checks if the provided value is less than the maximum specified value but greater than the minimum specified value.
def is_within(value, minimum_inclusive, maximum_inclusive):
    if minimum_inclusive <= value <= maximum_inclusive:
        return True
    return False
