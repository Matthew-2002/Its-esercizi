def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    scontati: dict[str:float] = {}
    for key, value in prodotti.items():
        if value > 20:
            scontati[key] = value - (value/10)
    return scontati