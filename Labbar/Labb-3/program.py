import os.path as path
import sys

import requests

import util
import search
import gui

menu = """
############################################
# Welcome to the Main Menu                 #
# Please enter your choice of action below #
############################################
# 1) Search for Movie                      #
# 2) View Previous Searches                #
# 3) Rate a Movie                          #
# 3) Exit                                  #
############################################
"""

if __name__ == '__main__':
    #gui.MainScreen.renderMainScreen()
    if not path.exists("./api-key.txt"):
        print("A file has been generated in your run-dir named 'api-key.txt' please enter your api-key for omdb there")
        with open("./api-key.txt", 'w', encoding='utf-8'):
            pass
        sys.exit()
    with open("./api-key.txt", 'r') as file:
        apiKey = file.read(8)
    response = requests.get(f"http://www.omdbapi.com/?apikey={apiKey}")
    json = response.json()
    while 'Error' in json and json['Error'] == 'Invalid API key!':
        print("Error: Invalid API Key")
        apiKey = input("Please enter your api key: ")
        response = requests.get(f"http://www.omdbapi.com/?apikey={apiKey}")
        json = response.json()
    optionID = -1
    while True:
        while optionID == -1:
            print(menu)
            optionID = input("Which program would you like to run: ")
            while not util.is_integer(optionID) or not util.is_within(int(optionID), 1, 3):
                print("Error: Invalid Program ID")
                optionID = input("Which program would you like to run: ")
            optionID = int(optionID)
        if optionID == 1:
            optionID = search.menu.runSearchMenuLogic(apiKey)
        elif optionID == 2:
            print()
        else:
            sys.exit()
