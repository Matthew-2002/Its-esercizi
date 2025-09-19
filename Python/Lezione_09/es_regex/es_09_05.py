'''5. Riconoscere date

Obiettivo: Lavorare con formati numerici separati da caratteri speciali.

    Esercizio 5.1: Scrivi una RegEx che riconosca una data nel formato gg/mm/aaaa (es. 09/04/2025).
    Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.
'''

import re

print(re.search(r"^\d{2}(?:/|-)\d{2}(?:/|-)\d{4}$", "21-30/2003"))