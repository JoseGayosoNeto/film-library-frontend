from genres.repository import GenreRepository


class GenreService:
    
    def __init__(self):
        self.__genre_repository = GenreRepository()
        
    def get_genres(self):
        return self.__genre_repository.get_genres()
    
    def create_genre(self, name):
        
        genre = dict(
            name=name,
        )
        
        return self.__genre_repository.create_genres(genre)