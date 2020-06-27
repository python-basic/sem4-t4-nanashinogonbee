def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


array = [7, 5, 6, 4, 3, 1, 2]
print('initial array: {}'.format(array))
insertion_sort(array)
print('sorted array: {}'.format(array))

