from movies.repository import MovieRepository
import streamlit as st


class MovieService():
    
    def __init__(self):
        self.__movie_repository = MovieRepository()
        
    def get_movies(self):
        return self.__movie_repository.get_movies()
    
    def create_movies(self, title, release_date, genre, actors, resume):
        movie = dict(
            title= title,
            release_date = release_date,
            genre = genre,
            actors = actors,
            resume = resume,
        )
        
        return self.__movie_repository.create_movie(movie)

    def get_movie_stats(self):
        return self.__movie_repository.get_movies_stats()