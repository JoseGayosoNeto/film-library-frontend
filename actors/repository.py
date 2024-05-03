from login.service import logout
import os
import requests
import streamlit as st


class ActorRepository:

    def __init__(self):
        self.__base_url = os.environ.get('BASE_URL')
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            url=self.__actors_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:  # Token expired
            logout()

        raise Exception(f'Error getting data from API. Status Code: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            url=self.__actors_url,
            headers=self.__headers,
            data=actor,
        )

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            logout()

        raise Exception(f'Error getting data from API. Status Code: {response.status}')
