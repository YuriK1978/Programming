# Есть массив, нужно оставить только уникальные элементы > 5.

'''
# Вариант 1
def get_unique(numbers):
    unique_numbers= {}
    for key in numbers:
        unique_numbers[key] = unique_numbers.get(key, 0) + 1
    return list(filter(lambda x: ((unique_numbers[x] < 2) and (x > 5)), unique_numbers))

print(get_unique([1, 77, 77, 89, 90, 100]))'''

# Вариант 2

if __name__ == '__main__':
    array = [1, 2, 2, 3, 3, 4, 5, 10, 10 ,8]
    result = [
        num for index, num in enumerate(array)
        if num > 5 and num not in array[index+1:]
        and num not in array[:index]
    ]
    print(result)