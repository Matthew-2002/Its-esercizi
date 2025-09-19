def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    lista_pari: list[int] = []
    for item in lista_numeri:
        if item % 2 == 0:
            lista_pari.append(item*fattore)
    return lista_pari

print(filtra_moltiplica([1,2,3,4,5,6,7], 10))
