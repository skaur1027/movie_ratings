"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    return movie


def get_movies():
    all_movies = Movie.query.all()
    return all_movies


def get_movie_by_id(movie_id):
    movie = Movie.query.get(movie_id)
    return movie


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating

def get_users():
    all_users = User.query.all()
    return all_users


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user

def get_user_by_email(email):
    """Show details on a particular user."""
    
    return User.query.filter(User.email == email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)