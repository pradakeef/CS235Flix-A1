# Assignment 1 Flix Project
# COMPSCI235
# aman290
# 365403795
# Aniketh Mantravadi

from actor import Actor
from director import Director
from genre import Genre
from typing import List


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
        self.__external_rating: float
        self.__votes: int
        self.__revenue: float
        self.__metascore: int

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

    @property
    def external_rating(self) -> float:
        return self.__external_rating

    @external_rating.setter
    def external_rating(self, e: float):
        error = (10 < e < 0)
        if error or type(e) is not float:
            raise ValueError
        else:
            self.__external_rating = e

    @property
    def votes(self) -> int:
        return self.__votes

    @votes.setter
    def votes(self, v: int):
        error = (v < 0)
        if type(v) is not int:
            raise ValueError
        elif error:
            raise ValueError
        else:
            self.__votes = v

    @property
    def revenue(self) -> float:
        return self.__revenue

    @revenue.setter
    def revenue(self, rev: float):
        error = (rev < 0)
        if type(rev) is not float:
            raise ValueError
        elif error:
            raise ValueError
        else:
            self.__revenue = rev

    @property
    def metascore(self) -> int:
        return self.__metascore

    @metascore.setter
    def metascore(self, m: int):
        error = (100 < m < 0)
        if type(m) is not int:
            raise ValueError
        elif error:
            raise ValueError
        else:
            self.__metascore = m

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
