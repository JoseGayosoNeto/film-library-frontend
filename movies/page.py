import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Os Mercenários'   
    },
    {
        'id': 3,
        'name': 'De volta para o futuro'
    },
]

def show_movies_page():
    
    st.write('Movies List')

    AgGrid(
        data = pd.DataFrame(movies),
        key = 'movies_grid',
        fit_columns_on_grid_load = True,
    )
    