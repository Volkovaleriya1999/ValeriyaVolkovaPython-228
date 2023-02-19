import pickle
import os


class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors


    def __str__(self):
        return f'"{self.title}" {self.genre} ({self.year})'


class FilmModel:
    def __init__(self):
        self.db_name = 'db_films.txt'
        self.films = self.load_data()


    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film


    def get_all_films(self):
        return self.films.values()


    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_film = {
            'название': film.title,
            'жанр': film.genre,
            'режиссер': film.director,
            'год выпуска': film.year,
            'длительность': film.duration,
            'студия': film.studio,
            'актеры': film.actors
        }
        return dict_film


    def remove_film(self, user_film):
        return self.films.pop(user_film)


    def save_data(self):
        with open(self.db_name, 'wb') as file:
            pickle.dump(self.films, file)


    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as file:
                return pickle.load(file)
        else:
            return dict()