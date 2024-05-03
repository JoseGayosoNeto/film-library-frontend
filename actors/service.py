from actors.repository import ActorRepository
import streamlit as st


class ActorService:

    def __init__(self):
        self.__actor_repository = ActorRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.__actor_repository.get_actors()
        st.session_state.actors = actors

        return actors

    def create_actors(self, name, date_of_birth, nationality):
        actor = dict(
            name=name,
            date_of_birth=date_of_birth,
            nationality=nationality,
        )

        new_actor = self.__actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor
