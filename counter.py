from collections import Counter, defaultdict, OrderedDict

# Counter count how many times each appears in list
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
print(Counter(li))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['b'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)
