def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    aggregazione: dict[str:list[int]] = {}
    for dict_voti in voti:
        nome: str = dict_voti["nome"]
        voto: int = dict_voti["voto"]
        if nome not in aggregazione:
            aggregazione[nome] = [voto]
        else:
            aggregazione[nome].append(voto)
    return aggregazione
                
