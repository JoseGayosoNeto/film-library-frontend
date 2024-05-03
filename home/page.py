from movies.service import MovieService
import plotly.express as px
import streamlit as st



def show_home_page():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()
    
    st.title('Movie Stats')
    
    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Movies by genre:')
        figure = px.pie(
            data_frame = movie_stats['movies_by_genre'],
            values = 'count',
            names = 'genre__name',
            title = 'Movies by Genre'
        )
        st.plotly_chart(figure)
        
    st.subheader('Total movies registered:')
    st.write(movie_stats['total_movies'])
    
    st.subheader('Numbers of movies by genre:')
    for genre in movie_stats['movies_by_genre']:
        st.write(f"{genre['genre__name']}: {genre['count']}")    
    
    st.subheader('Number of registered reviews:')
    st.write(movie_stats['total_reviews'])
    
    st.subheader('Overall average rating stars:')
    st.write(movie_stats['average_stars'])
    