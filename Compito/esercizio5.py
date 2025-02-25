'''Esercizio 5
Si supponga di poter acquistare barrette di cioccolato da un distributore automatico 
al costo di 1 euro ciascuna. Ogni barretta acquistata contiene un buono sconto, e con 
6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, 
considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.'''


euro_tot = int(input("Inserisci totale spesa:\n"))
barrete_extra = euro_tot // 6
buoni_avanzati = euro_tot % 6
barrette_totali = euro_tot + barrete_extra

print(f"Puoi acquistare un totale di {barrette_totali} barrette e ti avanzeranno un totale di {buoni_avanzati} buono/i")
   