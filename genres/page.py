import streamlit as st


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

    st.table(genres)
    
    st.divider()
    
    st.title('Register New Genre')
    
    name = st.text_input('Genre Name', placeholder='Enter your genre here.')
    if st.button('Register'):
        st.success(f'Genre {name} registered successfully.')
        