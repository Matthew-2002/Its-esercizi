def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    new_list: list[int] = []
    for i in range(len(x)):
        new_list.append(x[i] + y[i])