'''
This file consists Movie class definition
'''
# webbrowser module imported
import webbrowser


class Movie():
    ''' This is a Movie class definition
    It takes seven parameters:

    Parameters' description format:
    parameter(datatype): description

    //Parameter description
    self: Refers to the Movie instance that is being created
    movie_title(string): Contains name of the movie.
    movie_storyline(string): Contains storyline of the movie.
    movie_poster(string): This is a string consisting of a URL
    of the movie poster.
    movie_trailer(string): URL of movie's trailer.
    movie_rating(string): IMDb rating of the movie.
    movie_genre(string): Genre of the movie.
    //Parameter description ends

    Movie class takes all these parameters and returns an instance with
    the values passed.
    '''
    def __init__(self, movie_title, movie_storyline, movie_poster,
                 movie_trailer, movie_rating, movie_genre):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster = movie_poster
        self.trailer = movie_trailer
        self.rating = movie_rating
        self.genre = movie_genre

# Function show_traileris defined
    def show_trailer(self):
        '''show_trailer function defined
        Description: Plays trailer of the instance it is called with.
        Example: a.show_trailer plays the trailer of 'a' movie.
        '''
        webbrowser.open(self.trailer)
