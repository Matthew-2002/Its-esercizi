def count_isolated(lista) -> int:
    count = 0
    for i in range(len(lista)):
        if i == 0:
            if lista[i] != lista[i+1]:
                count += 1
        elif i == len(lista) - 1:
            if lista[i] != lista[i -1]:
                count += 1
        else:
            if lista[i] != lista[i+1] and \
                lista[i] != lista[i-1]:
                count += 1
    return count