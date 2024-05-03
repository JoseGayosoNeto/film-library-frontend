from login.service import logout
import os
import requests
import streamlit as st


class ReviewRepository:

    def __init__(self):
        self.__base_url = os.environ.get('BASE_URL')
        self.__reviews_url = f'{self.__base_url}reviews/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_reviews(self):
        response = requests.get(
            url=self.__reviews_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()

        raise Exception(f'Error when getting data from API. Status Code: {response.status_code}')

    def create_review(self, review):
        response = requests.post(
            url=self.__reviews_url,
            headers=self.__headers,
            data=review,
        )

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            logout()

        raise Exception(f'Error when getting data from API. Status Code: {response.status_code}')
