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


# Enumerate
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
for i,character in enumerate('hello world'):
    print(i, character)

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))

for i,character in enumerate(list(range(0,100))):
    if character == 50:
        print(f'is equal to 50: {character}')
        print(i)
        break

# While Loop 
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("done with  all the work")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Pass 
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed

# Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

for  character in enumerate(picture):
    # print(character)
    if character == 0:
        print('')
    if character == 1:
        print('*')
    # print(character)

