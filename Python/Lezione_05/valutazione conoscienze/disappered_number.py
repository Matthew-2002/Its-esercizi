def find_disappeared_numbers(nums: list[int]) -> list[int]:
    new_list: list[int] = []
    for i in range(1, len(nums)+1):
        if i not in nums:
            new_list.append(i)
    return new_list


print(find_disappeared_numbers([1,8,9,150,9,2189,2,82,3,3,3]))