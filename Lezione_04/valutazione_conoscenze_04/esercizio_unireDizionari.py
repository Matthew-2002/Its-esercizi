def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    new_dict: dict[any, any] = {}
    for key, value in dict1.items():
        for key2, value2 in dict2.items():
            if key == key2:
                new_dict[key] = value + value2
            else:
                new_dict[key] = dict1[key]
    for key, value in dict2.items():
        for key2, value2 in new_dict.items():
            if key != key2:
                new_dict[key] = dict2[key]

    return new_dict


print(merge_dictionaries({'x': 5}, {'x': -5}))