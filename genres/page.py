import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comédia'   
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]

def show_genres_page():
    
    st.write('Genres List')

    AgGrid(
        data = pd.DataFrame(genres),
        key = 'genres_grid',
        fit_columns_on_grid_load = True,
    )
    
    st.divider()
    
    st.title('Register New Genre')
    
    name = st.text_input('Genre Name', placeholder='Enter your genre here.')
    if st.button('Register'):
        st.success(f'Genre {name} registered successfully.')
        