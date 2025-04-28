def classifica_numeri(lista: list[int]) -> dict[str:list[int]]:
    classifica: dict = {"pari":[],"dispari":[]}
    for item in lista:
        if item % 2 == 0:
            classifica["pari"].append(item)
        else:
            classifica["dispari"].append(item)
    return classifica