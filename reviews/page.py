from movies.service import MovieService
import pandas as pd
from reviews.service import ReviewService
import streamlit as st
from st_aggrid import AgGrid


def show_reviews_page():
    review_service = ReviewService()

    reviews = review_service.get_reviews()
    if reviews:

        st.write('Reviews List')

        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            key='reviews_grid',
            fit_columns_on_grid_load=True,
        )

        st.divider()
    else:
        st.warning('No reviews found.')

    st.title('Register New Review')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movies_titles = {movie['title']: movie['id'] for movie in movies}

    selected_movie_titles = st.selectbox(
        label='Movie',
        options=list(movies_titles.keys())
    )

    stars = st.number_input(
        label='Stars',
        min_value=0,
        max_value=5,
        step=1
    )

    comment = st.text_area('Comment')

    if st.button('Register'):
        new_review = review_service.create_review(
            movie=movies_titles[selected_movie_titles],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Error when registering review. Check the fields.')
