# Iterate through
user = {
    "name": "Golem",
    "age": 100,
    "can_swim": False
}

for item in user:
    print(item)
for item in user.keys():
    print(item)
for item in user.items():
    print(item)

# Exercise 

# Counter
my_list = [1,2,3,4,5,6,7,8,9,10]
total = 0
for item in my_list:
    total += item
    # print(total)
print(total)

# Range
for number in range(0, 10):
    print(number)
for _ in range(10, 0, -1): #reverse order
    print(_)
for _ in range(2): #reverse order
    print(list(range(10))) 