from genres.service import GenreService
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


def show_genres_page():
    genre_services = GenreService()

    genres = genre_services.get_genres()

    if genres:
        st.write('Genres List')

        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            key='genres_grid',
            fit_columns_on_grid_load=True,
        )

        st.divider()
    else:
        st.warning('No genre found.')

    st.title('Register New Genre')

    name = st.text_input('Genre Name', placeholder='Enter your genre here.')
    if st.button('Register'):
        new_genre = genre_services.create_genre(name)
        if new_genre:
            st.rerun()
        else:
            st.error('Error when registering genre. Check the fields')
