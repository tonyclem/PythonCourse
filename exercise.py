# Exercise I
# converted = [[1, 2, 3, 4,5], [6, 7, 8], [9, 10, 11]]
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
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