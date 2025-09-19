def reverseList(
        lista: list[any], 
        ) -> None:

    if len(lista) == 1:
        return f"{lista[-1]}"
    print(f"{lista[-1]}")
    lista.pop
    new_list: list[any] = lista[:]
    return reverseList(new_list)


reverseList([1,2,3,4,5])
