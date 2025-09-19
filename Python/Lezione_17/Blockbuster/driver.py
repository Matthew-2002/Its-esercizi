from film import Film
from movie_genre import *
from noleggio import Noleggio

titoli: list[str] = [
    'Mad Max', 'Kill Bill', 
    'Die Hard', 'Matrix', 
    'Top Gun'
]
films: list[Film] = []
id = [i for i in range(10)]
for film in titoli:
    films.append(Azione(id[0], film))
    id.pop(0)
titoli: list[str] = [
    'A qualcuno piace caldo', 
    'Non ci resta che piangere',
    'Amici miei', 
    'Frankenstein Junior'
    ]
for film in titoli:
    films.append(Commedia(id[0], film))
    id.pop(0)

films.append(Drama(id[0], 'Parasite'))

#####


Nol1: Noleggio = Noleggio()

print('Quale film vuoi noleggiare?')

Nol1.setFilmList(films[:])

Nol1.rentAMovie(films[0], 0)
Nol1.rentAMovie(films[1], 0)
Nol1.rentAMovie(films[1], 1)
Nol1.rentAMovie(films[2], 1)
Nol1.giveBack(films[1], 0, 5)
Nol1.printMovies()