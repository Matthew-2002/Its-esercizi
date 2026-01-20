from abc import ABC, abstractmethod

# --- Classe Astratta Vehicle ---
class Vehicle(ABC):
    def __init__(self, plate_id: str, model: str, registration_year: int, status: str = "available", driver_name: str = None):
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
        prep_time = self.base_cleaning_time() * factor + self.wear_level() * 15
        return int(prep_time)


# --- Sottoclasse Car ---
class Car(Vehicle):
    def __init__(self, plate_id, model, registration_year, doors: int, is_cabrio: bool, status="available", driver_name=None):
        super().__init__(plate_id, model, registration_year, status, driver_name)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self) -> str:
        return "car"

    def base_cleaning_time(self) -> int:
        return 30

    def wear_level(self) -> int:
        return 2  # Usura bassa per automobili standard

    def info(self) -> dict:
        data = super().info()
        data.update({
            "doors": self.doors,
            "is_cabrio": self.is_cabrio
        })
        return data


# --- Sottoclasse Van ---
class Van(Vehicle):
    def __init__(self, plate_id, model, registration_year, max_load_kg: int, require_special_license: bool, status="available", driver_name=None):
        super().__init__(plate_id, model, registration_year, status, driver_name)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self) -> str:
        return "van"

    def base_cleaning_time(self) -> int:
        return 60

    def wear_level(self) -> int:
        return 5  # Usura alta per veicoli da lavoro

    def info(self) -> dict:
        data = super().info()
        data.update({
            "max_load_kg": self.max_load_kg,
            "require_special_license": self.require_special_license
        })
        return data


# --- Gestore della Flotta FleetManager ---
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


# --- Main / Esempio di Utilizzo ---
if __name__ == "__main__":
    fleet_manager = FleetManager()

    # Creazione dei veicoli
    panda = Car("HA014AS", "Fiat Panda", 2022, doors=5, is_cabrio=False)
    transit = Van("CC216FG", "Ford Transit", 2020, max_load_kg=1200, require_special_license=False)

    # Aggiunta alla flotta
    fleet_manager.add(panda)
    fleet_manager.add(transit)

    # Test calcolo tempo preparazione
    print(f"Tempo preparazione Panda: {panda.estimated_prep_time()} min")
    print(f"Tempo preparazione Transit: {transit.estimated_prep_time()} min")

    # Modifica stato tramite Patch
    fleet_manager.patch_status("HA014AS", "rented")

    # Visualizzazione flotta
    print("\n--- Elenco Veicoli nella Flotta ---")
    for v_info in fleet_manager.list_all():
        print(v_info)


# ==========================
# Applicazione Flask
# ==========================

from flask import Flask, jsonify, request, url_for


app = Flask(__name__)


def create_vehicle_from_data(data: dict, plate_id: str) -> Vehicle:

    if not plate_id:
        plate_id = data.get("plate_id")

    type: str = data.get("plate_id").vehicle_type()

    if type not in ("van", "car"):
        return jsonify({"error" : "tipo veicolo errato"}), 400
    
    match type:
        case "van":
            model = data.get("model")
            registration_year = data.get("moregistration_yeardel")
            max_load_kg = data.get("max_load_kg")
            require_special_license = data.get("require_special_license")
            if data.get("status"):
                status = data.get("status")
            else:
                status = "available"
            if data.get("driver_name"):
                driver_name = data.get("driver_name")
            else:
                driver_name = None

            if not all(model, registration_year, max_load_kg, require_special_license):
                raise ValueError("attributi mancanti")
            return Van(
                plate_id = plate_id, 
                model = model, 
                registration_year = registration_year, 
                max_load_kg = max_load_kg, 
                require_special_license = bool(require_special_license), status="available", driver_name=None
            )

        case "car":


    