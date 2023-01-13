from functools import reduce

my_pets = ['sis', 'bibi', 'titi', 'carla']


def capitalize(li):
    return li.upper()


# print(list(map(capitalize, my_pets)))

# Zip the 2 list into a list of tuples, but sort the number form lower to higher
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

# print(list(zip(my_strings, sorted(my_numbers))))

# Square
my_square = [4, 5, 3]
# print(list(map(lambda item: item ** 2, my_square)))

# List Sorted
a = [(0, 2), (4, 3), (9, 9), (10, -1)]


def sort_list(tup):
    tup.sort(key=lambda x: x[1])
    return tup


print(sort_list(a))
