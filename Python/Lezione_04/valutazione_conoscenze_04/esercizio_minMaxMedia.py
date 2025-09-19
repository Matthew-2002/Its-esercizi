def list_statistics(numbers: list[int]) -> any:
    min: int = 0
    max: int = 0
    somma: int = 0
    for item in numbers:
        if item == numbers[0]:
            min = item
            max = item
            somma += item
        else:
            if item < min:
                min = item
            elif item > max:
                max = item
            somma += item
    media: float = somma/len(numbers)
    return max, min, media

print(list_statistics([1,2,3,4,5,6,7,8]))