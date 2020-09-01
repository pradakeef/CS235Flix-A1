import pytest
from movie import Movie, MovieFileCSVReader
from director import Director
from movie import Actor
from genre import Genre
from movie import Review
from movie import User
from movie import WatchList


def test_title():
    movie = Movie("Moana", 2009)
    print(movie)


def test_description():
    movie = Movie("Moana", 2009)
    print(movie)

    movie3 = Movie("Moana", 2010)
    print(movie3)

    movie2 = Movie("Inception", 2010)
    print(movie2)

    print(movie > movie2)
    print(movie < movie3)
    print(movie3 == movie3)

    director = Director("Ron Clements")
    movie.director = director
    print(movie.director)

    director = Director("Christopher Nolan")
    movie2.director = director
    print(movie2.director)

    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie.add_actor(actor)
    movie.remove_actor(Actor("Auli'i Cravalho"))
    print(movie.actors)

    movie.runtime_minutes = 109
    print("Movie runtime: {} minutes".format(movie.runtime_minutes))


def test_read_csv_file():
    filename = 'Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
    print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
    print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
    print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')

    all_directors_sorted = sorted(movie_file_reader.dataset_of_directors)
    print(f'first 3 unique directors of sorted dataset: {all_directors_sorted[0:3]}')

    all_actors_sorted = sorted(movie_file_reader.dataset_of_actors)
    print(f'first 3 unique directors of sorted dataset: {all_actors_sorted[0:3]}')

    all_movies_sorted = sorted(movie_file_reader.dataset_of_movies)
    print(f'first 3 unique directors of sorted dataset: {all_movies_sorted[0:3]}')


def test_movie():
    movie = Movie("Moana", 2016)
    review_text = Movie("Me", 2324)
    rating = 100
    review = Review(movie, review_text, rating)
    review2 = Review(movie, review_text, rating)

    print(review.movie)
    print("Review: {}".format(review.review_text))
    print("Rating: {}".format(review.rating))

    print(review2 == review)
    print(review2 == review)
    print(review2.timestamp)
    print(review.timestamp)


def test_user_name():
    user1 = User('Martin', 'pw12345')
    user4 = User('Martin', 'pw12345')
    user2 = User('Ian', 'pw67890')
    user3 = User('Daniel', 'pw87465')

    movie = Movie("Moana", 2009)
    review_text = "It was so average"
    rating = 10
    review = Review(movie, review_text, rating)
    print(movie)
    movie.runtime_minutes = 107

    movie3 = Movie("", 4545)
    print(movie3)

    movie2 = Movie("Inception", 2010)
    movie2.runtime_minutes = 133
    user1.watch_movie(movie)
    user1.watch_movie(movie2)
    user1.watch_movie(movie)
    user2.add_review(review)
    print(user1)
    print(user2)
    print(user3)
    print(user1 == user4)
    print(user1 > user2)
    print(user1.time_spent_watching_movies_minutes)
    print(user2.reviews)
    print(user1.watched_movies)


def test_select_movie_to_watch():
    # init watchlist
    watchlist = WatchList()
    print(f"Size of watchlist: {watchlist.size()}")

    # check_size
    watchlist = WatchList()
    print(f"Size of watchlist: {watchlist.size()}")

    # check_size_of_nonempty_watchlist
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    print(f"Size of watchlist: {watchlist.size()}")

    #check_add_movie
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    print(f"Size of watchlist: {watchlist.size()}")


    #check add_same_movie_again
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Moana", 2016))
    print(f"Size of watchlist: {watchlist.size()}")

    #check_remove_movie_in_list
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.remove_movie(Movie("Moana", 2016))
    print(f"Size of watchlist: {watchlist.size()}")

    #check_remove_movie_not_in_list
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
    print(f"Size of watchlist: {watchlist.size()}")

    #check_select_movie_to_watch_index_ok
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    print(watchlist.select_movie_to_watch(2))

    #check_select_movie_to_watch_index_out_of_bounds
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.add_movie(Movie("Split", 2016))
    print(watchlist.select_movie_to_watch(4))

    #check_iterator_reaches_final_element
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    watchlist.add_movie(Movie("Split", 2016))
    watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
    for movie in watchlist:
        print(movie)










