import json
import search


class SearchHandler(object):

    def SearchHandler(self, partial: bool, input_json: json):
        self.__init__(self, partial, input_json)

    def __init__(self, partial: bool, input_json: json):
        self.raw = input_json
        self.partial = partial
        if partial:
            self.title = input_json['Title']
            self.year = input_json['Year']
            self.imdbID = input_json['imdbID']
            self.type = input_json['Type']
            self.poster = input_json['Poster']
        else:
            self.title = input_json['Title']
            self.year = input_json['Year']
            self.rated = input_json['Rated']
            self.released = input_json['Released']
            time = str(input_json['Runtime']).split(' ')[0]
            self.runtime = search.runtime.SearchRuntimeHandler(int(time))
            self.genre = input_json['Genre']
            self.director = input_json['Director']
            self.writer = input_json['Writer']
            self.actors = input_json['Actors']
            self.plot = input_json['Plot']
            self.language = input_json['Language']
            self.country = input_json['Country']
            self.awards = input_json['Awards']
            self.poster = input_json['Poster']
            self.ratings = search.rating.SearchRatingHandler(input_json['Ratings'])
            self.metascore = input_json['Metascore']
            self.imdbRating = input_json['imdbRating']
            self.imdbVotes = input_json['imdbVotes']
            self.imdbID = input_json['imdbID']
            self.type = input_json['Type']

    def __str__(self):
        if self.partial:
            return f"""
    Title: {self.title}
    Year:  {self.year}
    imdbID: {self.imdbID}
    Type: {self.type}
    Poster: {self.poster}
            """
        else:
            return f"""
    Title: {self.title}
    Year: {self.year}
    Rated: {self.rated}
    Released: {self.released}
    Runtime: {self.runtime}
    Genre: {self.genre}
    Director: {self.director}
    Writer: {self.writer}
    Actors: {self.actors}
    Plot: {self.plot}
    Language: {self.language}
    Country: {self.country}
    Awards: {self.awards}
    Poster: {self.poster}
    Ratings: {self.ratings}
    Metascore: {self.metascore}
    IMDB Rating: {self.imdbRating}
    IMDB Votes: {self.imdbVotes}
    IMDB ID: {self.imdbID}
    Type: {self.type}
            """
