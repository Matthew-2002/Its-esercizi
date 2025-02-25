'''Esercizio 10
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
Esempio di input e output
Input:

Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0
Output:

Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''


somma_pari:int = 0 
somma_dispari:int = 0
n_dis:int = 0
frequenza:dict[int, int] = {}
Max:int = 0
massimi:list[int] = []

# imposto ciclo e studio caso inserimento 0
while True:
    numero:int = int(input("Inserisci un numero (0 per terminare):\n"))
    
    if numero == 0:
        
        # stampo somma pari e media dispari anche nel caso di nessun elemento
        print (f"\nSomma dei numeri pari: {somma_pari}")
        if n_dis == 0:
            print (f"Media dei numeri dispari: 0")
        else: 
            print (f"Media dei numeri dispari: {somma_dispari/n_dis:.2f}")
        
        # controllo se ci sono elementi nel dizionario per la frequenza
        if len(frequenza) == 0:
            print("non hai aggiunto elementi\n")
        else:
            
            # salvo i numeri più ricorrenti in una lista
            for item in frequenza:
                if frequenza[item] > Max:
                    massimi:list = [item]
                    Max = frequenza[item]
                elif frequenza[item] == Max:
                    massimi.append(item)
            print(f"Numero/i più frequente/i: {massimi} ({Max} volta/e)\n")
        break
    
    # se l'utente inserisce numero, aggiorno somma pari, e somma dispari per la media
    else:
        if numero % 2 == 0:
            somma_pari += numero
        else:
            somma_dispari += numero
            n_dis += 1
   
    # inserisco numero da input nel dizionario
    if numero in frequenza:
        frequenza[numero] += 1
    else:
        frequenza[numero] = 1







