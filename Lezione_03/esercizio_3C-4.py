'''Esercizio 3C-4. Scrivere un programma in Python che 
permetta all'utente di inserire il nome di un animale e, 
utilizzando un match statement, identifichi a quale 
categoria esso appartiene. L'animale deve essere 
classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie 
sopra elencate,  mostrare un messaggio indicante che il 
programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro 
categorie.

Expected Output:

Digita il nome di un animale: cane
Output: cane appartiene alla categoria dei Mammiferi!'''


Mammiferi:list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]
Rettili:list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli:list[str] = ["aquila", "pappagallo", "gufo", "falco"]
Pesci:list[str] = ["squalo", "trota", "salmone", "carpa"]

animale:str = input("inserisci un animale da classificare: ")

match animale:
    case animale if animale in Mammiferi:
        print(f"{animale} appartiene alla categoria dei mammiferi")
    case animale if animale in Rettili:
        print(f"{animale} appartiene alla categoria dei rettili")
    case animale if animale in Uccelli:
        print(f"{animale} appartiene alla categoria dei uccelli")
    case animale if animale in Pesci:
        print(f"{animale} appartiene alla categoria dei pesci")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")         











