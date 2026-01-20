from abc import ABC, abstractmethod

class Ride(ABC):
    
    id_ride: str
    name: str
    min_height_cm: int

    def __init__(self, 
        id_ride: str, 
        name: str, 
        min_height_cm: int
    ) -> None:
        self.id_ride = id_ride
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def base_wait(self):
        pass

    def info(self):
        info_dict: dict = {
            "id" : self.id_ride,
            "name" : self.name,
            "min height" : self.min_height_cm,
            "category" : self.category()
        }
        return info_dict

    def wait_time(self, 
        crowd_factor: float = 1
    )-> int:
        return round(self.base_wait()*crowd_factor)
    

class RollerCoster(Ride):

    id_ride: str
    name: str
    min_height_cm: int

    inversions: int

    def __init__(self, 
        id_ride, 
        name, 
        min_height_cm, 
        inversions
    ) -> None:
        super().__init__(
            id_ride, 
            name, 
            min_height_cm
        )
        self.inversions = inversions

    def category(self) -> str:
        return "roller_coaster"
    
    def base_wait(self) -> int:
        return 40
    
    def info(self):
        info_dict = super().info()
        info_dict["inversions"] = self.inversions
        return info_dict


class Carousel(Ride):

    id_ride: str
    name: str
    min_height_cm: int

    animals: list[str]

    def __init__(self,
        id_ride, 
        name, 
        min_height_cm,
        animals
    ) -> None:
        super().__init__(
            id_ride, 
            name, 
            min_height_cm
        )
        self.animals = animals

    def category(self):
        return "family"
    
    def base_wait(self):
        return 10
    
    def info(self):
        info_dict = super().info()
        info_dict["animals"] = self.animals
        return info_dict

class Park:

    rides: dict[str, Ride]

    def __init__(self) -> None:
        self.rides = {}

    def add(self,
        ride: Ride
    ) -> None:
        if ride.id_ride in self.rides:
            return "Erroe: corsa già presente"
        self.rides[ride.id_ride] = ride

    def get(self,
       id_ride
    ) -> Ride:
        return self.rides[id_ride] if id_ride in self.rides else None
    
    def list_all(self) -> list[Ride]:
        ride_list = []
        for value in self.rides.values():
            ride_list.append(value)
        oredered_ride_list = sorted(ride_list, key= lambda r: (r.category(), r.name))
        for item in oredered_ride_list:
            print(item.info())
        return oredered_ride_list
    
#r1 = RollerCoster("1", "Velociraptor", 140, 28)
#r2 = RollerCoster("2", "SpaceShip", 120, 19)
#
#r3 = Carousel("3", "Farm", 60, ["horse", "cow"])
#r4 = Carousel("4", "House", 60, ["dog", "cat"])
#
#p1 = Park()
#p1.add(r1)
#p1.add(r2)
#p1.add(r3)
#p1.add(r4)
#p1.list_all()



from flask import Flask, jsonify, url_for
import json


with open("park_data.json", "r", encoding="utf-8") as f:
    dati = json.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1>Welcome to park API</h1> \n\
    some end points available:\n    \
    - {url_for('get_rides')}\n   \
    - {url_for('get_ride', id_ride='inserire_id_ride')}\n   \
    - {url_for('get_wait_crowd', id_ride='inserire_id_ride', crowd=0.5)}"

@app.route('/rides', methods=['GET'])
def get_rides():
    if dati["rides"]:
        return jsonify(dati["rides"]), 200
    return {"Errore": "Dati mancanti"}, 404

@app.route('/rides/<id_ride>', methods=['GET'])
def get_ride(id_ride):
    if id_ride in dati["rides"]:
        return jsonify(dati["rides"][id_ride])
    return {"Errore": "Dati mancanti"}, 404
    
@app.route('/rides/<id_ride>/wait/<float:crowd>', methods=['GET'])
def get_wait_crowd(id_ride, crowd):
    if id_ride in dati["rides"]:
        return {"Attesa" : 60 * crowd}
    return {"Errore": "Dati mancanti"}, 404
