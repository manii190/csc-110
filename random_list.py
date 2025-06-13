import random

def random_list(numbers):
    random.seed(123)
    index = 0
    while index < len(numbers):
        numbers[index] = random.randint(0, numbers[index])
        index+=1
    return numbers #steven

numbers = [3, 2, 1, 3, 5]
numbers = random_list(numbers)
print(numbers)