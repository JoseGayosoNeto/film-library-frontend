import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 4   
    },
    {
        'id': 3,
        'stars': 3
    },
]

def show_reviews_page():
    
    st.write('Reviews List')

    AgGrid(
        data = pd.DataFrame(reviews),
        key = 'reviews_grid',
        fit_columns_on_grid_load = True,
    )
        