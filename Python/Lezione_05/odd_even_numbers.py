def even_odd_pattern(numbers:list[int]) -> list[int]:
    dispari: list[int] = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            dispari.append(numbers[i])
    for i in dispari:
        if i in numbers:
            numbers.remove(i)
    numbers += dispari
    return numbers