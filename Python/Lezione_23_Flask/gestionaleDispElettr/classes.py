from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, id, model, customer_name, purchase_year, status="received"):
        self.id = id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.status = status

    @abstractmethod
    def device_type(self):
        pass

    @abstractmethod
    def base_diagnosis_time(self):
        pass

    @abstractmethod
    def repair_complexity(self):
        pass

    def info(self) -> dict[str, str|int]:
        return {
            "id": self.id,
            "device_type": self.device_type(),
            "model": self.model,
            "customer_name": self.customer_name,
            "purchase_year": self.purchase_year,
            "status": self.status
        }

    def estimated_total_time(self, factor: float = 1.0):
        base = self.base_diagnosis_time()
        complexity = self.repair_complexity()
        total = base * factor + complexity * 30
        return int(total)


class Smartphone(Device):
    def __init__(self, id, model, customer_name, purchase_year,
                 has_protective_case, storage_gb, status="received"):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb

    def device_type(self):
        return "smartphone"

    def base_diagnosis_time(self):
        return 20 

    def repair_complexity(self):
        return 2

    def info(self):
        base_info = super().info()
        base_info.update({
            "has_protective_case": self.has_protective_case,
            "storage_gb": self.storage_gb
        })
        return base_info


class Laptop(Device):
    def __init__(self, id, model, customer_name, purchase_year,
                 has_dedicated_gpu, screen_size_inches, status="received"):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches

    def device_type(self):
        return "laptop"

    def base_diagnosis_time(self):
        return 40

    def repair_complexity(self):
        return 4 

    def info(self):
        base_info = super().info()
        base_info.update({
            "has_dedicated_gpu": self.has_dedicated_gpu,
            "screen_size_inches": self.screen_size_inches
        })
        return base_info


class ServiceCenter:
    def __init__(self):
        self.devices = {}

    def add(self, device):
        if device.id in self.devices:
            return False
        self.devices[device.id] = device
        return True

    def get(self, device_id):
        return self.devices.get(device_id, None)

    def update(self, device_id, new_device):
        if device_id in self.devices:
            self.devices[device_id] = new_device
            return True
        return False

    def patch_status(self, device_id, new_status):
        device = self.get(device_id)
        if device:
            device.status = new_status
            return True
        return False

    def delete(self, device_id):
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False

    def list_all(self):
        return [dev.info() for dev in self.devices.values()]


if __name__ == "__main__":
    center = ServiceCenter()

    s1 = Smartphone(
        id="d1",
        model="iPhone 13",
        customer_name="Mario Rossi",
        purchase_year=2021,
        has_protective_case=True,
        storage_gb=128
    )

    l1 = Laptop(
        id="d2",
        model="ThinkPad X1",
        customer_name="Luigi Bianchi",
        purchase_year=2020,
        has_dedicated_gpu=False,
        screen_size_inches=14.0
    )

    center.add(s1)
    center.add(l1)

    for d in center.list_all():
        print(d)

    center.patch_status("d1", "diagnosing")

    print("\nDopo update stato d1:")
    print(center.get("d1").info())

    print("\nTempo stimato per d1:", center.get("d1").estimated_total_time())
    print("Tempo stimato per d2:", center.get("d2").estimated_total_time())


#funzioni ausiliarie
def leggi(nome_file_json = 'data.json'):
    try:
        with open(nome_file_json, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file_json}' non è stato trovato")
        return {} 
    
def scrivi(dati_da_salvare: dict, nome_file_json = 'data.json'):
    try:
        with open(nome_file_json, 'w', encoding='utf-8') as file:
            json.dump(dati_da_salvare, file, indent=4)
        print(f"File '{nome_file_json}' salvato con successo.")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")


from flask import Flask, jsonify, url_for, request
import json

dati = {"devices" : {}}
for key, element in center.devices.items():
    dati["devices"][key] = element.info()
scrivi(dati)


#inizio app Flask
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify()

@app.route("/devices", methods=["GET"])
def getDevices():
    return jsonify(leggi()["devices"]) \
        if (jsonify(leggi()["devices"])) \
            else jsonify({"errore" : "elenco dispositivi vuoto"}), 404

@app.route("/devices/<device_id>", methods=["GET"])
def getDevice(device_id):
    return jsonify(leggi()["devices"][device_id]) \
        if (jsonify(leggi()["devices"][device_id])) \
            else jsonify({"errore" : "dispositivo non trovato"}), 404

@app.route("/devices/<device_id>/estimate/<float:factor>", methods=["GET"])
def getDeviceEstimatedTime(device_id, factor):
    try:        
        device = center.get(device_id)
        if not device: 
            raise KeyError
        
        result = {
            "id": device_id,
            "device_type": device.device_type(),
            "factor": factor,
            "estimated_total_minutes": device.estimated_total_time(factor)
        }
        return jsonify(result)
        
    except KeyError:
        return jsonify({"errore": "dispositivo non trovato"}), 404
    

@app.route("/devices", methods=["POST"])
def addDevice():
    payload = request.get_json()
    if not payload:
        return jsonify({"errore": "payload non trovato"}), 404
    try:   
        if payload["device_type"] == "smatphone":
            device = Smartphone(payload["id"], payload["model"], payload["customer_name"], payload["purchase_year"],
                                payload["has_protective_case"], payload["storage_gb"])
        elif payload["device_type"] == "laptop":
            device =  Laptop(payload["id"], payload["model"], payload["customer_name"], payload["purchase_year"],
                             payload["has_dedicated_gpu"], payload["screen_size_inches"])
        else:
            return jsonify({"errore": f'tipo \"{payload["device_type"]}\" non valido'}), 404
        center.add(device)
    except KeyError as e:
        return jsonify({"errore" : f"chiave {str(e)} mancante"}), 404
    
    

    
    

    




