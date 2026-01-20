#print ("Hello World!")
#print ("hey there")

from datetime import datetime, timedelta

assenze: float = 192
erogate: float = 874.5
presenze: float = erogate - assenze

#dati aggiornati al 20 gennaio

max_assenze: float = 0.2
giorni: int = 0
giorni_lez_mancanti = int (1080 - erogate) // 5
giorni_tot_mancanti_we = giorni_lez_mancanti+giorni_lez_mancanti*2/7

print(f'Percentuale asssenza attuale {(assenze*100/erogate):.2f}%')

while (assenze/erogate) > max_assenze:
    erogate += 5
    giorni += 1

giorni_per_obiettivo = giorni*2/7 + giorni
data_obiettivo = datetime.today() + timedelta(giorni_per_obiettivo)
data_fine_corso = datetime.today() + timedelta(giorni_tot_mancanti_we)

print(f'Previsione raggiungimento obiettivo: ~ {data_obiettivo.strftime("%d-%m-%Y")}\n\
Giorni di lezione effettivi all\'obiettivo: ~ {giorni}\
\nGiorni di lezione effettivi al\'termine lezioni: ~ {giorni_lez_mancanti}\
\nPrevisione termine corso: ~ {data_fine_corso.strftime("%d-%m-%Y")}\
\nGiorni al termine delle lezione con we: ~ {giorni_tot_mancanti_we:.0f}\n\
Giorni al termine dell\'obiettivo con we: ~ {giorni_per_obiettivo:.0f}'
)


