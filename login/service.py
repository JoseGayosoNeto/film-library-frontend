import streamlit as st
from api.service import Authentication


def login(username, password):
    auth_service = Authentication()
    
    response = auth_service.get_authentication_token(username, password)
    if response.get('error'):
        st.error(f"Error when logging in: {response.get('error')}.")
    else:
        st.session_state.token = response.get('access')
        st.rerun()