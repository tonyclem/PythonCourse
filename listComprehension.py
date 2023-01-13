# List, set, dictionary

my_list = [char for char in 'hello world']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(my_list3)

simple_dict = {
    "a": 1,
    "b": 2,
}

my_dict = {
    k: v**2 for k, v in simple_dict.items() if v % 2 == 0
}
# print(my_dict)

my_num = {num: num*2 for num in [1, 2, 3]}
# print(my_num)

some_list = ['a', 'b', 'c', 'd', 'm', 'b', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
