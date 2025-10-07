def dedup_stable(nums: list[int]) -> list[int]:
    new_nums = []
    for num in nums:
        lunghezza = len(str(num))
        new_num = num//(10**(lunghezza-1))
        if new_nums: 
            if new_num != new_nums[-1]:
                new_nums.append(new_num)
        else:
            new_nums.append(new_num)
    return new_nums


def chunk(lst: list[int], size: int) -> list[list[int]]:
    new_list = []
    if not lst:
        return new_list
    i = len(lst)//size
    index = 0
    while index < len(lst):
        if i == 0:
            size = len(lst)%size 
        for j in range(size):
            if j == 0:
                temp_list = [lst[index]]
            else:
                temp_list.append(lst[index])
            index += 1
        new_list.append(temp_list)
        i -= 1
    return new_list

            
def flatten_once(nested: list[list[int]]) -> list[int]:
    new_list = []
    for list in nested:
        for num in list:
            new_list.append(num)
    return new_list


def letter_count(text: str) -> dict[str,int]:
    occorrenze = {}
    for l in text:
        if l.isalpha():
                l = l.lower()
                if l in occorrenze:
                    occorrenze[l] += 1
                else:
                    occorrenze[l] = 1
    return occorrenze


def deep_get(d, path: list, default=None):
    try:
        for item in path:
            d = d[item]
        return d
    except:
        return default
    
    
print(deep_get({'a': {'b': [10, 20]}}, ['a', 'b', 2], 'default'))



def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:

    new_list: list[int] = []
    a += b
    for num in a:
        if a.count(num) == 1:
            new_list.append(num)

    return sorted(new_list)

def are_anagrams(a: str, b: str) -> bool:
    new_a = ''
    new_b = ''
    for item in a:
        if item.isalpha():
            new_a += item.lower()
    for item in b:
        if item.isalpha():
            new_b += item.lower()
    if len(new_a) != len(new_b):
        return False
    for item in new_a:
        if new_a.count(item) != new_b.count(item):
            return False
    return True

        
def powerset_size(n: int) -> int:

    return 2**n

def apply_twice(fn, x):
    
    
            
        
        