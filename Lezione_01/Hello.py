print ("Hello World!")
print ("hey there")

from datetime import date

assenze: float = 187
erogate: float = 592.5
presenze: float = erogate - assenze

#dati aggiornati al 25 luglio

obiettivo: float = 0.2

giorni: int = 0

for _ in range(3):    
    erogate += 2.5
    giorni += 1

while (assenze/erogate) > obiettivo:
    erogate += 5
    giorni += 1

print(giorni)
    



