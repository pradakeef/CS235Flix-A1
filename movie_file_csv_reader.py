import csv
from actor import Actor
from director import Director
from genre import Genre
from typing import List
from movie import Movie

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
