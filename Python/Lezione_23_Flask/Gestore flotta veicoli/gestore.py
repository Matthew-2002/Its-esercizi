from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, plate_id: str, model: str, registration_year: int, driver_name: str = None, status: str = "available"):
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self) -> str:
        pass

    @abstractmethod
    def base_cleaning_time(self) -> int:
        pass

    @abstractmethod
    def wear_level(self) -> int:
        pass

    def info(self) -> dict:
        return {
            "id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status
        }

    def estimated_prep_time(self, factor: float = 1.0) -> int:
        # Formula: base_cleaning_time() * factor + wear_level() * 15
        return int(self.base_cleaning_time() * factor + self.wear_level() * 15)


class Car(Vehicle):
    def __init__(self, plate_id, model, registration_year, doors: int, is_cabrio: bool, driver_name: str = None, status: str = "available"):
        super().__init__(plate_id, model, registration_year, driver_name, status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self):
        return "car"

    def base_cleaning_time(self):
        return 30

    def wear_level(self):
        return 2  # Usura bassa per auto

    def info(self):
        data = super().info()
        data.update({
            "doors": self.doors,
            "is_cabrio": self.is_cabrio
        })
        return data


class Van(Vehicle):
    def __init__(self, plate_id, model, registration_year, max_load_kg: int, require_special_license: bool, driver_name: str = None, status: str = "available"):
        super().__init__(plate_id, model, registration_year, driver_name, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self):
        return "van"

    def base_cleaning_time(self):
        return 60  # Più oneroso da pulire

    def wear_level(self):
        return 4  # Usura alta per uso lavorativo

    def info(self):
        data = super().info()
        data.update({
            "max_load_kg": self.max_load_kg,
            "require_special_license": self.require_special_license
        })
        return data


class FleetManager:
    def __init__(self):
        self.vehicles = {}

    def add(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id in self.vehicles:
            return False
        self.vehicles[vehicle.plate_id] = vehicle
        return True

    def get(self, plate_id: str) -> Vehicle:
        return self.vehicles.get(plate_id)

    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        if plate_id in self.vehicles:
            self.vehicles[plate_id] = new_vehicle

    def patch_status(self, plate_id: str, new_status: str) -> None:
        vehicle = self.get(plate_id)
        if vehicle:
            vehicle.status = new_status

    def delete(self, plate_id: str) -> bool:
        if plate_id in self.vehicles:
            del self.vehicles[plate_id]
            return True
        return False

    def list_all(self) -> list:
        return [v.info() for v in self.vehicles.values()]
    
    def getVehicles(self) -> dict:
        return self.vehicles


from flask import Flask, jsonify, url_for
import json

app = Flask(__name__)

fm: FleetManager = FleetManager()

@app.route('/veichles', methods=['GET'])
def getVeichles():
    return jsonify(fm.getVehicles()), 200

@app.route('/vehicles/<vehicle_plate>', methods=['GET'])
def getVehicle(vehicle_plate):
    if fm.get(vehicle_plate):
        return jsonify(fm.get(vehicle_plate)), 200
    else:
        return jsonify({"Errore": "veicolo non trovato"}), 400

    