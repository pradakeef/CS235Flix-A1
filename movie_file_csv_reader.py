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
        self.description: List[str] = list()
        self.runtime: List[int] = list()
        self.external_ratings: List[float] = list()
        self.votes: List[int] = list()
        self.revenues: List[float] = list()
        self.metascores: List[int] = list()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                self.movies.append(row['Title'])
                self.actors.append(row['Actors'])
                self.genres.append(row['Genre'])
                self.directors.append(row['Director'])
                self.year.append(int(row['Year']))
                self.description.append(row['Description'])
                self.runtime.append(row['Runtime (Minutes)'])
                self.external_ratings.append(row['Rating'])
                self.votes.append(row['Votes'])
                self.metascores.append(row['Metascore'])
                self.revenues.append(row['Revenue (Millions)'])

            index = 0
            for mov in self.movies:
                mov = mov.split(',')
                mov = " ".join(mov)

                movie = Movie(mov, self.year[index])
                if movie not in self.dataset_of_movies:
                    self.dataset_of_movies.append(movie)
                    movie.description = self.description[index]
                    movie.director = Director(self.directors[index])
                    for genre in self.genres[index].split(','):
                        movie.add_genre(Genre(genre))
                    for actor in self.actors[index].split(','):
                        movie.add_actor(Actor(actor))
                    if self.runtime == 'N/A':
                        pass
                    else:
                        movie.runtime_minutes = int(self.runtime[index])
                    if self.external_ratings == "N/A":
                        pass
                    else:
                        movie.external_rating = float(self.external_ratings[index])
                    if self.revenues[index] == "N/A":
                        pass
                    else:
                        movie.revenue = float(self.revenues[index])
                    if self.metascores[index] == "N/A":
                        pass
                    else:
                        movie.metascore = int(self.metascores[index])
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
