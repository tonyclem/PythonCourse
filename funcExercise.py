from functools import reduce

my_pets = ['sis', 'bibi', 'titi', 'carla']


def capitalize(li):
    return li.upper()


print(list(map(capitalize, my_pets)))

# Zip the 2 list into a list of tuples, but sort the number form lower to higher
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))
