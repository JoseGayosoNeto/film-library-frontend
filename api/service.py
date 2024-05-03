import os
import requests


class Authentication:

    def __init__(self):
        self.__base_url = os.environ.get('BASE_URL')
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_authentication_token(self, username, password):

        auth_payload = {
            'username': username,
            'password': password,
        }

        auth_response = requests.post(
            url=self.__auth_url,
            data=auth_payload
        )

        if auth_response.status_code == 200:
            return auth_response.json()

        return {'error': f'Error authenticating. Status Code: {auth_response.status_code}'}
