import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


random_array = [random.randint(0, 100) for _ in range(random.randint(10, 30))]
print('initial array: {}'.format(random_array))
insertion_sort(random_array)
print('sorted array: {}'.format(random_array))

