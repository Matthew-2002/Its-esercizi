def remove_duplicates(lista) -> list[any]:
    new_lista: list[any] = []
    for item in lista:
        if item not in new_lista:
            new_lista.append(item)
    return new_lista

print(remove_duplicates([1,6,3,7,9,7,4,2,1,6]))
