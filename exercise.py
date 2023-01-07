# Exercise I
# converted = [[1, 2, 3, 4,5], [6, 7, 8], [9, 10, 11]]
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='')
        if pixel == 0:
            print(' ', end='')
    print('')

# Exercises II
some_list = ['a', 'b', 'c', 'd', 'd', 'm', 'n', 'n', 'a']

# First Solution
sort_list = sorted(some_list)
for i in set(sort_list):
    sort_list.remove(i)
print(sort_list)

# Second Solution short-circuit
duplicate_list = []
for values in sort_list:
    if sort_list.count(values) > 1 and values not in duplicate_list:
        duplicate_list.append(values)
print(duplicate_list)

# Third Solution
duplicates = []
for values in sort_list:
    if sort_list.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)

# Exercises III

li = [1, 2, 3, 4, 5, 6, 7, 1, 3, 5]
for x in set(li):
    li.remove(x)
li = list(set(li))
print(li)

# Exercise IIII


def highest_even(li):
    highest_even_number = 0
    for x in li:
        if x % 2 == 0:
            # print(f"{x} is Even number")
            if x > highest_even_number:
                highest_even_number = x
    return highest_even_number


print(highest_even([1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

# Second Solution


def highest_evens(li):
    even = []
    for number in li:
        if number % 2 == 0:
            even.append(number)
    return max(even)


print(highest_evens([2, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# Example III


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        x = 3
        if age >= 4:
            self.name = name
            self.age = age

    def oldest_func(self):
        print(f"Then oldest cat is {self.age} old")
        return


cat1 = Cat('love', 3)
cat2 = Cat('nice', 2)
cat1 = Cat('great', 4)
cat1.oldest_func()

# Solution


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Peanut', 3)
cat2 = Cat('Garfield', 2)
cat3 = Cat('snicker', 1)

# Find the oldest cat


def get_oldest_cat(*args):
    return max(args)


print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)}")
