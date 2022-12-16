# print("hello world! it clement first python code")
n = 5
while n > 0:
    # print(n)
    n = n - 1
# print("hello world")

# init and float
# print(type(6)) # int
# print(type(2 -4)) # int
# print(type(2 * 4)) # int
# print(type( 2 / 4)) # 0.5 float
# print(type( 2 ** 3)) # int
# print(type( 5 % 4)) # int
# print( 2 ** 2) # int

# formatted strings
name = "Johnny"
age = 44
print('hi {}. you are {} years old'.format(name, age))
print('hi {}. you are {} years old'.format("Clement", "24"))
print(f'hi {name}. you are {age} years old')

print('hi {new_name}. you are {age} years old'.format(new_name="sander", age=20))

# [start: stop: stepOver]
# filter_number = '123456'
# print(filter_number[::2])

# birth_year = input('what year were you born')

# now_year_data  = 2022
# subtract_year = now_year_data - int(birth_year)

# print(f"{birth_year} i'm born on {birth_year}, and my age is {subtract_year}")

# Password converter
user_name = input("user name")
password = input("password")
multiple_password = len(password)

hidden_password = '*' * multiple_password

print(f'{user_name} your password is {hidden_password} is {len(password)} letter long')