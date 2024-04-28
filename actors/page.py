import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Leonardo Di Caprio',
    },
    {
        'id': 2,
        'name': 'Chris Rock'
    },
    {
        'id': 3,
        'name': 'Sylvester Stallone'
    },
]

def show_actors_page():
    
    st.write('Actors List')
    
    AgGrid(
        data = pd.DataFrame(actors),
        key = 'actors_grid',
        fit_columns_on_grid_load = True,
    )
    
    st.divider()
    
    st.title('Register New Actor')
    
    name = st.text_input('Actor Name', placeholder= 'Enter your actor here.')
    if st.button('Register'):
        st.success(f'Actor {name} sucessfully registered.')
