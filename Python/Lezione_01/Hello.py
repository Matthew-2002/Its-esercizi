print ("Hello World!")
print ("hey there")

from datetime import date

assenze: float = 187
erogate: float = 605
presenze: float = erogate - assenze

#dati aggiornati al 31 luglio

obiettivo: float = 0.2

giorni: int = 0

print(f'{(assenze*100/erogate):.2f}%')

while (assenze/erogate) > obiettivo:
    erogate += 5
    giorni += 1

print(giorni)

    



