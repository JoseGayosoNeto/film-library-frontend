from datetime import datetime
from enum import Enum
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService

def show_actors_page():
    actor_service = ActorService()
    actors = actor_service.get_actors()
    if actors:
        st.write('Actors List')
        
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data = actors_df,
            key = 'actors_grid',
            fit_columns_on_grid_load = True,
        )
    
        st.divider()
    else:
        st.warning('No actors found.')
    
    st.title('Register New Actor')
    
    name = st.text_input('Actor Name', placeholder= 'Enter your actor here.')
    date_of_birth = st.date_input(
        label = "Actor's birthday",
        value = datetime.today(),
        min_value = datetime(1600, 1, 1).date(),
        max_value = datetime.today(),
        format = 'MM/DD/YYYY',
    )
    
    class NationalityDropdown(Enum):
        USA = 'United States of America'
        CHN = 'China'
        JPN = 'Japan'
        DEU = 'Germany'
        IND = 'India'
        GBR = 'United Kingdom'
        FRA = 'France'
        ITA = 'Italy'
        BRA = 'Brazil'
        CAN = 'Canada'
        RUS = 'Russia'
        KOR = 'South Korea'
        AUS = 'Australia'
        ESP = 'Spain'
        MEX = 'Mexico'
        IDN = 'Indonesia'
        TUR = 'Turkey'
        SAU = 'Saudi Arabia'
        CHE = 'Switzerland'
        NLD = 'Netherlands'
    
    nationality = st.selectbox(
        label = "Actor's nationality",
        options = [nationality.value for nationality in NationalityDropdown],
    )
    # Get Enum.name for the respective nationality value to insert in db
    nationality_name = next((n.name for n in NationalityDropdown
                            if n.value == nationality), None)
    if st.button('Register'):
        new_actor = actor_service.create_actors(name, date_of_birth, nationality_name)
        if new_actor:
            st.rerun()
        else:
            st.error('Error when registering actor. Check the fields.')