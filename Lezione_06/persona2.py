class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

    def displayData(self) -> None:
        print(f"Dati:\n    nome: {self.name}\n    cognome: {self.lastname}\n    età: {self.age}")
    
    def setName(self, name):
        self.name = name

    def setLastname(self, lastname):
        self.lastname = lastname

    def setAge(self, age):
        if age < 0:
            print("Errore: età negativa")
        else:
            self.age = age
    
    def getName(self) -> str:
        return self.name
    
    def getLastname(self) -> str:
        return self.lastname
    
    def getAge(self) -> int:
        return self.age

        