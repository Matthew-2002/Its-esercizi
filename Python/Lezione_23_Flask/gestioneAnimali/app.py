from abc import ABC, abstractmethod
import json
from flask import Flask, jsonify, url_for
import requests



class Animal(ABC):

    animal_id: str
    name: str
    age_years: int
    weight_kg: float

    def __init__(self,
        animal_id: str,
        name: str,
        age_years: int,
        weight_kg: float
    ) -> None:
        self.animal_id = animal_id
        self.name = name
        self.age_years = age_years
        self. weight_kg = weight_kg

    @abstractmethod
    def species(self) -> str:
        pass

    @abstractmethod
    def daily_food_grams(self) -> int:
        pass

    def info(self) -> dict[str,str]:
        info = {
            "id": self.animal_id, 
            "name": self.name, 
            "species": self.species(),
            "age_years": self.age_years, 
            "weight_kg": self.weight_kg
        }
        return info
    
    def get_bmi(self) -> float:
        return self.weight_kg / (self.age_years + 1)
    

class Dog(Animal):

    breed: str
    is_trained: bool

    def __init__(self,
        animal_id: str,
        name: str,
        age_years: int,
        weight_kg: float,
        breed: str,
        is_trained: bool
    ) -> None:
        super().__init__(
            animal_id,
            name,
            age_years,
            weight_kg
        )
        self.breed = breed
        self.is_trained = is_trained

    def species(self):
        return "dog"
    
    def daily_food_grams(self):
        return  200 + self.age_years * 50
    
    def info(self):
        info: dict[str: str|bool] = super().info()
        info["breed"] = self.breed
        info["is_trained"] = self.is_trained
        return info
    

class Cat(Animal):

    indoor_only: bool
    favorite_toy: str

    def __init__(self,
        animal_id: str,
        name: str,
        age_years: int,
        weight_kg: float,
        indoor_only: bool,
        favorite_toy: str
    ) -> None:
        super().__init__(
            animal_id,
            name,
            age_years,
            weight_kg
        )
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species(self):
        return "cat"
    
    def daily_food_grams(self):
        return 100 + self.age_years * 30 

    def info(self):
        info: dict[str: str|bool] = super().info()
        info["indoor_only"] = self.indoor_only
        info["favorite_toy"] = self.favorite_toy
        return info    


class Shelter:

    animals: dict[str, Animal]
    adoptions: dict[str, str]

    def __init__(self):
        self.animals = {}
        self.adoptions = {}

    def add(self,
        animal: Animal
    ) -> str|int:
        if animal.animal_id in self.animals:
            return {"Errore" : "Animale già presente nel sistema"}, 400
        if animal.animal_id and type(animal.animal_id) == str:
            self.animals[animal.animal_id] = animal
            return 201
        
    def get(self,
        animal_id
    ) -> Animal|int:
        if animal_id in self.animals:
            return self.animals[animal_id], 200
        return {"Errore" : "Animale non presente nel sistema"}, 400
    
    def list_all(self) -> list[Animal]:
        animal_list = []
        if not self.animals:
            return {"Errore" : "Non ci sono animali presenti nel sistema"}, 400
        for value in self.animals.values():
            animal_list.append(value.info())
        return animal_list, 200
    
    def is_adopted(self,
        animal_id
    ) -> str|bool|int:
        if animal_id not in self.animals:
            return {"Errore" : "Animale non presente nel sistema"}, 400
        if animal_id in self.adoptions:
            return True, 200
        return False, 200
    
    def set_adopted(self,
        animal_id,
        adopter_name
    ) -> str|int:
        if animal_id not in self.animals:
            return {"Errore" : "Animale non presente nel sistema"}, 400
        if animal_id in self.adoptions:
            return {"Errore" : "Animale già risulta adottato"}, 400
        self.adoptions[animal_id] = adopter_name
        return 201
    
app = Flask(__name__)

s: Shelter = Shelter()


@app.route('/')
def home():
    return jsonify({"message": "Welcome to Animal Shelter API",
                    "links": { 
                        "getAnimals": url_for("getAnimals"), 
                        "getAnimal": url_for("getAnimal", animal_id="d1"),
                        "getAnimalFood": url_for("getAnimalFood", animal_id="d1"),
                        }
                    })


@app.route('/animals', methods=["GET"])
def getAnimals():
    infoAll: dict = {}
    for animal_id, animal in s.animals.items():
        infoAll[animal_id] = animal.info()
    return jsonify(infoAll)

@app.route('/animals/<animal_id>', methods=["GET"])
def getAnimal(animal_id):
    if animal_id in s.animals:
        return jsonify(s.animals[animal_id].info()), 200
    return jsonify({"Errore" : "Animale non presente nel sistema"}), 400

@app.route('/animals/<animal_id>/food', methods=["GET"])
def getAnimalFood(animal_id):
    if animal_id in s.animals:
        return jsonify({
            "id": animal_id,
            "daily_food_grams": s.animals[animal_id].daily_food_grams()
        }), 200
    return jsonify({"Errore" : "Animale non presente nel sistema"}), 400
    
@app.route('/animals/<animal_id>/adopted', methods=["GET"])
def getAdoption(animal_id):
    if animal_id in s.animals:
        if not s.animals[animal_id].is_adopted():
            return jsonify({
                "id": animal_id,
                "adopted": s.animals[animal_id].is_adopted()
            }), 200
        return jsonify({
                "id": animal_id,
                "adopted": s.animals[animal_id].is_adopted(),
                "adopter_name": s.adoptions[animal_id]
            }), 200
    return jsonify({"Errore" : "Animale non presente nel sistema"}), 400


@app.route('/animals/add', methods=['POST'])
def addAnimal():
    load: json = requests.get_json()
    match load["type"]:
        case "dog":
            c = Dog(
                load["id"], load["name"],
                load["age_years"],load["weight_kg"],
                load[ "breed"],load["is_trained"]
            )

    



        

    

        


