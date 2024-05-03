import streamlit as st
from login.service import login


def show_login_page():
    st.title('Login')

    username = st.text_input('Username', placeholder='Enter your username here.')
    password = st.text_input(
        label='Password',
        type='password',
        placeholder='Enter your password here.',
    )

    if st.button('Login'):
        login(
            username=username,
            password=password,
        )
