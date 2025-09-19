def calculate_average(numbers: list[int]) -> float:
    somma: int = 0
    if len(numbers) == 0:
        return 0
    else:
        for item in numbers:
            somma += item
    return somma / len(numbers)