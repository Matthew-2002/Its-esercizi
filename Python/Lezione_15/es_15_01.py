'''Esercizio 1

Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')'''


'''class FileManager:
    
    def __enter__(self):

        open(self.fileName, self.openingMode, self.encoding)
        return 
    
    def __init__(self, name: str, mode: str = "r", encoding: str = "utf-8"):

        self.fileName = name
        self.openingMode = mode
        self.encoding = encoding 


    def __exit__(self):

'''
import json

# es_jason = open("Lezione_15/es2_jason.json", "w")

# json_data: dict = {
#     "a1": {
#         "b1": "c1",
#         "b2": "c2"
#     },
#     "a2": {
#         "b3": "c3",
#         "b4": "c4"
#     }
# }

# json.dump(json_data, es_jason)

# es_jason.close()



