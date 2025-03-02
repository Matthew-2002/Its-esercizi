'''Esercizio 3C-5. Scrivere un programma in Python che 
memorizzi il nome, il ruolo e l'età di un utente in un 
dizionario. Il nome, il ruolo e l'età devono essere 
inseriti in input dall'utente stesso. Il programma deve 
determinare il livello di accesso ai servizi in base al 
ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare 
le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i 
servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune 
funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei 
contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! 
Accesso Negato!"

Expected Output:

Digitare nome dell'utente: Mario Rossi
Digitare ruolo dell'utente: admin
Digitare l'età dell'utente: 30
Output: Accesso completo a tutte le funzionalità.'''


informazioni:dict[str] = {"nome": "0", "ruolo": "0", "età": "0",}
nome_:str = input("Digitare il tuo nome: ")
ruolo_:str = input("Digitare il tuo ruolo: ")
età_:str =  int(input("digitare la tua età: "))

if età_ < 18:
    età_ = "min"
else:
    età_ = "magg"

informazioni["nome"] = nome_
informazioni["ruolo"] = ruolo_
informazioni["età"] = età_

match informazioni:
    case {"nome": name_, "ruolo": "admin", "età": età_}:
        print("Accesso completo a tutte le funzionalità")
    case {"nome": name_, "ruolo": "moderatore", "età": età_}:
        print("Può gestire contenuti, ma non modifivare le impostazioni")
    case {"nome": name_, "ruolo": "utente", "età": "min"}:
        print("Accesso limitato! alcune funzionalità sono bloccate")
    case {"nome": name_, "ruolo": "utente", "età": "magg"}:
        print("Accesso standard a tutti i servizi")
    case {"nome": name_, "ruolo": "ospite", "età": età_}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")













