import os.path

import util
import requests
import search


def runSearchMenuLogic(api_key: str):
    typeTarget, movie_id = util.getSearchID()
    r = util.getRequest(api_key, typeTarget, movie_id)
    if r.status_code != 200 or 'Error' in r.json():
        util.handleSearchError(r)
    else:
        rj = r.json()
        handlers = []
        if 'Search' in rj:
            for d in rj['Search']:
                handlers.append(f"Option {rj['Search'].index(d)}: {search.searchHandler.SearchHandler(True, d)}")
            for h in handlers:
                print(h)
            target = input("Which of the above movies/series did you want to view?: ")
            while not util.is_integer(target) or not util.is_within(int(target), 0, len(rj['Search'])):
                print("Error: Invalid Target ID")
                target = input("Which of the above movies/series did you want to view?: ")
            title = rj['Search'][int(target)]['Title']
            imdbId = rj['Search'][int(target)]["imdbID"]
            util.handleSearchSave(title, imdbId)
            r = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={imdbId}")
            handler = search.searchHandler.SearchHandler(False, r.json())
            print(handler)
        else:
            title = rj['Title']
            imdbId = rj["imdbID"]
            print(title, imdbId)
            util.handleSearchSave(title, imdbId)
            handler = search.searchHandler.SearchHandler(False, rj)
            print(handler)
        input("Press any key to continue back to MainMenu")
