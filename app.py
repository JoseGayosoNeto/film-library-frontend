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
        st.write('Actors')
        
    elif menu_option == 'Movies':
        st.write('Movies')
        
    elif menu_option == 'Reviews':
        st.write('Reviews')
    
if __name__ == "__main__":
    main()
