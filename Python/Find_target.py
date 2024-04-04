# Найти два элемента по таргету БЕЗ ИНДЕКСОВ.

def find_target(seq: list, target: int) -> tuple[int]:
    my_set = set()
    for el in seq:
        temp = target - el
        if temp in my_set:
            return temp, el
        my_set.add(el)
        
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(find_target(nums, 15))
