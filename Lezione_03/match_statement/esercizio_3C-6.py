'''Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, 
affinchè si possa scrivere un codice python che consenta 
all'utente di inserire il nome di un animale ed un habitat. 
Quando il codice dell'esercizo 3C-4 classifica l'animale 
inserito in una delle categorie tra mammiferi, rettili, 
uccelli o pesci, oltre a mostrare un messaggio a schermo, 
deve salvare tale categoria in una variabile animal_type. 
Se l'animale inserito non è classificabile in una delle 
quattro categorie proposte, il valore di animal_type sarà ' 
"unknown".

Inserire, poi, in un dizionario il nome dell'animale, la 
categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria 
a cui esso appartiene possano vivere nell'habitat inserito; 
dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare 
un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, 
stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare 
un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, 
delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, 
gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra'''



mammiferi:list[str] = [
                        "cane", 
                        "gatto", 
                        "cavallo", 
                        "elefante", 
                        "leone", 
                        "balena", 
                        "delfino"
                                    ]
rettili:list[str] = [
                        "serpente", 
                        "lucertola", 
                        "tartaruga", 
                        "coccodrillo"
                                        ]
uccelli:list[str] = [
                        "aquila", 
                        "pappagallo", 
                        "gufo", 
                        "falco", 
                        "cigno", 
                        "anatra", 
                        "gallina", 
                        "tacchino"
                                        ]
pesci:list[str] = [
                        "squalo", 
                        "trota", 
                        "salmone", 
                        "carpa"
                                    ]

animale:str = input("inserisci un animale da classificare: ")
habitat:str = input("inserire l'habitat: ")

match animale:
    
    case animale if animale in mammiferi:
        scheda_animale:dict[str] = {
                                    "animale": animale, 
                                    "habitat": habitat
                                    }
        match scheda_animale:
            case {"animale": "balena" | "delfino", 
                  "habitat": "acqua"}:
                print(f"l'animale {animale} può vivere nell'habitat {habitat}")
            case {"habitat": "terra"}:
                print(f"l'animale {animale} può vivere nell'habitat {habitat}")
            case _:
                print(f"L'animale {animale} non può vivere nell'habitat {habitat}")
    
    case animale if animale in rettili:
        scheda_animale:dict[str] = {
                                    "animale": animale, 
                                    "habitat": habitat
                                    }
        match scheda_animale:
            case {"habitat": "terra" | "acqua"}:
                print(f"l'animale {animale} può vivere nell'habitat {habitat}")
            case {"habitat": "acqua"}:
                print(f"l'animale {animale} può vivere nell'habitat {habitat}")
            case _:
                print(f"l'animale {animale} non può vivere nell'habitat {habitat}")
    
    case animale if animale in uccelli:
        animal_type:str = "Uccelli"
        scheda_animale:dict[str] = {
                                    "animale": animale,                                  
                                    "habitat": habitat
                                    }
        match scheda_animale:
            case {"animale": "cigno" | "anatra", 
                  "habitat": "acqua"}:
                print(f"l'animale {animale} può vivere nell'habitat {habitat}")
            case {"habitat": "aria"}:
                print(f"l'animale {animale} può vivere nell'habitat {habitat}")
            case _:
                print(f"l'animale {animale} non può vivere nell'habitat {habitat}")     
    case animale if animale in pesci:
        animal_type:str = "Pesci"
        scheda_animale:dict[str] = {
                                    "animale": animale,                                   
                                    "habitat": habitat
                                    }
        match scheda_animale:
            case {"habitat": "acqua"}:
                print(f"l'animale {animale} può vivere nell'habitat {habitat}")
            case _:
                print(f"l'animale {animale} non può vivere nell'habitat {habitat}")
    case _:

        print(f"l'animale o habitat non riconosciuto")
        







