"""
Script to seed database.
"""

import os
import json
from random import choice, randint
from datetime import datetime
from turtle import clear
from random import choice, randint

import model
import server
import crud

os.system('dropdb ratings')
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()


with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    title, overview, poster_path = (movie["title"], movie["overview"], movie["poster_path"])
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

users_in_db = []
for n in range(10):
    email, password = f'user{n}@test.com', 'test'  # Voila! A unique email!
    db_user = crud.create_user(email, password)
    users_in_db.append(db_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()

ratings_in_db = []
for i in range(10):
    for user in users_in_db:
        db_rating = crud.create_rating(user, choice(movies_in_db),randint(1, 5))
        ratings_in_db.append(db_rating)


model.db.session.add_all(ratings_in_db)
model.db.session.commit()