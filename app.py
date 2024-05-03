from login.page import show_login_page
import streamlit as st
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')

def main():
    
    if 'token' not in st.session_state:
        show_login_page()
    else:
        st.title("Film Library App")

        menu_option = st.sidebar.selectbox(
            'Select an option',
            ['Home', 'Genres', 'Actors', 'Movies', 'Reviews'],
        )
        
        if menu_option == 'Home':
            from home.page import show_home_page
            show_home_page()
            
        elif menu_option == 'Genres':
            from genres.page import show_genres_page
            show_genres_page()
            
        elif menu_option == 'Actors':
            from actors.page import show_actors_page
            show_actors_page()
            
        elif menu_option == 'Movies':
            from movies.page import show_movies_page
            show_movies_page()
            
        elif menu_option == 'Reviews':
            from reviews.page import show_reviews_page
            show_reviews_page()
        
if __name__ == "__main__":
    main()
