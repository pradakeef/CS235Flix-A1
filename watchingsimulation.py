from user import User
from movie import Movie
from review import Review

class MovingWatchingSimulation:
    user1 = User('BigCinema', 'pw12345')
    user4 = User('Hoyts', 'pw12345')
    user2 = User('Events', 'pw67890')
    user3 = User('ReadingCinema', 'pw87465')

    movie = Movie("Rogue One", 2016)
    review_text = "It was really average"
    rating = 10
    review = Review(movie, review_text, rating)
    print(movie)
    movie.runtime_minutes = 133

    movie3 = Movie("", 4545)
    print(movie3)

    movie2 = Movie("Inception", 2010)
    movie2.runtime_minutes = 133
    user1.watch_movie(movie)
    user1.watch_movie(movie2)
    user1.watch_movie(movie)
    user2.add_review(review)
    print(user1)
    print(user4)
    print(user2)
    print(user3)
    print(user1 == user4)
    print(user1 > user2)
    print(user1.time_spent_watching_movies_minutes)
    print(user2.reviews)
    print(user1.watched_movies)