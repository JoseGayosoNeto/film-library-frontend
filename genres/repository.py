from login.service import logout
import os
import requests
import streamlit as st


class GenreRepository:

    def __init__(self):
        self.__base_url = os.environ.get('BASE_URL')
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):

        response = requests.get(
            url=self.__genres_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:  # Token expired
            logout()

        raise Exception(f'Error getting data from API. Status Code: {response.status_code}')

    def create_genres(self, genre):

        response = requests.post(
            url=self.__genres_url,
            headers=self.__headers,
            data=genre,
        )

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:  # Token expired
            logout()

        raise Exception(f'Error getting data from API. Status Code: {response.status_code}')
