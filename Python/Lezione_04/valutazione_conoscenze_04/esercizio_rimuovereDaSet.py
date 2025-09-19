def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    for item in elements_to_remove:
        if item in original_set:
            original_set.remove(item)
    return original_set