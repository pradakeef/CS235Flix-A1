from movie import Movie
import datetime

class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        rating_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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
        if type(movie) is not Movie:
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