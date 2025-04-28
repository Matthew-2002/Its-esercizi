def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for key,value in da_rimuovere.items():
        if key in lista:
            for i in range(value):
                lista.remove(key)
    return lista