from movie import Movie
from review import Review
from typing import List

class User:

    def __init__(self, user_name: str, password: str):
        if type(user_name) is not str:
            self.__user_name = None
        elif user_name == "":
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()

        if type(password) is not str:
            self.__password = None
        elif password == "":
            self.__password = None
        else:
            self.__password = password.strip()

        self.__watched_movies: List[Movie] = list()
        self.__reviews: List[Review] = list()
        self.__time_spent_watching_movies_minutes: int = 0

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name: str):
        if type(user_name) is not str:
            self.__user_name = None
        elif user_name == "":
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        if type(password) is not str:
            self.__password = None
        elif password == "":
            self.__password = None
        else:
            self.__password = password.strip()

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def watch_movie(self, movie: Movie):
        if type(movie) is not Movie:
            pass
        elif movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes
        else:
            pass

    def add_review(self, review: Review):
        if type(review) is not Review:
            pass
        else:
            self.__reviews.append(review)

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):

        return not self.__user_name < other.__user_name and not other.__user_name < self.__user_name
        pass

    def __lt__(self, other):

        return self.__user_name < other.__user_name
        pass

    def __hash__(self):

        return hash(self.__user_name)
        pass
