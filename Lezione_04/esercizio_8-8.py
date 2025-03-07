'''8-8. User Albums: Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist 
and title. Once you have that information, call make_album() with 
the user’s input and print the dictionary that’s created. Be sure 
to include a quit value in the while loop.'''


def make_album(artist: str, title: str, numero_canzoni: int =None):
    album: dict[str] = {
                        "Artist": artist, 
                        "Title": title, 
                        "number of songs": numero_canzoni
                        }
    return album

while True:
    
    nome_artista: str = input("Inserisci nome artista/stop: ")
    if nome_artista == "stop":
        break
    
    titolo: str = input("Inserisci titolo album/stop: ")
    if titolo == "stop":
        break
    
    nstr_song: str = str(input("Inserisci numero di canzoni: "))
    if nstr_song.isdigit() == True:
        n_song: int = int(nstr_song)
    else:
        n_song = "Unknown"

    input_album: dict[str, str|int] = make_album(nome_artista, titolo, n_song)
    print(f"Nome arista: {input_album['Artist']}, titolo album: {input_album['Title']}, Numero canzoni: {input_album['number of songs']}")