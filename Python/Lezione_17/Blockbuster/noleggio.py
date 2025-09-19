from typing import Self
from film import Film
from movie_genre import *

class Noleggio:

    film_list: list[Film]
    rented_film: dict[int:list[Film]]

    def __init__(self) -> Self:
        self.film_list = []
        self.rented_film = {}

    def setFilmList(self,
        film_list
    ) -> None:
        self.film_list = film_list

    def isAvailable(self,
        film
    ) -> bool:
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")
        return False

    def rentAMovie(self,
        film,
        clientId
    ) -> None:
        if self.isAvailable(film):
            self.film_list.remove(film)
            if clientId in self.rented_film:
                self.rented_film[clientId].append(film)
            else:
                self.rented_film[clientId] = [film]
            print(f"Il cliente {clientId} ha noleggiato {film.getTitle()}!")
        else:
            print(f'Non è possibile nolegiare il film {film.getTitle()}!')

    def giveBack(self,
        film,
        clientId,
        n_giorni
    ) -> None:
        self.rented_film[clientId].remove(film)
        self.film_list.append(film)
        penale: float = n_giorni * film.getPenale()
        print(f"Cliente: {clientId}! La penale da pagare per il film {film} e' di {penale} euro!")

    def printMovies(self) -> str:
        for film in self.film_list:
            print(f'{film.getTitle()} - {film.getGenere()}')
        
    def printRentMovies(self,
        clientId
    ) -> list[Film]:
        return self.rented_film[clientId]
    
