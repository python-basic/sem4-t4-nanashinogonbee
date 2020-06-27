import random

random_array = [random.randint(0, 100) for _ in range(random.randint(10, 30))]
print('initial array: {}'.format(random_array))

even_array = [el for el in random_array if not el % 2]
odd_array = [el for el in random_array if el % 2]

print('even array: {}'.format(even_array))
print('odd array: {}'.format(odd_array))

