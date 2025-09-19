class Persona:
    def __init__(self,name:str,last_name:str,age:int):
        self.setName(name)
        self.setLast_name(last_name)
        self.setAge(age)

    # funzione che mi mostri in output i dati relativi ad una persona
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.last_name}\nEtà: {self.age}"
    
    # funzione che mi mostri in output i dati relativi ad una persona
    def __call__(self):
        if self.age < 18:
            print(f"{self.name} {self.last_name} e' minorenne!")
        elif 18 <= self.age < 30:
            print(f"{self.name} {self.last_name} e' maggiorenne!")
        elif 30<= self.age < 80:
            print(f"{self.name} {self.last_name} e' una persona adulta!")
        else:
            print(f"{self.name} {self.last_name} e' una persona anziana!")
    
    # funzione che mi consenta di impostare il valore di self.name
    def setName(self, name:str) -> None:
        if name:
            self.name = name
        else:
            print("Errore")

    # funzione che mi consenta di impostare il valore self.last_name
    def setLast_name(self,last_name:str) -> None:
        if last_name:
            self.last_name = last_name
        else:
            print("Errore")

    # finzione che mi consenta di impostare il valore di self.age
    def setAge(self, age:int) -> None:
        if age < 0 or age > 120:
            self.age = 0
        else:
            self.age = age

    # funzione che mi consenta di ritornare il valore di self.name
    def getName(self) -> str:
        return self.name
    
    # funzione che mi consenta di ritornare il valore di self.last_name
    def getLast_name(self) -> str:
        return self.last_name
    
    #funzione che mi consenta di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age
    
    def speak(self) -> None:
        print(f"\nHello! my name is {self.getName()}!\n")
    