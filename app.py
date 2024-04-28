import streamlit as st


def main():
    st.title("Film Library App")

    menu_option = st.sidebar.selectbox(
        'Select an option',
        ['Home', 'Genres', 'Actors', 'Movies', 'Reviews'],
    )
    
    if menu_option == 'Home':
        st.write('Home')
        
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
