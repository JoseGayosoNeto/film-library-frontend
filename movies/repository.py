from login.service import logout
import os
import requests
import streamlit as st


class MovieRepository:

    def __init__(self):
        self.__base_url = os.environ.get('BASE_URL')
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            url=self.__movies_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()

        raise Exception(f'Error getting data from API. Status Code: {response.status_code}')

    def create_movie(self, movie):
        response = requests.post(
            url=self.__movies_url,
            headers=self.__headers,
            data=movie
        )

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            logout()

        raise Exception(f'Error getting data from API. Status Code: {response.status_code}')

    def get_movies_stats(self):
        response = requests.get(
            url=f'{self.__movies_url}stats/',
            headers=self.__headers,
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()

        raise Exception(f'Error getting data from API. Status Code: {response.status_code}')
