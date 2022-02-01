import util
import requests

import search


def runSearchMenuLogic(api_key: str):
    typeTarget, movieId = util.getSearchID()
    if typeTarget.lower() == 'id':
        r = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={movieId}")
    else:
        r = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&s={movieId}")
    if r.status_code != 200 or 'Error' in r.json():
        print()
        print("Error: The requested ID was either found no results or returned a status-code other than 200")
        print(f"Status Code: {r.status_code}")
        print(f"Error: {r.json()['Error']}")
        print(f"Reason: {r.reason}")
        print()
        input("Press any key to continue back to MainMenu")
        return -1
    else:
        rj = r.json()
        handlers = []
        if 'Search' in rj:
            for d in rj['Search']:
                handlers.append(f"Option {rj['Search'].index(d)}: {search.handler.SearchHandler(True, d)}")
            for h in handlers:
                print(h)
            target = input("Which of the above movies/series did you want to view?: ")
            while not util.is_integer(target) or not util.is_within(int(target), 0, len(rj['Search'])):
                print("Error: Invalid Target ID")
                target = input("Which of the above movies/series did you want to view?: ")
            imdbId = rj['Search'][int(target)]["imdbID"]
            r = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={imdbId}")
            handler = search.handler.SearchHandler(False, r.json())
            print(handler)
        else:
            handler = search.handler.SearchHandler(False, rj)
            print(handler)
        input("Press any key to continue back to MainMenu")
        return -1
