from actors.service import ActorService
from datetime import datetime
from genres.service import GenreService
from movies.service import MovieService
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


def show_movies_page():
    movie_service = MovieService()
    
    movies = movie_service.get_movies()
    if movies: 
        
        st.write('Movies List')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data = movies_df,
            key = 'movies_grid',
            fit_columns_on_grid_load = True,
        )
        
        st.divider()
    else:
        st.warning('No movies found.')
        
    st.title('Register New Movie')
    
    title = st.text_input('Movie Title')
    
    release_date = st.date_input(
        label = 'Release Date',
        value = datetime.today(),
        min_value = datetime(1600, 1, 1).date(),
        max_value = datetime.today(),
        format = 'MM/DD/YYYY'
    )
    
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genres_names = {genre['name']: genre['id'] for genre in genres}
    
    selected_genre_name = st.selectbox(
        label = 'Genre',
        options = list(genres_names.keys()),
    )
    
    actor_service = ActorService()
    actors = actor_service.get_actors()
    actors_names = {actor['name']: actor['id'] for actor in actors}
    
    selected_actors_names = st.multiselect(
        label = 'Actor',
        options = list(actors_names.keys())
    )
    
    selected_actors_ids = [actors_names[name] for name in selected_actors_names]
    
    resume = st.text_area('Resume')
    
    if st.button('Register'):
        new_movie = movie_service.create_movies(
            title = title,
            release_date = release_date,
            genre = genres_names[selected_genre_name],
            actors = selected_actors_ids,
            resume = resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Error when registering movie. Check the fields.')
    