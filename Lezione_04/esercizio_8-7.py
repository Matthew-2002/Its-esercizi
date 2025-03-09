'''8-7. Album: Write a function called make_album() that 
builds a dictionary describing a music album. The function 
should take in an artist name and an album title, and it 
should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries 
representing different albums. Print each return value to 
show that the  dictionaries are storing the album information 
correctly. Use None to add an optional parameter to make_album() 
that allows you to store the number of songs on an album. If 
the calling line includes a value for the number of songs, add 
that value to the album’s dictionary. Make at least one new 
function call that includes the number of songs on an album.
'''



def make_album(artist: str, title: str, numero_canzoni: str =None):
    album: dict[str] = {
                        "Artist": artist, 
                        "Title": title, 
                        "number of songs": numero_canzoni
                        }
    return album

def print_album(album: dict[str]):
    for key, value in album.items():
        print(f"{key}: \"{value}\"", end= " | ")
    print()

print_album(make_album("Michael Jackson", "Thriller"))

print_album(make_album("Pink Floyd", "The Dark Side of the Moon"))

print_album(make_album("AC/DC","Back in Black"))

print_album(make_album("Michael Jackson", "Thriller", "9"))

