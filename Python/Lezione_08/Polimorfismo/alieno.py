class Alieno:

    def __init__(self, galaxy: str):

        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy: str) -> None:

        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore, la Galassia di\
 provenienza non deve essere una stringa vuota!")
    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia\
 {self.getGalaxy}"
    
    def speak(self) -> None:
        print("aipdfgcausldhcnkuzxefgynoiauefnh")