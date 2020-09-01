#Assignment 1 Flix Project
#COMPSCI235
#aman290
#365403795
#Aniketh Mantravadi

import csv
import datetime

from typing import List


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return not self < other and not other < self
        pass

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name
        pass

    def __hash__(self):
        return hash(self.__director_full_name)
        pass


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        return not self < other and not other < self
        pass

    def __lt__(self, other):
        return self.__genre_name < other.__genre_name
        pass

    def __hash__(self):
        return hash(self.__genre_name)
        pass


class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        self.colleague_list = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def add_actor_colleague(self, colleague):
        self.colleague_list.append(colleague.__actor_full_name)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague.__actor_full_name in self.colleague_list:
            return True
        else:
            return False

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return not self < other and not other < self
        pass

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name
        pass

    def __hash__(self):
        return hash(self.__actor_full_name)
        pass


class Movie:

    def __init__(self, title: str, release_year: int):
        if type(title) is not str:
            self.__title = None
        elif title == "":
            self.__title = None
        else:
            self.__title = title.strip()

        if release_year <= 1900 or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year

        if self.__title is not None or self.__release_year:
            self.uniqueID: str = f"{self.__title}_{self.__release_year}"
        else:
            self.uniqueID: str = ""
        self.actor: Actor
        self.genre: Genre
        self.__description: str
        self.__director: Director
        self.__actors: List[Movie.Actor] = list()
        self.__genres: List[Movie.Genre] = list()
        self.__runtime_minutes: int

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, desc: str):
        self.__description = desc.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, direc: Director):
        self.__director = direc


    @property
    def actors(self) -> List[Actor]:
        return self.__actors

    @property
    def genres(self) -> List[Genre]:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, r: int):
        error = (r < 0)
        if error:
            raise ValueError
        else:
            self.__runtime_minutes = r


    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            i: int = self.__actors.index(actor)
            self.__actors.pop(i)
        else:
            pass

    def add_actor(self, actor: Actor):
        if actor not in self.__actors:
            self.__actors.append(actor)
        else:
            pass

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            i: int = self.__genres.index(genre)
            self.__genres.pop(i)
        else:
            pass

    def add_genre(self, genre: Genre):
        if genre not in self.__genres:
            self.__genres.append(genre)
        else:
            pass


    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):

        return not self.uniqueID < other.uniqueID and not other.uniqueID < self.uniqueID
        pass

    def __lt__(self, other):

        return self.uniqueID < other.uniqueID
        pass

    def __hash__(self):

        return hash(self.uniqueID)
        pass

class ValueError(Exception):
    pass


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        rating_list = [1,2,3,4,5,6,7,8,9,10]
        if type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie

        if type(review_text) is not str:
            self.__review_text = None
        elif review_text == "":
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()

        if 10 < rating < 1 or type(rating) is not int:
            self.__rating = None
        elif 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp: datetime = datetime.datetime.now().timestamp()
        self.uniqueID: str = f"{self.__movie}_{self.__review_text}_{self.__rating}_{self.__timestamp}"


    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie: Movie):
        if movie == Movie() or type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie

        self.__timestamp: datetime = datetime.datetime.now().timestamp()

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, review_text: str):
        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()

        self.__timestamp: datetime = datetime.datetime.now().timestamp()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        if 10 < rating < 1 or type(rating) is not int:
            self.__rating = None
        elif 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp: datetime = datetime.datetime.now().timestamp()

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__review_text}, {self.__rating}, {self.__timestamp}>"

    def __eq__(self, other):
        return not self.uniqueID < other.uniqueID and not other.uniqueID < self.uniqueID
        pass

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


class WatchList:

    def __init__(self):
        self.__watchlist: List[Movie] = list()

    def add_movie(self, movie: Movie):
        if type(movie) is not Movie:
            pass
        elif movie not in self.__watchlist:
            self.__watchlist.append(movie)
        else:
            pass

    def remove_movie(self, movie: Movie):
        if type(movie) is not Movie:
            pass
        elif movie in self.__watchlist:
            i: int = self.__watchlist.index(movie)
            self.__watchlist.pop(i)
        else:
            pass

    def select_movie_to_watch(self, index: int):
        if index < 0 or index > len(self.__watchlist)-1:
            return None
        else:
            return self.__watchlist[index]

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) == 0:
            return None
        else:
            return self.__watchlist[0]

    def size(self):
        return len(self.__watchlist)

    def __iter__(self):
        self._index = 0
        return iter(self.__watchlist)

    def __next__(self):
        ''''Returns the next value from watchlist object's lists '''
        if self._index < len(self.__watchlist):
            return self.__watchlist[self.index]
            self._index += 1
        # End of Iteration
        raise StopIteration



class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name

        self.dataset_of_movies: List[Movie] = list()
        self.dataset_of_actors: List[Actor] = list()
        self.dataset_of_directors: List[Director] = list()
        self.dataset_of_genres: List[Genre] = list()

        self.movies: List[Movie] = list()
        self.actors: List[Actor] = list()
        self.directors: List[Director] = list()
        self.genres: List[Genre] = list()
        self.year: List[int] = list()


    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)



            for row in movie_file_reader:
                self.movies.append(row['Title'])
                self.actors.append(row['Actors'])
                self.genres.append(row['Genre'])
                self.directors.append(row['Director'])
                self.year.append(int(row['Year']))

            index = 0
            for mov in self.movies:
                mov = mov.split(',')
                mov = " ".join(mov)

                if Movie(mov, self.year[index]) not in self.dataset_of_movies:
                    self.dataset_of_movies.append(Movie(mov, self.year[index]))
                else:
                    pass
                index += 1



            for actor in self.actors:
                list_actors = actor.split(',')
                for act in list_actors:
                    act = act.split()
                    act = " ".join(act)
                    if Actor(act) not in self.dataset_of_actors:
                        self.dataset_of_actors.append(Actor(act))
                    else:
                        pass

            for genre in self.genres:
                list_genre = genre.split(',')
                for gen in list_genre:
                    gen = gen.split()
                    gen = " ".join(gen)
                    if Genre(gen) not in self.dataset_of_genres:
                        self.dataset_of_genres.append(Genre(gen))
                    else:
                        pass

            for director in self.directors:
                list_directors = director.split(',')
                for dir in list_directors:
                    dir = dir.split()
                    dir = " ".join(dir)
                    if Director(dir) not in self.dataset_of_directors:
                        self.dataset_of_directors.append(Director(dir))
                    else:
                        pass

            #print(f"{len(self.movies)}, {len(self.dataset_of_actors)}, {len(self.dataset_of_genres)}, {len(self.dataset_of_directors)}")


