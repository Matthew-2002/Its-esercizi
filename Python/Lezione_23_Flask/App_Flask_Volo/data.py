dati: dict = {
    "Nazioni": {
        "1": {
            "id": 1, 
            "nome": "Italia"
        },
        "2": {
            "id": 2, 
            "nome": "Germania"
        },
        "3": {
            "id": 3, 
            "nome": "Francia"
        },
        "4": {
            "id": 4, 
            "nome": "Spagna"
        }
    },
    "Città": {
        "1": {
            "id": 1, 
            "nome": "Roma", 
            "n_abitanti": 2873000, 
            "nazione": 1
        },
        "2": {
            "id": 2, 
            "nome": "Berlino", 
            "n_abitanti": 3645000, 
            "nazione": 2
        },
        "3": {
            "id": 3, 
            "nome": "Parigi", 
            "n_abitanti": 2148000, 
            "nazione": 3
        },
        "4": {
            "id": 4, 
            "nome": "Madrid", 
            "n_abitanti": 3266000, 
            "nazione": 4
        }
    },
    "Compagnie": {
        "Alitalia": {
            "nome": "Alitalia", 
            "fondazione": 2000, 
            "città": 1
        },
        "Lufthansa": {
            "nome": "Lufthansa", 
            "fondazione": 2000, 
            "città": 2
        },
        "AirFrance": {
            "nome": "AirFrance", 
            "fondazione": 2000, 
            "città": 3
        },
        "Iberia": {
            "nome": "Iberia", 
            "fondazione": 2000, 
            "città": 4
        }
    },
    "Aeroporti": {
        "FCO": {
            "codice": "FCO", 
            "nome": "Aeroporto di Roma Fiumicino", 
            "città": 1
        },
        "TXL": {
            "codice": "TXL", 
            "nome": "Aeroporto di Berlino Tegel", 
            "città": 2
        },
        "CDG": {
            "codice": "CDG", 
            "nome": "Aeroporto Charles de Gaulle", 
            "città": 3
        },
        "MAD": {
            "codice": "MAD", 
            "nome": "Aeroporto di Madrid-Barajas", 
            "città": 4
        }
    },
    "Voli": {
        "AZ100": {
            "codice": "AZ100", 
            "durata_in_minuti": 120, 
            "partenza": "FCO", 
            "arrivo": "CDG", 
            "compagnia": "Alitalia", 
            "città": 1
        },
        "LH200": {
            "codice": "LH200", 
            "durata_in_minuti": 100, 
            "partenza": "TXL", 
            "arrivo": "FCO", 
            "compagnia": "Lufthansa", 
            "città": 2
        },
        "AF300": {
            "codice": "AF300", 
            "durata_in_minuti": 90, 
            "partenza": "CDG", 
            "arrivo": "MAD", 
            "compagnia": "AirFrance", 
            "città": 3
        },
        "IB400": {
            "codice": "IB400", 
            "durata_in_minuti": 110, 
            "partenza": "MAD", 
            "arrivo": "TXL", 
            "compagnia": "Iberia", 
            "città": 4
        }
    }
}