from movie import Movie
from typing import List

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
        if index < 0 or index > len(self.__watchlist) - 1:
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
        if self._index < len(self.__watchlist):
            return self.__watchlist[self._index]
            self._index += 1
        # End of Iteration
        raise StopIteration