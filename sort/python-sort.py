import random

def python_sort(array):
    return sorted(array)

random_data = [random.randint(0, 100_000) for i in range(100_000)]
sorted_data = python_sort(random_data)

print(sorted_data)