from functools import reduce

# map, filter, zip, and reduce


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list
# print(multiply_by2([1, 2, 3]))


my_list = [1, 2, 3]


def multiply_withMap(item):
    return item * 2
# print(list(map(multiply_withMap, my_list)))

# Filter


def only_Odd(item):
    return item % 2 != 0
# print(list(filter(only_Odd, my_list)))


# Zip
your_list = [10, 20, 30, 40, 50]
# print(list(zip(my_list, your_list)))

# reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# print(reduce(accumulator, my_list, 0))

# Examples
# Capitalization all of pet names and print the list
my_pets = ['sis', 'bibi', 'titi', 'carla']


def sort_name(li):
    for i in range(len(li)):
        li[i] = li[i].upper()
    return li


print(sort_name(my_pets))

# Zip the 2 list into a list of tuples, but sort the number form lower to higher
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

# Filter the scores  that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def filter_scores(num):
    return num > 50


print(list(filter(filter_scores, scores)))

# Combine all of the number that are in a list on this file using reduce (my_number and scores). what is the total


def accumulate_total(acc, item):
    return acc + item


print(reduce(accumulate_total, my_numbers, sum(scores)))  # 456
print(reduce(accumulate_total, scores + my_numbers, 0))  # 456

my_num = [1, 2, 4, 6, 7]
print(list(map(lambda item: item * 2, my_num)))
print(list(filter(lambda item: item % 2 != 0, my_num)))
print(reduce(lambda acc, item: acc + item, my_num))
