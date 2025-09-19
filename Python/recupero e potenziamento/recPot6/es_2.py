def validateName(nome: str) -> bool:

    if nome != '' and len(nome) < 20:
        return True
    return False


inseriti: list[str] = []
nome: str = input("Inserisci un nome: ").replace(" ", "")
valido: bool = validateName(nome)

while nome not in inseriti and len(inseriti) <= 30:

    if valido == False:
        nome: str = input("Nome non valido, inserisci un nome: ").replace(" ", "")
        valido: bool = validateName(nome)
        continue
    else:
        if len(inseriti) == 0:
            nomepiulungo: str = nome[:]
            lungmax: int = len(nome)
        else:
            if len(nome) > lungmax:
                nomepiulungo: str = nome[:]
                lungmax: int = len(nome)
        inseriti.append(nome)
        nome: str = input("Inserisci un nome: ").replace(" ", "")
        valido: bool = validateName(nome) 

print(f'Hai inserito {len(inseriti)} nomi distinti\n\
Il più lungo è {nomepiulungo} con {lungmax} caratteri')  
        
    
        
