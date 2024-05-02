from actors.repository import ActorRepository


class ActorService:
    
    def __init__(self):
        self.__actor_repository = ActorRepository()
    
    def get_actors(self):
        return self.__actor_repository.get_actors()
        
    def create_actors(self, name, date_of_birth, nationality):
        actor = dict(
            name = name,
            date_of_birth = date_of_birth,
            nationality = nationality,
        )
        
        return self.__actor_repository.create_actor(actor)
