from movies.repository import MovieRepository
import streamlit as st


class MovieService():
    
    def __init__(self):
        self.__movie_repository = MovieRepository()
        
    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.__movie_repository.get_movies()
        st.session_state.movies = movies
        
        return movies
    
    def create_movies(self, title, release_date, genre, actors, resume):
        movie = dict(
            title= title,
            release_date = release_date,
            genre = genre,
            actors = actors,
            resume = resume,
        )
        new_movie = self.__movie_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        
        return new_movie

    def get_movie_stats(self):
        return self.__movie_repository.get_movies_stats()